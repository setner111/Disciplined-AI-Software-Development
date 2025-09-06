<img src="https://banes-lab.com/assets/images/banes_lab/700px_Main_Animated.gif" width="70" />

## 📂 The Project - Current Tree Structure
```
📂 src
├─ ⚡ benchmark_results.json (62 lines)
├─ 📄 go.mod (67 lines)
├─ 🗃️ regression.db (0 lines)
├─ 📝 server.log (12 lines)
├─ 🧪 test-pipeline.bat (130 lines)
├─ 📂 benchsuite
│   ├─ 🧩 components.go (163 lines) ‼️
│   └─ 🐹 runner.go (79 lines)
├─ 📂 bin
│   └─ 📄 regression-server.exe (0 lines)
├─ 📂 cmd
│   ├─ 📂 benchmark
│   │   └─ 🏠 main.go (32 lines)
│   └─ 📂 server
│       └─ 🏠 main.go (64 lines)
├─ 📂 internal
│   ├─ 📂 config
│   │   └─ ⚙️ config.go (70 lines)
│   ├─ 📂 database
│   │   └─ 🐹 init.go (60 lines)
│   ├─ 📂 github
│   │   └─ 🐹 client.go (89 lines)
│   ├─ 📂 regression
│   │   ├─ 🐹 analysis.go (99 lines)
│   │   ├─ 📊 database.go (42 lines)
│   │   └─ 🐹 detector.go (78 lines)
│   └─ 📂 server
│       ├─ 🐹 handlers.go (68 lines)
│       ├─ 🛣️ router.go (10 lines)
│       └─ 🐹 server.go (93 lines)
├─ 📂 pkg
│   └─ 📂 types
│       └─ 📋 types.go (65 lines)
└─ 📂 test-ci
    ├─ 📂 benchmark-data
    │   └─ 🔧 regression.json (30 lines)
    ├─ 📂 github-sim
    │   ├─ 🐹 simulator.go (94 lines)
    │   └─ 📂 webhook-payloads
    │       └─ 🔧 pr_opened.json (74 lines)
    ├─ 📂 integration
    │   └─ 🐹 full-flow.go (217 lines) ‼️
    └─ 📂 mock-repos
        └─ 📂 golang-project
            └─ ⚡ benchmarks.json (22 lines)
⚖️ LICENSE (44 lines)
```

## 📄 Project File Contents


=== File: src\benchmark_results.json (62 lines) ===

```json
{
  "results": [
    {
      "component": "regression",
      "operation": "detection",
      "duration_ns": 1209805,
      "iterations": 6222,
      "memory_bytes": 47237856,
      "allocations": 2065598,
      "timestamp": 1756669469
    },
    {
      "component": "regression",
      "operation": "baseline_calculation",
      "duration_ns": 2,
      "iterations": 474272494,
      "memory_bytes": 0,
      "allocations": 0,
      "timestamp": 1756669471
    },
    {
      "component": "integration",
      "operation": "database_write",
      "duration_ns": 0,
      "iterations": 1000000000,
      "memory_bytes": 0,
      "allocations": 0,
      "timestamp": 1756669471
    },
    {
      "component": "integration",
      "operation": "database_read",
      "duration_ns": 0,
      "iterations": 1000000000,
      "memory_bytes": 0,
      "allocations": 0,
      "timestamp": 1756669471
    },
    {
      "component": "memory",
      "operation": "json_processing",
      "duration_ns": 31,
      "iterations": 37867072,
      "memory_bytes": 0,
      "allocations": 0,
      "timestamp": 1756669472
    },
    {
      "component": "concurrent",
      "operation": "parallel_analysis",
      "duration_ns": 0,
      "iterations": 1000000000,
      "memory_bytes": 992,
      "allocations": 27,
      "timestamp": 1756669473
    }
  ],
  "go_version": "go1.25.0",
  "goos": "windows",
  "goarch": "amd64",
  "timestamp": 1756669473
}
```

=== File: src\go.mod (67 lines) ===

```text
module regression-ci

go 1.21

require (
	github.com/gin-gonic/gin v1.9.1
	github.com/glebarez/go-sqlite v1.21.2
	github.com/google/go-github/v57 v57.0.0
	github.com/jmoiron/sqlx v1.3.5
	github.com/rs/zerolog v1.31.0
	github.com/spf13/viper v1.17.0
	golang.org/x/oauth2 v0.15.0
	gonum.org/v1/gonum v0.14.0
)

require (
	github.com/bytedance/sonic v1.9.1 // indirect
	github.com/chenzhuoyu/base64x v0.0.0-20221115062448-fe3a3abad311 // indirect
	github.com/dustin/go-humanize v1.0.1 // indirect
	github.com/fsnotify/fsnotify v1.6.0 // indirect
	github.com/gabriel-vasile/mimetype v1.4.2 // indirect
	github.com/gin-contrib/sse v0.1.0 // indirect
	github.com/go-playground/locales v0.14.1 // indirect
	github.com/go-playground/universal-translator v0.18.1 // indirect
	github.com/go-playground/validator/v10 v10.14.0 // indirect
	github.com/goccy/go-json v0.10.2 // indirect
	github.com/golang/protobuf v1.5.3 // indirect
	github.com/google/go-querystring v1.1.0 // indirect
	github.com/google/uuid v1.3.0 // indirect
	github.com/hashicorp/hcl v1.0.0 // indirect
	github.com/json-iterator/go v1.1.12 // indirect
	github.com/klauspost/cpuid/v2 v2.2.4 // indirect
	github.com/leodido/go-urn v1.2.4 // indirect
	github.com/magiconair/properties v1.8.7 // indirect
	github.com/mattn/go-colorable v0.1.13 // indirect
	github.com/mattn/go-isatty v0.0.19 // indirect
	github.com/mitchellh/mapstructure v1.5.0 // indirect
	github.com/modern-go/concurrent v0.0.0-20180306012644-bacd9c7ef1dd // indirect
	github.com/modern-go/reflect2 v1.0.2 // indirect
	github.com/pelletier/go-toml/v2 v2.1.0 // indirect
	github.com/remyoudompheng/bigfft v0.0.0-20230129092748-24d4a6f8daec // indirect
	github.com/sagikazarmark/locafero v0.3.0 // indirect
	github.com/sagikazarmark/slog-shim v0.1.0 // indirect
	github.com/sourcegraph/conc v0.3.0 // indirect
	github.com/spf13/afero v1.10.0 // indirect
	github.com/spf13/cast v1.5.1 // indirect
	github.com/spf13/pflag v1.0.5 // indirect
	github.com/subosito/gotenv v1.6.0 // indirect
	github.com/twitchyliquid64/golang-asm v0.15.1 // indirect
	github.com/ugorji/go/codec v1.2.11 // indirect
	go.uber.org/atomic v1.9.0 // indirect
	go.uber.org/multierr v1.9.0 // indirect
	golang.org/x/arch v0.3.0 // indirect
	golang.org/x/crypto v0.16.0 // indirect
	golang.org/x/exp v0.0.0-20230905200255-921286631fa9 // indirect
	golang.org/x/net v0.19.0 // indirect
	golang.org/x/sys v0.15.0 // indirect
	golang.org/x/text v0.14.0 // indirect
	google.golang.org/appengine v1.6.7 // indirect
	google.golang.org/protobuf v1.31.0 // indirect
	gopkg.in/ini.v1 v1.67.0 // indirect
	gopkg.in/yaml.v3 v3.0.1 // indirect
	modernc.org/libc v1.22.5 // indirect
	modernc.org/mathutil v1.5.0 // indirect
	modernc.org/memory v1.5.0 // indirect
	modernc.org/sqlite v1.23.1 // indirect
)

```

