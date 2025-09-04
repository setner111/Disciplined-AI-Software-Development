<img src="https://banes-lab.com/assets/images/banes_lab/700px_Main_Animated.gif" width="70" />

## 📂 Folder: tests - Current Tree Structure
```
📂 tests
├─ ⚡ benchmark.js (138 lines)
├─ 📜 check-regressions.js (117 lines)
├─ 📜 result-paths.js (19 lines)
├─ ⚡ run-benchmarks.js (32 lines)
├─ 🧪 run-stress-tests.js (48 lines)
└─ 📜 stress.js (108 lines)
```

## 📄 Project File Contents


=== File: tests\benchmark.js (138 lines) ===

```javascript
const { performance } = require('perf_hooks');
const fs = require('fs').promises;
const path = require('path');
const { PATH_BASELINE, PATH_OUTPUT } = require('./result-paths');

class BenchmarkFramework {
    constructor(outputPath = PATH_OUTPUT) {
        this.results = {};
        this.baselines = {};
        this.outputPath = outputPath;
        this.baselinePath = PATH_BASELINE;
    }

    async loadBaselines() {
        try {
            const data = await fs.readFile(this.baselinePath, 'utf8');
            this.baselines = JSON.parse(data);
        } catch {
            this.baselines = {};
        }
    }

    async measureTime(fn, iterations = 1000) {
        const measurements = [];
        const sampleCount = 10;
        
        for (let i = 0; i < sampleCount; i++) {
            const start = performance.now();
            for (let j = 0; j < iterations; j++) {
                await fn();
            }
            measurements.push((performance.now() - start) / iterations);
        }
        
        measurements.sort((a, b) => a - b);
        return measurements[Math.floor(measurements.length / 2)];
    }

    measureMemory() {
        if (global.gc) global.gc();
        const usage = process.memoryUsage();
        return Math.round(usage.heapUsed / 1024 / 1024 * 100) / 100;
    }

    async testComponent(name, testFn, iterations = 1000) {
        if (['audit_logging', 'docs_generation'].includes(name)) {
            iterations = 50;
        }
        console.log(`Testing ${name}...`);
        
        const memoryBefore = this.measureMemory();
        let status = 'pass';
        let totalTime = 0;
        
        try {
            totalTime = await this.measureTime(testFn, iterations);
        } catch (err) {
            status = 'fail';
            console.log(`${name}: FAIL - ${err.message}`);
        }
        
        const memoryAfter = this.measureMemory();
        
        this.results[name] = {
            speed_ms: Math.round(totalTime * 100) / 100,
            memory_mb: memoryAfter,
            memory_delta_mb: Math.round((memoryAfter - memoryBefore) * 100) / 100,
            status: status,
            timestamp: new Date().toISOString()
        };
        
        this.checkRegression(name);
        console.log(`${name}: ${status} (${this.results[name].speed_ms}ms)`);
    }

    checkRegression(componentName) {
        const baseline = this.baselines[componentName];
        const current = this.results[componentName];
        
        if (!baseline) return;
        
        const speedDifference = current.speed_ms - baseline.speed_ms;
        const memoryDifference = current.memory_mb - baseline.memory_mb;
        
        current.baseline_comparison = {
            speed_change_ms: Math.round(speedDifference * 100) / 100,
            memory_change_mb: Math.round(memoryDifference * 100) / 100,
            baseline_speed_ms: baseline.speed_ms,
            baseline_memory_mb: baseline.memory_mb
        };
        
        if (speedDifference > 5) {
            console.warn(`⚠️ ${componentName}: Speed regression (+${speedDifference.toFixed(2)}ms)`);
        }
        if (memoryDifference > 10) {
            console.warn(`⚠️ ${componentName}: Memory regression (+${memoryDifference.toFixed(2)}MB)`);
        }
    }

    async saveResults() {
        let existingResults = {};
        try {
            const data = await fs.readFile(this.outputPath, 'utf8');
            existingResults = JSON.parse(data);
        } catch {
            // File doesn't exist or invalid JSON, start fresh
        }

        const mergedResults = { ...existingResults, ...this.results };
        
        await fs.mkdir(path.dirname(this.outputPath), { recursive: true });
        await fs.writeFile(this.outputPath, JSON.stringify(mergedResults, null, 2));
        console.log(`Results saved to ${this.outputPath}`);
    }

    async updateBaseline() {
        await fs.mkdir(path.dirname(this.baselinePath), { recursive: true });
        await fs.writeFile(this.baselinePath, JSON.stringify(this.results, null, 2));
        console.log('Baseline updated');
    }

    printSummary() {
        const components = Object.keys(this.results);
        const passed = components.filter(name => this.results[name].status === 'pass').length;
        const failed = components.length - passed;
        
        console.log(`\nTested: ${components.length}, Passed: ${passed}, Failed: ${failed}`);
        
        components.forEach(name => {
            const result = this.results[name];
            if (result.status === 'pass') {
                console.log(`${name}: ${result.speed_ms}ms, ${result.memory_per_op_mb || 0}MB`);
            }
        });
    }
}

module.exports = BenchmarkFramework;
```