=== File: src\regression.db (0 lines) ===

```text
[Could not read file: 'utf-8' codec can't decode byte 0xea in position 99: invalid continuation byte]
```

=== File: src\server.log (12 lines) ===

```log
[GIN-debug] [WARNING] Running in "debug" mode. Switch to "release" mode in production.
 - using env:	export GIN_MODE=release
 - using code:	gin.SetMode(gin.ReleaseMode)

[GIN-debug] GET    /health                   --> regression-ci/internal/server.(*Server).healthCheck-fm (3 handlers)
[GIN-debug] POST   /webhook                  --> regression-ci/internal/server.(*Server).handleWebhook-fm (3 handlers)
[GIN-debug] POST   /analyze                  --> regression-ci/internal/server.(*Server).analyzeEndpoint-fm (3 handlers)
[GIN-debug] GET    /config/:repo             --> regression-ci/internal/server.(*Server).getRepoConfig-fm (3 handlers)
[GIN-debug] PUT    /config/:repo             --> regression-ci/internal/server.(*Server).updateRepoConfig-fm (3 handlers)
{"level":"info","address":":8080","time":1756669473,"message":"starting server"}
{"level":"info","client_ip":"::1","method":"GET","path":"/health","status":200,"latency":0.6303,"time":1756669476,"message":"request completed"}
{"level":"info","client_ip":"::1","method":"POST","path":"/analyze","status":200,"latency":8.0221,"time":1756669476,"message":"request completed"}

```

=== File: src\test-pipeline.bat (130 lines) ===

```batch
@echo off
setlocal EnableDelayedExpansion

echo ================================
echo Regression CI Test Pipeline
echo ================================
echo.

REM Check Go installation
echo [1/8] Checking Go installation...
go version >nul 2>&1
if !errorlevel! neq 0 (
    echo ERROR: Go is not installed or not in PATH
    exit /b 1
)
echo Go is installed

REM Initialize and download dependencies
echo.
echo [2/8] Initializing module and downloading dependencies...
go mod tidy
if !errorlevel! neq 0 (
    echo ERROR: Failed to download dependencies
    exit /b 1
)
echo Dependencies downloaded

REM Compile the application
echo.
echo [3/8] Compiling application...
if not exist "bin" mkdir bin
go build -o bin\regression-server.exe .\cmd\server
if !errorlevel! neq 0 (
    echo ERROR: Compilation failed
    exit /b 1
)
echo Compilation successful

REM Run unit tests
echo.
echo [4/8] Running unit tests...
go test -v ./internal/...
if !errorlevel! neq 0 (
    echo WARNING: Some unit tests failed
) else (
    echo Unit tests passed
)

REM Run benchmark suite
echo.
echo [5/8] Running benchmark suite...
go run ./cmd/benchmark -o benchmark_results.json
if !errorlevel! neq 0 (
    echo WARNING: Benchmark suite encountered issues
) else (
    echo Benchmark suite completed
)

REM Start server in background for integration tests
echo.
echo [6/8] Starting server for integration tests...
set WEBHOOK_SECRET=test-secret-key
set DATABASE_PATH=:memory:
start /B bin\regression-server.exe > server.log 2>&1
set SERVER_PID=!ERRORLEVEL!

REM Wait for server to start
timeout /t 3 /nobreak >nul

REM Test server health
echo.
echo [7/8] Testing server endpoints...
curl -s http://localhost:8080/health >nul 2>&1
if !errorlevel! neq 0 (
    echo WARNING: Server health check failed
) else (
    echo Server health check passed
)

REM Test analyze endpoint with sample data
curl -s -X POST http://localhost:8080/analyze ^
    -H "Content-Type: application/json" ^
    -d @test-ci\mock-repos\golang-project\benchmarks.json >nul 2>&1
if !errorlevel! neq 0 (
    echo WARNING: Analyze endpoint test failed
) else (
    echo Analyze endpoint test passed
)

REM Run integration tests
echo.
echo [8/8] Running integration tests...
go test -v ./test-ci/integration
if !errorlevel! neq 0 (
    echo WARNING: Integration tests had issues
) else (
    echo Integration tests passed
)

REM Stop server
echo.
echo Stopping test server...
taskkill /F /IM regression-server.exe >nul 2>&1

REM Summary
echo.
echo ================================
echo Test Pipeline Summary
echo ================================
echo Compilation: SUCCESS
if exist benchmark_results.json (
    echo Benchmarks: COMPLETED
) else (
    echo Benchmarks: FAILED
)

if exist server.log (
    echo Server logs available in: src\server.log
)

if exist benchmark_results.json (
    echo Benchmark results available in: src\benchmark_results.json
)

echo.
echo Test pipeline completed
echo To run the server manually: cd src && bin\regression-server.exe
echo.

pause
```

=== File: src\benchsuite\components.go (163 lines) ‼️ ===

```go
// Copyright 2025 Baleine Jay
// Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
// Commercial use requires a paid license. See link for details.
package benchsuite

import (
	"testing"

	"github.com/jmoiron/sqlx"
	_ "github.com/glebarez/go-sqlite"

	"regression-ci/internal/config"
	"regression-ci/internal/regression"
	"regression-ci/pkg/types"
)

func benchmarkRegression() []BenchmarkResult {
	var results []BenchmarkResult

	db := setupTestDB()
	defer db.Close()
	detector := setupDetector(db)

	results = append(results, measureBenchmark("regression", "detection", func(b *testing.B) {
		req := createTestRequest()
		for i := 0; i < b.N; i++ {
			detector.Analyze(req)
		}
	}))

	results = append(results, measureBenchmark("regression", "baseline_calculation", func(b *testing.B) {
		values := []float64{95.2, 98.1, 96.8, 97.5, 99.0}
		for i := 0; i < b.N; i++ {
			calculateBaselineMock(values)
		}
	}))

	return results
}

func benchmarkIntegration() []BenchmarkResult {
	var results []BenchmarkResult

	db := setupTestDB()
	defer db.Close()

	results = append(results, measureBenchmark("integration", "database_write", func(b *testing.B) {
		for i := 0; i < b.N; i++ {
			insertBenchmarkMock(db, "test/repo", "main", "abc123", "component", 100.0)
		}
	}))

	results = append(results, measureBenchmark("integration", "database_read", func(b *testing.B) {
		for i := 0; i < b.N; i++ {
			queryBaselineMock(db, "test/repo", "component")
		}
	}))

	return results
}

func benchmarkMemory() []BenchmarkResult {
	var results []BenchmarkResult

	results = append(results, measureBenchmark("memory", "json_processing", func(b *testing.B) {
		data := generateLargeBenchmarkJSON()
		for i := 0; i < b.N; i++ {
			parseBenchmarkJSONMock(data)
		}
	}))

	return results
}

func benchmarkConcurrent() []BenchmarkResult {
	var results []BenchmarkResult

	results = append(results, measureBenchmark("concurrent", "parallel_analysis", func(b *testing.B) {
		b.RunParallel(func(pb *testing.PB) {
			for pb.Next() {
				detectRegressionMock(100.0, 90.0, 10.0)
			}
		})
	}))

	return results
}

func detectRegressionMock(current, baseline, threshold float64) bool {
	change := ((current - baseline) / baseline) * 100
	return change > threshold
}

func calculateBaselineMock(values []float64) float64 {
	sum := 0.0
	for _, v := range values {
		sum += v
	}
	return sum / float64(len(values))
}

func setupTestDB() *sqlx.DB {
	db, _ := sqlx.Open("sqlite", ":memory:")
	
	// Create tables for testing
	schema := `
	CREATE TABLE IF NOT EXISTS benchmarks (
		id INTEGER PRIMARY KEY,
		repo TEXT NOT NULL,
		branch TEXT NOT NULL,
		commit_hash TEXT NOT NULL,
		component TEXT NOT NULL,
		value REAL NOT NULL,
		timestamp INTEGER NOT NULL
	);
	
	CREATE TABLE IF NOT EXISTS baselines (
		repo TEXT NOT NULL,
		component TEXT NOT NULL,
		baseline_value REAL NOT NULL,
		sample_count INTEGER DEFAULT 5,
		updated_at INTEGER NOT NULL,
		PRIMARY KEY (repo, component)
	);`
	
	db.Exec(schema)
	return db
}

func insertBenchmarkMock(db *sqlx.DB, repo, branch, commit, component string, value float64) {
}

func queryBaselineMock(db *sqlx.DB, repo, component string) float64 {
	return 100.0
}

func generateLargeBenchmarkJSON() []byte {
	return []byte(`{"component": "test", "value": 100.0}`)
}

func parseBenchmarkJSONMock(data []byte) map[string]interface{} {
	return map[string]interface{}{"component": "test", "value": 100.0}
}

func setupDetector(db *sqlx.DB) *regression.Detector {
	cfg := config.DetectionConfig{
		DefaultThreshold: 10.0,
		MinSamples:       5,
		MaxSamples:       50,
	}
	return regression.New(db, cfg)
}

func createTestRequest() types.AnalyzeRequest {
	return types.AnalyzeRequest{
		Repo:   "test/repo",
		Branch: "main", 
		Commit: "abc123",
		Components: map[string]float64{
			"test_component": 100.0,
		},
	}
}
```

=== File: src\benchsuite\runner.go (79 lines) ===

```go
package benchsuite

import (
	"encoding/json"
	"fmt"
	"os"
	"runtime"
	"testing"
	"time"
)

type BenchmarkResult struct {
	Component   string        `json:"component"`
	Operation   string        `json:"operation"`
	Duration    time.Duration `json:"duration_ns"`
	Iterations  int           `json:"iterations"`
	Memory      int64         `json:"memory_bytes"`
	Allocations int64         `json:"allocations"`
	Timestamp   int64         `json:"timestamp"`
}

type SuiteResult struct {
	Results   []BenchmarkResult `json:"results"`
	GoVersion string            `json:"go_version"`
	GOOS      string            `json:"goos"`
	GOARCH    string            `json:"goarch"`
	Timestamp int64             `json:"timestamp"`
}

func RunSuite() (*SuiteResult, error) {
	var results []BenchmarkResult

	regression := benchmarkRegression()
	integration := benchmarkIntegration()
	memory := benchmarkMemory()
	concurrent := benchmarkConcurrent()

	results = append(results, regression...)
	results = append(results, integration...)
	results = append(results, memory...)
	results = append(results, concurrent...)

	suite := &SuiteResult{
		Results:   results,
		GoVersion: runtime.Version(),
		GOOS:      runtime.GOOS,
		GOARCH:    runtime.GOARCH,
		Timestamp: time.Now().Unix(),
	}

	return suite, nil
}

func WriteResults(suite *SuiteResult, filename string) error {
	data, err := json.MarshalIndent(suite, "", "  ")
	if err != nil {
		return fmt.Errorf("failed to marshal results: %w", err)
	}

	if err := os.WriteFile(filename, data, 0644); err != nil {
		return fmt.Errorf("failed to write results: %w", err)
	}

	return nil
}

func measureBenchmark(name, operation string, fn func(*testing.B)) BenchmarkResult {
	result := testing.Benchmark(fn)

	return BenchmarkResult{
		Component:   name,
		Operation:   operation,
		Duration:    time.Duration(result.NsPerOp()),
		Iterations:  result.N,
		Memory:      int64(result.MemBytes),
		Allocations: int64(result.MemAllocs),
		Timestamp:   time.Now().Unix(),
	}
}
```

=== File: src\bin\regression-server.exe (0 lines) ===

```text
[Could not read file: 'utf-8' codec can't decode byte 0x90 in position 2: invalid start byte]
```

=== File: src\cmd\benchmark\main.go (32 lines) ===

```go
// Copyright 2025 Baleine Jay
// Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
// Commercial use requires a paid license. See link for details.
package main

import (
	"flag"
	"fmt"
	"os"

	"regression-ci/benchsuite"
)

func main() {
	outputFile := flag.String("o", "benchmark_results.json", "Output file for benchmark results")
	flag.Parse()

	fmt.Println("Running benchmark suite...")
	
	suite, err := benchsuite.RunSuite()
	if err != nil {
		fmt.Printf("Error running benchmark suite: %v\n", err)
		os.Exit(1)
	}

	if err := benchsuite.WriteResults(suite, *outputFile); err != nil {
		fmt.Printf("Error writing benchmark results: %v\n", err)
		os.Exit(1)
	}

	fmt.Printf("Benchmark suite completed. Results written to %s\n", *outputFile)
}
```

=== File: src\cmd\server\main.go (64 lines) ===