=== File: tests\check-regressions.js (117 lines) ===

```javascript
const fs = require('fs').promises;
const { PATH_OUTPUT, PATH_BASELINE, PATH_PR_BASELINE } = require('./result-paths');

const SPEED_REGRESSION_THRESHOLD_MS = 5;
const MEMORY_REGRESSION_THRESHOLD_MB = 10;
const SPEED_IMPROVEMENT_THRESHOLD_MS = 2;
const MEMORY_IMPROVEMENT_THRESHOLD_MB = 5;

const SKIP_COMPONENTS = ['audit_logging', 'docs_generation'];

async function checkRegressions() {
    const resultsPath = PATH_OUTPUT;
    const isCI = process.env.CI === 'true';
    const baselinePath = isCI ? PATH_PR_BASELINE : PATH_BASELINE;

    let results, baseline;

    try {
        results = JSON.parse(await fs.readFile(resultsPath, 'utf8'));
    } catch (error) {
        console.error('Failed to read results:', error.message);
        process.exit(1);
    }

    try {
        baseline = JSON.parse(await fs.readFile(baselinePath, 'utf8'));
    } catch {
        if (isCI && process.env.GITHUB_REF === 'refs/heads/main') {
            console.log('Main branch: No baseline exists, will be created by workflow');
            process.exit(0);
        }
        if (isCI && process.env.GITHUB_REF !== 'refs/heads/main') {
            console.error('No baseline found for PR comparison. Run benchmarks on main branch first.');
            process.exit(1);
        }
        await fs.writeFile(baselinePath, JSON.stringify(results, null, 2));
        console.log(`Baseline established at ${baselinePath}`);
        process.exit(0);
    }

    const regressions = [];
    const improvements = [];

    for (const [component, result] of Object.entries(results)) {
        if (!baseline[component] || result.status !== 'pass') continue;
        if (SKIP_COMPONENTS.includes(component)) continue;

        const baselineResult = baseline[component];

        const speedChange = result.speed_ms - baselineResult.speed_ms;
        if (speedChange > SPEED_REGRESSION_THRESHOLD_MS) {
            regressions.push({
                component,
                type: 'speed',
                change: speedChange.toFixed(2),
                current: result.speed_ms,
                baseline: baselineResult.speed_ms
            });
        } else if (speedChange < -SPEED_IMPROVEMENT_THRESHOLD_MS) {
            improvements.push({
                component,
                type: 'speed',
                improvement: Math.abs(speedChange).toFixed(2)
            });
        }

        const memoryChange = result.memory_mb - baselineResult.memory_mb;
        if (memoryChange > MEMORY_REGRESSION_THRESHOLD_MB) {
            regressions.push({
                component,
                type: 'memory',
                change: memoryChange.toFixed(2),
                current: result.memory_mb,
                baseline: baselineResult.memory_mb
            });
        } else if (memoryChange < -MEMORY_IMPROVEMENT_THRESHOLD_MB) {
            improvements.push({
                component,
                type: 'memory',
                improvement: Math.abs(memoryChange).toFixed(2)
            });
        }
    }

    if (improvements.length > 0) {
        console.log('Performance improvements detected:');
        improvements.forEach(imp => {
            const unit = imp.type === 'speed' ? 'ms' : 'MB';
            console.log(`  ✓ ${imp.component}: ${imp.type} improved by ${imp.improvement}${unit}`);
        });
    }

    if (regressions.length > 0) {
        console.log('Performance regressions detected:');
        regressions.forEach(reg => {
            const unit = reg.type === 'speed' ? 'ms' : 'MB';
            console.log(`  ✗ ${reg.component}: ${reg.type} regression +${reg.change}${unit} (${reg.current} vs ${reg.baseline})`);
        });
        console.log(`\nFailed: ${regressions.length} regressions exceed thresholds`);
        console.log(`Speed threshold: ${SPEED_REGRESSION_THRESHOLD_MS}ms, Memory threshold: ${MEMORY_REGRESSION_THRESHOLD_MB}MB`);
        process.exit(1);
    }

    if (improvements.length > 0) {
        console.log('Updating baseline with improvements...');
        await fs.writeFile(baselinePath, JSON.stringify(results, null, 2));
    }

    console.log('All performance checks passed');
    process.exit(0);
}

if (require.main === module) {
    checkRegressions().catch(console.error);
}

module.exports = { checkRegressions };
```

=== File: tests\result-paths.js (19 lines) ===

```javascript
const path = require('path');

const PATH_BASELINE = path.join(__dirname, 'data', 'baseline.json');
const PATH_PR_BASELINE = path.join(__dirname, 'data', 'pr-baseline.json');
const PATH_RESULTS = path.join(__dirname, 'data', 'results.json');
const PATH_PR_RESULTS = path.join(__dirname, 'data', 'pr-results.json');
const PATH_STRESS = path.join(__dirname, 'data', 'stress-results.json');

const isCI = process.env.CI === 'true';
const PATH_OUTPUT = isCI ? PATH_PR_RESULTS : PATH_RESULTS;

module.exports = {
    PATH_BASELINE,
    PATH_PR_BASELINE,
    PATH_RESULTS,
    PATH_PR_RESULTS,
    PATH_OUTPUT,
    PATH_STRESS
}
```

=== File: tests\run-benchmarks.js (32 lines) ===

```javascript
const BenchmarkFramework = require('./benchmark.js');
const coreTests = require('./suites/core-tests');
const dataTests = require('./suites/data-tests');
const securityTests = require('./suites/security-tests');
const handlerTests = require('./suites/handler-tests');

async function runAllBenchmarks() {
    const benchmark = new BenchmarkFramework();
    await benchmark.loadBaselines();

    console.log('Starting benchmarks\n');

    await coreTests.run(benchmark);
    await dataTests.run(benchmark);
    await securityTests.run(benchmark);
    await handlerTests.run(benchmark);

    benchmark.printSummary();
    await benchmark.saveResults();

    if (process.argv.includes('--update-baseline')) {
        await benchmark.updateBaseline();
    }

    process.exit(0);
}

if (require.main === module) {
    runAllBenchmarks().catch(console.error);
}

module.exports = { runAllBenchmarks };
```

=== File: tests\run-stress-tests.js (48 lines) ===

```javascript
const StressTestFramework = require('./stress');
const { runDatabaseStressTests } = require('./stress/stress-database');
const { runSecurityStressTests } = require('./stress/stress-security');
const { runPluginStressTests } = require('./stress/stress-plugins');
const { runApiStressTests } = require('./stress/stress-api');
const { runMemoryLeakTests } = require('./stress/stress-memory');
const { validateCriticalFailures } = require('./stress/stress-validators');

async function runAllStressTests() {
    console.log('Starting stress testing suite\n');
    
    const stress = new StressTestFramework();
    
    try {
        await runDatabaseStressTests(stress);
        await runSecurityStressTests(stress);
        await runPluginStressTests(stress);
        await runApiStressTests(stress);
        await runMemoryLeakTests(stress);
        
        stress.printSummary();
        await stress.saveResults();
        
        const criticalFailures = validateCriticalFailures(stress.results);
        
        if (criticalFailures.length > 0) {
            console.log('\n⚠️  CRITICAL ISSUES DETECTED:');
            criticalFailures.forEach(([name, result]) => {
                console.log(`  ${name}: ${JSON.stringify(result, null, 2)}`);
            });
            process.exit(1);
        } else {
            console.log('\n✅ All stress tests passed');
        }
        
    } catch (error) {
        console.error('Stress testing failed:', error);
        process.exit(1);
    }
    
    process.exit(0);
}

if (require.main === module) {
    runAllStressTests().catch(console.error);
}

module.exports = { runAllStressTests };
```