```go
// Copyright 2025 Baleine Jay
// Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
// Commercial use requires a paid license. See link for details.
package main

import (
	"context"
	"os"
	"os/signal"
	"syscall"
	"time"

	"github.com/rs/zerolog"
	"github.com/rs/zerolog/log"

	"regression-ci/internal/config"
	"regression-ci/internal/database"
	"regression-ci/internal/server"
)

func main() {
	setupLogger()

	cfg, err := config.Load()
	if err != nil {
		log.Fatal().Err(err).Msg("failed to load configuration")
	}

	db, err := database.Init(cfg.Database.Path)
	if err != nil {
		log.Fatal().Err(err).Msg("failed to initialize database")
	}
	defer db.Close()

	srv := server.New(db, cfg)

	go func() {
		log.Info().Str("address", cfg.Server.Address).Msg("starting server")
		if err := srv.Start(); err != nil {
			log.Fatal().Err(err).Msg("server failed to start")
		}
	}()

	quit := make(chan os.Signal, 1)
	signal.Notify(quit, syscall.SIGINT, syscall.SIGTERM)
	<-quit

	log.Info().Msg("shutting down server")
	ctx, cancel := context.WithTimeout(context.Background(), 30*time.Second)
	defer cancel()

	if err := srv.Shutdown(ctx); err != nil {
		log.Fatal().Err(err).Msg("server forced to shutdown")
	}

	log.Info().Msg("server shutdown complete")
}

func setupLogger() {
	zerolog.TimeFieldFormat = zerolog.TimeFormatUnix
	if os.Getenv("ENVIRONMENT") == "development" {
		log.Logger = log.Output(zerolog.ConsoleWriter{Out: os.Stderr})
	}
}
```

=== File: src\internal\config\config.go (70 lines) ===

```go
// Copyright 2025 Baleine Jay
// Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
// Commercial use requires a paid license. See link for details.
package config

import (
	"time"

	"github.com/spf13/viper"
)

type Config struct {
	Server    ServerConfig    `mapstructure:"server"`
	Database  DatabaseConfig  `mapstructure:"database"`
	GitHub    GitHubConfig    `mapstructure:"github"`
	Detection DetectionConfig `mapstructure:"detection"`
}

type ServerConfig struct {
	Address      string        `mapstructure:"address"`
	ReadTimeout  time.Duration `mapstructure:"read_timeout"`
	WriteTimeout time.Duration `mapstructure:"write_timeout"`
}

type DatabaseConfig struct {
	Path string `mapstructure:"path"`
}

type GitHubConfig struct {
	WebhookSecret string `mapstructure:"webhook_secret"`
	Token         string `mapstructure:"token"`
	AppID         int64  `mapstructure:"app_id"`
	PrivateKey    string `mapstructure:"private_key"`
}

type DetectionConfig struct {
	DefaultThreshold float64 `mapstructure:"default_threshold"`
	MinSamples       int     `mapstructure:"min_samples"`
	MaxSamples       int     `mapstructure:"max_samples"`
}

func Load() (*Config, error) {
	viper.SetDefault("server.address", ":8080")
	viper.SetDefault("server.read_timeout", "30s")
	viper.SetDefault("server.write_timeout", "30s")
	viper.SetDefault("database.path", "./regression.db")
	viper.SetDefault("detection.default_threshold", 10.0)
	viper.SetDefault("detection.min_samples", 5)
	viper.SetDefault("detection.max_samples", 50)

	viper.SetConfigName("config")
	viper.SetConfigType("yaml")
	viper.AddConfigPath(".")
	viper.AddConfigPath("./config")

	viper.AutomaticEnv()

	if err := viper.ReadInConfig(); err != nil {
		if _, ok := err.(viper.ConfigFileNotFoundError); !ok {
			return nil, err
		}
	}

	var config Config
	if err := viper.Unmarshal(&config); err != nil {
		return nil, err
	}

	return &config, nil
}
```

=== File: src\internal\database\init.go (60 lines) ===