=== File: tests\stress.js (108 lines) ===

```javascript
const { performance } = require('perf_hooks');
const fs = require('fs').promises;
const path = require('path');
const { PATH_STRESS } = require('./result-paths');

class StressTestFramework {
    constructor() {
        this.results = {};
        this.outputPath = PATH_STRESS
        this.isRunning = false;
    }

    async runConcurrentTest(name, testFn, concurrency, duration) {
        console.log(`Stress testing ${name} (${concurrency} concurrent, ${duration}ms)`);
        
        const results = { operations: 0, errors: 0, memoryStart: this.getMemoryUsage(), memoryPeak: 0 };
        const responseTimes = [];
        
        this.isRunning = true;
        const workers = [];
        for (let i = 0; i < concurrency; i++) {
            workers.push(this.createWorker(testFn, duration, results, responseTimes));
        }
        
        const startTime = performance.now();
        await Promise.all(workers);
        const totalTime = performance.now() - startTime;
        
        results.opsPerSecond = (results.operations / totalTime) * 1000;
        results.errorRate = (results.errors / results.operations) * 100;
        results.avgResponseTime = responseTimes.reduce((a, b) => a + b, 0) / responseTimes.length;
        results.memoryGrowth = this.getMemoryUsage() - results.memoryStart;
        
        this.results[name] = results;
        this.isRunning = false;
        
        console.log(`${name}: ${results.operations} ops, ${results.opsPerSecond.toFixed(2)} ops/sec`);
        return results;
    }

    async createWorker(testFn, duration, results, responseTimes) {
        const endTime = performance.now() + duration;
        
        while (performance.now() < endTime && this.isRunning) {
            const opStart = performance.now();
            
            try {
                await testFn();
                results.operations++;
                responseTimes.push(performance.now() - opStart);
            } catch (error) {
                results.errors++;
            }
        }
    }

    async runSustainedTest(name, testFn, duration) {
        console.log(`Sustained test ${name} (${duration}ms)`);
        
        const results = { operations: 0, errors: 0, memoryStart: this.getMemoryUsage() };
        const endTime = performance.now() + duration;
        
        while (performance.now() < endTime) {
            const opStart = performance.now();
            
            try {
                await testFn();
                results.operations++;
            } catch (error) {
                results.errors++;
            }
            
            await new Promise(resolve => setTimeout(resolve, 10));
        }
        
        results.opsPerSecond = (results.operations / duration) * 1000;
        results.errorRate = (results.errors / results.operations) * 100;
        results.memoryGrowth = this.getMemoryUsage() - results.memoryStart;
        
        this.results[name] = results;
        console.log(`${name}: ${results.operations} ops, ${results.opsPerSecond.toFixed(2)} ops/sec`);
        return results;
    }

    getMemoryUsage() {
        return Math.round(process.memoryUsage().heapUsed / 1024 / 1024 * 100) / 100;
    }

    async saveResults() {
        await fs.mkdir(path.dirname(this.outputPath), { recursive: true });
        await fs.writeFile(this.outputPath, JSON.stringify(this.results, null, 2));
        console.log(`Stress test results saved to ${this.outputPath}`);
    }

    printSummary() {
        console.log('\n=== STRESS TEST SUMMARY ===');
        
        Object.entries(this.results).forEach(([name, result]) => {
            console.log(`\n${name}:`);
            console.log(`  Operations: ${result.operations}`);
            console.log(`  Ops/sec: ${result.opsPerSecond?.toFixed(2) || 'N/A'}`);
            console.log(`  Error rate: ${result.errorRate?.toFixed(2) || 0}%`);
            console.log(`  Memory growth: ${result.memoryGrowth?.toFixed(2) || 0}MB`);
        });
    }
}

module.exports = StressTestFramework;
```