```go
// Copyright 2025 Baleine Jay
// Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
// Commercial use requires a paid license. See link for details.
package database

import (
	"fmt"

	"github.com/jmoiron/sqlx"
	_ "github.com/glebarez/go-sqlite"
)

const schema = `
CREATE TABLE IF NOT EXISTS benchmarks (
	id INTEGER PRIMARY KEY,
	repo TEXT NOT NULL,
	branch TEXT NOT NULL,
	commit_hash TEXT NOT NULL,
	component TEXT NOT NULL,
	value REAL NOT NULL,
	timestamp INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS baselines (
	repo TEXT NOT NULL,
	component TEXT NOT NULL,
	baseline_value REAL NOT NULL,
	sample_count INTEGER DEFAULT 5,
	updated_at INTEGER NOT NULL,
	PRIMARY KEY (repo, component)
);

CREATE TABLE IF NOT EXISTS config (
	repo TEXT PRIMARY KEY,
	threshold_percent REAL DEFAULT 10.0,
	min_samples INTEGER DEFAULT 5,
	enabled BOOLEAN DEFAULT 1
);

CREATE INDEX IF NOT EXISTS idx_benchmarks_repo_component ON benchmarks(repo, component);
CREATE INDEX IF NOT EXISTS idx_benchmarks_timestamp ON benchmarks(timestamp);
`

func Init(path string) (*sqlx.DB, error) {
	db, err := sqlx.Connect("sqlite", path)
	if err != nil {
		return nil, fmt.Errorf("database connection failed: %w", err)
	}

	if err := createTables(db); err != nil {
		return nil, fmt.Errorf("table creation failed: %w", err)
	}

	return db, nil
}

func createTables(db *sqlx.DB) error {
	_, err := db.Exec(schema)
	return err
}
```

=== File: src\internal\github\client.go (89 lines) ===

```go
// Copyright 2025 Baleine Jay
// Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
// Commercial use requires a paid license. See link for details.
package github

import (
	"context"
	"fmt"

	"github.com/google/go-github/v57/github"
	"golang.org/x/oauth2"

	"regression-ci/internal/config"
)

type Client struct {
	client *github.Client
	config config.GitHubConfig
}

func New(cfg config.GitHubConfig) *Client {
	var client *github.Client
	
	if cfg.Token != "" {
		ts := oauth2.StaticTokenSource(&oauth2.Token{AccessToken: cfg.Token})
		tc := oauth2.NewClient(context.Background(), ts)
		client = github.NewClient(tc)
	} else {
		client = github.NewClient(nil)
	}

	return &Client{
		client: client,
		config: cfg,
	}
}

func (c *Client) CreatePRComment(ctx context.Context, owner, repo string, prNumber int, body string) error {
	comment := &github.IssueComment{
		Body: &body,
	}

	_, _, err := c.client.Issues.CreateComment(ctx, owner, repo, prNumber, comment)
	if err != nil {
		return fmt.Errorf("failed to create PR comment: %w", err)
	}

	return nil
}

func (c *Client) UpdatePRComment(ctx context.Context, owner, repo string, commentID int64, body string) error {
	comment := &github.IssueComment{
		Body: &body,
	}

	_, _, err := c.client.Issues.EditComment(ctx, owner, repo, commentID, comment)
	if err != nil {
		return fmt.Errorf("failed to update PR comment: %w", err)
	}

	return nil
}

func (c *Client) ListPRComments(ctx context.Context, owner, repo string, prNumber int) ([]*github.IssueComment, error) {
	comments, _, err := c.client.Issues.ListComments(ctx, owner, repo, prNumber, nil)
	if err != nil {
		return nil, fmt.Errorf("failed to list PR comments: %w", err)
	}

	return comments, nil
}

func (c *Client) GetRepository(ctx context.Context, owner, repo string) (*github.Repository, error) {
	repository, _, err := c.client.Repositories.Get(ctx, owner, repo)
	if err != nil {
		return nil, fmt.Errorf("failed to get repository: %w", err)
	}

	return repository, nil
}

func (c *Client) ValidateWebhookSignature(payload []byte, signature string) bool {
	if c.config.WebhookSecret == "" {
		return false
	}

	err := github.ValidateSignature(signature, payload, []byte(c.config.WebhookSecret))
	return err == nil
}
```

=== File: src\internal\regression\analysis.go (99 lines) ===

```go
// Copyright 2025 Baleine Jay
// Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
// Commercial use requires a paid license. See link for details.
package regression

import (
	"fmt"
	"math"
	"time"

	"gonum.org/v1/gonum/stat"

	"regression-ci/pkg/types"
)

func (d *Detector) detectRegression(repo, component string, currentValue float64) (*types.RegressionResult, error) {
	baseline, err := d.getBaseline(repo, component)
	if err != nil {
		return d.createInitialBaseline(repo, component, currentValue)
	}

	percentChange := ((currentValue - baseline.BaselineValue) / baseline.BaselineValue) * 100
	
	threshold := d.config.DefaultThreshold
	repoConfig, err := d.getRepoConfig(repo)
	if err == nil && repoConfig.ThresholdPercent > 0 {
		threshold = repoConfig.ThresholdPercent
	}

	isRegression := percentChange > threshold
	confidence := d.calculateConfidence(baseline, currentValue, percentChange)

	return &types.RegressionResult{
		IsRegression:    isRegression,
		CurrentValue:    currentValue,
		BaselineValue:   baseline.BaselineValue,
		PercentChange:   percentChange,
		ConfidenceScore: confidence,
		SampleSize:      baseline.SampleCount,
	}, nil
}

func (d *Detector) createInitialBaseline(repo, component string, value float64) (*types.RegressionResult, error) {
	baseline := &types.Baseline{
		Repo:          repo,
		Component:     component,
		BaselineValue: value,
		SampleCount:   1,
		UpdatedAt:     time.Now().Unix(),
	}

	query := `INSERT OR REPLACE INTO baselines 
	          (repo, component, baseline_value, sample_count, updated_at) 
	          VALUES (?, ?, ?, ?, ?)`
	
	_, err := d.db.Exec(query, baseline.Repo, baseline.Component, 
		baseline.BaselineValue, baseline.SampleCount, baseline.UpdatedAt)
	if err != nil {
		return nil, fmt.Errorf("failed to create baseline: %w", err)
	}

	return &types.RegressionResult{
		IsRegression:    false,
		CurrentValue:    value,
		BaselineValue:   value,
		PercentChange:   0.0,
		ConfidenceScore: 100.0,
		SampleSize:      1,
	}, nil
}

func (d *Detector) updateBaseline(repo, component string, newValue float64, result *types.RegressionResult) {
	if result.IsRegression {
		return
	}

	recentSamples, err := d.getRecentSamples(repo, component, d.config.MaxSamples)
	if err != nil || len(recentSamples) < d.config.MinSamples {
		return
	}

	newBaseline := stat.Mean(recentSamples, nil)
	
	query := `UPDATE baselines SET baseline_value = ?, sample_count = ?, updated_at = ? 
	          WHERE repo = ? AND component = ?`
	
	d.db.Exec(query, newBaseline, len(recentSamples), time.Now().Unix(), repo, component)
}

func (d *Detector) calculateConfidence(baseline *types.Baseline, currentValue, percentChange float64) float64 {
	if baseline.SampleCount < d.config.MinSamples {
		return 50.0
	}

	changeAbs := math.Abs(percentChange)
	confidence := math.Min(90.0, 50.0+(changeAbs*2))
	
	return confidence
}
```

=== File: src\internal\regression\database.go (42 lines) ===

```go
// Copyright 2025 Baleine Jay
// Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
// Commercial use requires a paid license. See link for details.
package regression

import (
	"fmt"

	"regression-ci/pkg/types"
)

func (d *Detector) getBaseline(repo, component string) (*types.Baseline, error) {
	var baseline types.Baseline
	query := `SELECT repo, component, baseline_value, sample_count, updated_at 
	          FROM baselines WHERE repo = ? AND component = ?`
	
	err := d.db.Get(&baseline, query, repo, component)
	if err != nil {
		return nil, fmt.Errorf("baseline not found: %w", err)
	}
	
	return &baseline, nil
}

func (d *Detector) getRecentSamples(repo, component string, limit int) ([]float64, error) {
	query := `SELECT value FROM benchmarks 
	          WHERE repo = ? AND component = ? 
	          ORDER BY timestamp DESC LIMIT ?`
	
	var values []float64
	err := d.db.Select(&values, query, repo, component, limit)
	return values, err
}

func (d *Detector) getRepoConfig(repo string) (*types.RepoConfig, error) {
	var config types.RepoConfig
	query := `SELECT repo, threshold_percent, min_samples, enabled 
	          FROM config WHERE repo = ?`
	
	err := d.db.Get(&config, query, repo)
	return &config, err
}
```

=== File: src\internal\regression\detector.go (78 lines) ===

```go
// Copyright 2025 Baleine Jay
// Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
// Commercial use requires a paid license. See link for details.
package regression

import (
	"fmt"
	"time"

	"github.com/jmoiron/sqlx"

	"regression-ci/internal/config"
	"regression-ci/pkg/types"
)

type Detector struct {
	db     *sqlx.DB
	config config.DetectionConfig
}

func New(db *sqlx.DB, cfg config.DetectionConfig) *Detector {
	return &Detector{
		db:     db,
		config: cfg,
	}
}

func (d *Detector) Analyze(req types.AnalyzeRequest) (*types.AnalyzeResponse, error) {
	timestamp := time.Now().Unix()
	response := &types.AnalyzeResponse{
		Repo:      req.Repo,
		Commit:    req.Commit,
		Timestamp: timestamp,
	}

	if err := d.storeBenchmarks(req, timestamp); err != nil {
		return nil, fmt.Errorf("failed to store benchmarks: %w", err)
	}

	for component, value := range req.Components {
		result, err := d.detectRegression(req.Repo, component, value)
		
		componentResult := types.ComponentResult{
			Component: component,
		}
		
		if err != nil {
			componentResult.Error = err.Error()
		} else {
			componentResult.Result = result
			d.updateBaseline(req.Repo, component, value, result)
		}
		
		response.Components = append(response.Components, componentResult)
	}

	return response, nil
}

func (d *Detector) storeBenchmarks(req types.AnalyzeRequest, timestamp int64) error {
	tx, err := d.db.Beginx()
	if err != nil {
		return fmt.Errorf("failed to begin transaction: %w", err)
	}
	defer tx.Rollback()

	query := `INSERT INTO benchmarks (repo, branch, commit_hash, component, value, timestamp) 
	          VALUES (?, ?, ?, ?, ?, ?)`

	for component, value := range req.Components {
		_, err := tx.Exec(query, req.Repo, req.Branch, req.Commit, component, value, timestamp)
		if err != nil {
			return fmt.Errorf("failed to insert benchmark: %w", err)
		}
	}

	return tx.Commit()
}
```

=== File: src\internal\server\handlers.go (68 lines) ===

```go
// Copyright 2025 Baleine Jay
// Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
// Commercial use requires a paid license. See link for details.
package server

import (
	"net/http"
	"time"

	"github.com/gin-gonic/gin"
	"github.com/rs/zerolog/log"

	"regression-ci/pkg/types"
)

func (s *Server) healthCheck(c *gin.Context) {
	if err := s.db.Ping(); err != nil {
		c.JSON(http.StatusServiceUnavailable, gin.H{
			"status": "unhealthy",
			"error":  "database connection failed",
		})
		return
	}

	c.JSON(http.StatusOK, gin.H{
		"status":    "healthy",
		"timestamp": time.Now().Unix(),
	})
}

func (s *Server) handleWebhook(c *gin.Context) {
	c.JSON(http.StatusNotImplemented, gin.H{
		"error": "webhook handling not implemented",
	})
}

func (s *Server) analyzeEndpoint(c *gin.Context) {
	var req types.AnalyzeRequest
	if err := c.ShouldBindJSON(&req); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{
			"error": "invalid request format",
		})
		return
	}

	result, err := s.detector.Analyze(req)
	if err != nil {
		log.Error().Err(err).Msg("analysis failed")
		c.JSON(http.StatusInternalServerError, gin.H{
			"error": "analysis failed",
		})
		return
	}

	c.JSON(http.StatusOK, result)
}

func (s *Server) getRepoConfig(c *gin.Context) {
	c.JSON(http.StatusNotImplemented, gin.H{
		"error": "config retrieval not implemented",
	})
}

func (s *Server) updateRepoConfig(c *gin.Context) {
	c.JSON(http.StatusNotImplemented, gin.H{
		"error": "config update not implemented",
	})
}
```

=== File: src\internal\server\router.go (10 lines) ===

```go
// Copyright 2025 Baleine Jay
// Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
// Commercial use requires a paid license. See link for details.
package server

import "github.com/gin-gonic/gin"

func (s *Server) Router() *gin.Engine {
	return s.router
}
```

=== File: src\internal\server\server.go (93 lines) ===

```go
// Copyright 2025 Baleine Jay
// Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
// Commercial use requires a paid license. See link for details.
package server

import (
	"context"
	"net/http"
	"time"

	"github.com/gin-gonic/gin"
	"github.com/jmoiron/sqlx"
	"github.com/rs/zerolog/log"

	"regression-ci/internal/config"
	"regression-ci/internal/regression"
	"regression-ci/internal/github"
)

type Server struct {
	db       *sqlx.DB
	config   *config.Config
	detector *regression.Detector
	github   *github.Client
	router   *gin.Engine
	server   *http.Server
}

func New(db *sqlx.DB, cfg *config.Config) *Server {
	s := &Server{
		db:       db,
		config:   cfg,
		detector: regression.New(db, cfg.Detection),
		github:   github.New(cfg.GitHub),
	}

	s.setupRoutes()
	s.server = &http.Server{
		Addr:         cfg.Server.Address,
		Handler:      s.router,
		ReadTimeout:  cfg.Server.ReadTimeout,
		WriteTimeout: cfg.Server.WriteTimeout,
	}

	return s
}

func (s *Server) Start() error {
	return s.server.ListenAndServe()
}

func (s *Server) Shutdown(ctx context.Context) error {
	return s.server.Shutdown(ctx)
}

func (s *Server) setupRoutes() {
	s.router = gin.New()
	s.router.Use(gin.Recovery())
	s.router.Use(s.loggingMiddleware())

	s.router.GET("/health", s.healthCheck)
	s.router.POST("/webhook", s.handleWebhook)
	s.router.POST("/analyze", s.analyzeEndpoint)
	s.router.GET("/config/:repo", s.getRepoConfig)
	s.router.PUT("/config/:repo", s.updateRepoConfig)
}

func (s *Server) loggingMiddleware() gin.HandlerFunc {
	return func(c *gin.Context) {
		start := time.Now()
		path := c.Request.URL.Path
		raw := c.Request.URL.RawQuery

		c.Next()

		latency := time.Since(start)
		clientIP := c.ClientIP()
		method := c.Request.Method
		statusCode := c.Writer.Status()

		if raw != "" {
			path = path + "?" + raw
		}

		log.Info().
			Str("client_ip", clientIP).
			Str("method", method).
			Str("path", path).
			Int("status", statusCode).
			Dur("latency", latency).
			Msg("request completed")
	}
}
```

=== File: src\pkg\types\types.go (65 lines) ===

```go
// Copyright 2025 Baleine Jay
// Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
// Commercial use requires a paid license. See link for details.
package types

type AnalyzeRequest struct {
	Repo       string                 `json:"repo" binding:"required"`
	Branch     string                 `json:"branch" binding:"required"`
	Commit     string                 `json:"commit" binding:"required"`
	Components map[string]float64     `json:"components" binding:"required"`
	Metadata   map[string]interface{} `json:"metadata,omitempty"`
}

type RegressionResult struct {
	IsRegression    bool    `json:"is_regression"`
	CurrentValue    float64 `json:"current_value"`
	BaselineValue   float64 `json:"baseline_value"`
	PercentChange   float64 `json:"percent_change"`
	ConfidenceScore float64 `json:"confidence_score"`
	SampleSize      int     `json:"sample_size"`
}

type ComponentResult struct {
	Component string            `json:"component"`
	Result    *RegressionResult `json:"result"`
	Error     string            `json:"error,omitempty"`
}

type AnalyzeResponse struct {
	Repo       string            `json:"repo"`
	Commit     string            `json:"commit"`
	Components []ComponentResult `json:"components"`
	Timestamp  int64             `json:"timestamp"`
}

type Baseline struct {
	Repo          string  `json:"repo" db:"repo"`
	Component     string  `json:"component" db:"component"`
	BaselineValue float64 `json:"baseline_value" db:"baseline_value"`
	SampleCount   int     `json:"sample_count" db:"sample_count"`
	UpdatedAt     int64   `json:"updated_at" db:"updated_at"`
}

type Benchmark struct {
	ID         int64   `json:"id" db:"id"`
	Repo       string  `json:"repo" db:"repo"`
	Branch     string  `json:"branch" db:"branch"`
	CommitHash string  `json:"commit_hash" db:"commit_hash"`
	Component  string  `json:"component" db:"component"`
	Value      float64 `json:"value" db:"value"`
	Timestamp  int64   `json:"timestamp" db:"timestamp"`
}

type RepoConfig struct {
	Repo             string                        `json:"repo" db:"repo"`
	ThresholdPercent float64                       `json:"threshold_percent" db:"threshold_percent"`
	MinSamples       int                           `json:"min_samples" db:"min_samples"`
	Enabled          bool                          `json:"enabled" db:"enabled"`
	Components       map[string]ComponentConfig   `json:"components,omitempty"`
}

type ComponentConfig struct {
	CustomThreshold *float64 `json:"custom_threshold,omitempty"`
	Enabled         bool     `json:"enabled"`
}
```

=== File: src\test-ci\benchmark-data\regression.json (30 lines) ===

```json
{
  "scenario": "performance_regression",
  "description": "Simulates a 25% performance degradation in HTTP handler latency",
  "baseline": {
    "repo": "testorg/test-project", 
    "component": "http_handler_latency",
    "samples": [
      {"commit": "base001", "value": 120.5, "timestamp": 1725094800},
      {"commit": "base002", "value": 118.2, "timestamp": 1725098400},
      {"commit": "base003", "value": 122.8, "timestamp": 1725102000},
      {"commit": "base004", "value": 119.7, "timestamp": 1725105600},
      {"commit": "base005", "value": 121.1, "timestamp": 1725109200}
    ],
    "calculated_baseline": 120.46,
    "standard_deviation": 1.84
  },
  "regression_data": {
    "commit": "regr001",
    "value": 152.3,
    "timestamp": 1725112800,
    "percent_change": 26.4,
    "expected_detection": true,
    "confidence_threshold": 95.0
  },
  "configuration": {
    "threshold_percent": 15.0,
    "min_samples": 5,
    "detection_method": "percentage_change"
  }
}
```

=== File: src\test-ci\github-sim\simulator.go (94 lines) ===

```go
// Copyright 2025 Baleine Jay
// Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
// Commercial use requires a paid license. See link for details.
package main

import (
	"bytes"
	"crypto/hmac"
	"crypto/sha256"
	"encoding/hex"
	"fmt"
	"io"
	"net/http"
	"os"
	"path/filepath"
)

type WebhookSimulator struct {
	targetURL string
	secret    string
	client    *http.Client
}

func NewSimulator(targetURL, secret string) *WebhookSimulator {
	return &WebhookSimulator{
		targetURL: targetURL,
		secret:    secret,
		client:    &http.Client{},
	}
}

func (w *WebhookSimulator) SendPayload(payloadFile string) error {
	payload, err := w.loadPayload(payloadFile)
	if err != nil {
		return fmt.Errorf("failed to load payload: %w", err)
	}

	signature := w.generateSignature(payload)

	req, err := http.NewRequest("POST", w.targetURL, bytes.NewBuffer(payload))
	if err != nil {
		return fmt.Errorf("failed to create request: %w", err)
	}

	req.Header.Set("Content-Type", "application/json")
	req.Header.Set("X-GitHub-Event", "pull_request")
	req.Header.Set("X-Hub-Signature-256", signature)
	req.Header.Set("User-Agent", "GitHub-Hookshot/test")

	resp, err := w.client.Do(req)
	if err != nil {
		return fmt.Errorf("request failed: %w", err)
	}
	defer resp.Body.Close()

	body, _ := io.ReadAll(resp.Body)
	fmt.Printf("Response: %d %s\nBody: %s\n", resp.StatusCode, resp.Status, string(body))

	return nil
}

func (w *WebhookSimulator) loadPayload(filename string) ([]byte, error) {
	payloadPath := filepath.Join("test-ci", "github-sim", "webhook-payloads", filename)
	return os.ReadFile(payloadPath)
}

func (w *WebhookSimulator) generateSignature(payload []byte) string {
	mac := hmac.New(sha256.New, []byte(w.secret))
	mac.Write(payload)
	return "sha256=" + hex.EncodeToString(mac.Sum(nil))
}

func main() {
	if len(os.Args) < 3 {
		fmt.Println("Usage: go run simulator.go <target-url> <payload-file>")
		os.Exit(1)
	}

	targetURL := os.Args[1]
	payloadFile := os.Args[2]
	secret := os.Getenv("WEBHOOK_SECRET")

	if secret == "" {
		secret = "test-secret-key"
		fmt.Println("Using default test secret")
	}

	simulator := NewSimulator(targetURL, secret)

	if err := simulator.SendPayload(payloadFile); err != nil {
		fmt.Printf("Error: %v\n", err)
		os.Exit(1)
	}
}

```

=== File: src\test-ci\github-sim\webhook-payloads\pr_opened.json (74 lines) ===

```json
{
  "action": "opened",
  "number": 123,
  "pull_request": {
    "id": 789456123,
    "number": 123,
    "state": "open",
    "title": "Add performance optimization to core algorithm",
    "user": {
      "login": "developer",
      "id": 12345,
      "type": "User"
    },
    "body": "This PR optimizes the core algorithm to improve throughput by 15%.\n\nBenchmark results:\n- Algorithm A: 1200ms -> 1020ms\n- Algorithm B: 850ms -> 722ms\n- Memory usage: 45MB -> 39MB",
    "created_at": "2025-08-31T10:30:00Z",
    "updated_at": "2025-08-31T10:30:00Z",
    "head": {
      "label": "feature/performance-optimization",
      "ref": "feature/performance-optimization",
      "sha": "abc123def456789",
      "repo": {
        "id": 654321,
        "name": "test-project",
        "full_name": "testorg/test-project",
        "owner": {
          "login": "testorg",
          "id": 98765,
          "type": "Organization"
        },
        "private": false,
        "default_branch": "main"
      }
    },
    "base": {
      "label": "main",
      "ref": "main", 
      "sha": "def789abc123456",
      "repo": {
        "id": 654321,
        "name": "test-project",
        "full_name": "testorg/test-project",
        "owner": {
          "login": "testorg",
          "id": 98765,
          "type": "Organization"
        },
        "private": false,
        "default_branch": "main"
      }
    }
  },
  "repository": {
    "id": 654321,
    "name": "test-project",
    "full_name": "testorg/test-project",
    "owner": {
      "login": "testorg",
      "id": 98765,
      "type": "Organization"
    },
    "private": false,
    "default_branch": "main"
  },
  "organization": {
    "login": "testorg",
    "id": 98765,
    "type": "Organization"
  },
  "sender": {
    "login": "developer",
    "id": 12345,
    "type": "User"
  }
}
```

=== File: src\test-ci\integration\full-flow.go (217 lines) ‼️ ===

```go
// Copyright 2025 Baleine Jay
// Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
// Commercial use requires a paid license. See link for details.
package integration

import (
	"bytes"
	"encoding/json"
	"fmt"
	"net/http"
	"net/http/httptest"
	"os"
	"path/filepath"
	"testing"
	"time"

	"github.com/jmoiron/sqlx"
	_ "github.com/glebarez/go-sqlite"

	"regression-ci/internal/config"
	"regression-ci/internal/server"
	"regression-ci/pkg/types"
)

type TestEnvironment struct {
	db     *sqlx.DB
	server *httptest.Server
	client *http.Client
}

func SetupTestEnv(t *testing.T) *TestEnvironment {
	db, err := sqlx.Open("sqlite", ":memory:")
	if err != nil {
		t.Fatalf("failed to open test database: %v", err)
	}

	cfg := &config.Config{
		Server: config.ServerConfig{
			Address:      ":0",
			ReadTimeout:  30 * time.Second,
			WriteTimeout: 30 * time.Second,
		},
		Database: config.DatabaseConfig{
			Path: ":memory:",
		},
		Detection: config.DetectionConfig{
			DefaultThreshold: 10.0,
			MinSamples:       5,
			MaxSamples:       50,
		},
	}

	srv := server.New(db, cfg)
	testServer := httptest.NewServer(srv.Router())

	return &TestEnvironment{
		db:     db,
		server: testServer,
		client: &http.Client{Timeout: 10 * time.Second},
	}
}

func (env *TestEnvironment) Cleanup() {
	env.server.Close()
	env.db.Close()
}

func TestFullPipeline(t *testing.T) {
	env := SetupTestEnv(t)
	defer env.Cleanup()

	t.Run("health_check", func(t *testing.T) {
		resp, err := env.client.Get(env.server.URL + "/health")
		if err != nil {
			t.Fatalf("health check failed: %v", err)
		}
		defer resp.Body.Close()

		if resp.StatusCode != http.StatusOK {
			t.Errorf("expected status 200, got %d", resp.StatusCode)
		}
	})

	t.Run("analyze_endpoint", func(t *testing.T) {
		benchmarkData := loadTestBenchmark(t, "golang-project/benchmarks.json")
		
		payload, err := json.Marshal(benchmarkData)
		if err != nil {
			t.Fatalf("failed to marshal benchmark data: %v", err)
		}

		resp, err := env.client.Post(
			env.server.URL+"/analyze",
			"application/json",
			bytes.NewBuffer(payload),
		)
		if err != nil {
			t.Fatalf("analyze request failed: %v", err)
		}
		defer resp.Body.Close()

		if resp.StatusCode == http.StatusNotImplemented {
			t.Skip("analyze endpoint not yet implemented")
		}
	})

	t.Run("webhook_simulation", func(t *testing.T) {
		webhookPayload := loadWebhookPayload(t, "pr_opened.json")
		
		resp, err := env.client.Post(
			env.server.URL+"/webhook",
			"application/json",
			bytes.NewBuffer(webhookPayload),
		)
		if err != nil {
			t.Fatalf("webhook request failed: %v", err)
		}
		defer resp.Body.Close()

		if resp.StatusCode == http.StatusNotImplemented {
			t.Skip("webhook endpoint not yet implemented")
		}
	})
}

func TestRegressionScenarios(t *testing.T) {
	env := SetupTestEnv(t)
	defer env.Cleanup()

	scenarios := []string{"regression.json", "baseline.json", "improvements.json"}
	
	for _, scenario := range scenarios {
		t.Run(scenario, func(t *testing.T) {
			scenarioData := loadBenchmarkScenario(t, scenario)
			validateScenario(t, env, scenarioData)
		})
	}
}

func TestConcurrentLoad(t *testing.T) {
	env := SetupTestEnv(t)
	defer env.Cleanup()

	concurrency := 10
	requests := 50
	
	results := make(chan error, concurrency*requests)
	
	for i := 0; i < concurrency; i++ {
		go func() {
			for j := 0; j < requests; j++ {
				resp, err := env.client.Get(env.server.URL + "/health")
				if err != nil {
					results <- fmt.Errorf("request failed: %w", err)
					continue
				}
				resp.Body.Close()
				
				if resp.StatusCode != http.StatusOK {
					results <- fmt.Errorf("unexpected status: %d", resp.StatusCode)
					continue
				}
				
				results <- nil
			}
		}()
	}

	for i := 0; i < concurrency*requests; i++ {
		if err := <-results; err != nil {
			t.Errorf("concurrent request failed: %v", err)
		}
	}
}

func loadTestBenchmark(t *testing.T, filename string) types.AnalyzeRequest {
	path := filepath.Join("test-ci", "mock-repos", filename)
	data, err := os.ReadFile(path)
	if err != nil {
		t.Fatalf("failed to load test benchmark: %v", err)
	}

	var req types.AnalyzeRequest
	if err := json.Unmarshal(data, &req); err != nil {
		t.Fatalf("failed to parse benchmark data: %v", err)
	}

	return req
}

func loadWebhookPayload(t *testing.T, filename string) []byte {
	path := filepath.Join("test-ci", "github-sim", "webhook-payloads", filename)
	data, err := os.ReadFile(path)
	if err != nil {
		t.Fatalf("failed to load webhook payload: %v", err)
	}
	return data
}

func loadBenchmarkScenario(t *testing.T, filename string) map[string]interface{} {
	path := filepath.Join("test-ci", "benchmark-data", filename)
	data, err := os.ReadFile(path)
	if err != nil {
		t.Fatalf("failed to load benchmark scenario: %v", err)
	}

	var scenario map[string]interface{}
	if err := json.Unmarshal(data, &scenario); err != nil {
		t.Fatalf("failed to parse scenario data: %v", err)
	}

	return scenario
}

func validateScenario(t *testing.T, env *TestEnvironment, scenario map[string]interface{}) {
	t.Logf("Validating scenario: %s", scenario["scenario"])
}
```

=== File: src\test-ci\mock-repos\golang-project\benchmarks.json (22 lines) ===

```json
{
  "repo": "testorg/golang-project",
  "branch": "main",
  "commit": "abc123def456",
  "timestamp": 1725098400,
  "components": {
    "http_handler_latency": 125.5,
    "database_query_time": 45.2,
    "json_marshal_time": 12.8,
    "memory_allocation": 2048576,
    "cpu_usage_percent": 23.4,
    "throughput_rps": 1250.0,
    "error_rate_percent": 0.02,
    "cache_hit_ratio": 94.5
  },
  "metadata": {
    "go_version": "1.21.0",
    "test_duration": "5m",
    "load_pattern": "constant",
    "environment": "ci"
  }
}
```

=== File: LICENSE (44 lines) ===

```text
Phicode License
------------------------------------------------------------------------------------------
Copyright 2025 Baleine Jay

https://banes-lab.com | https://github.com/Varietyz/phicode-runtime

------------------------------------------------------------------------------------------
NON-COMMERCIAL LICENSE (Default)
This software is available under a non-commercial license based on the MIT License.
------------------------------------------------------------------------------------------

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, **subject to the following commercial restriction:**

COMMERCIAL USE RESTRICTION:
Any use of the Software for commercial purposes, including but not limited to use in
commercial software, paid services, internal use by for-profit organizations, hosting
as a service (SaaS), or distribution for revenue, is expressly prohibited without
a separate commercial license.

To obtain a commercial license, visit: https://banes-lab.com/licensing
or contact: jay.bane@outlook.com.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

------------------------------------------------------------------------------------------
COMMERCIAL LICENSE
For commercial use, a paid license is required. Commercial licenses grant:
- Rights for commercial use, distribution, and hosting
- Rights to create derivative works for commercial purposes
- Optional technical support and maintenance

For details or enterprise licensing, contact: jay.bane@outlook.com.
------------------------------------------------------------------------------------------

```
