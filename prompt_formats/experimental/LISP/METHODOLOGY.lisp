(methodology
    (license "Disciplined AI Software Development Methodology © 2025 by Jay Baleine is licensed under CC BY-SA 4.0")
    (license-url "https://creativecommons.org/licenses/by-sa/4.0/")
    (attribution-requirements
        "When sharing content publicly (repositories, documentation, articles): Include the full attribution above"
        "When working with AI systems (ChatGPT, Claude, etc.): Attribution not required during collaboration sessions"
        "When distributing or modifying the methodology: Full CC BY-SA 4.0 compliance required")
    
    (title "Project Documentation Methodology")
    
    (core-architectural-principles
        (foundational-philosophy
            (principle "Architectural Minimalism with Deterministic Reliability: Every line of code must earn its place through measurable value. Build systems that work predictably in production, not demonstrations of sophistication."))
        
        (code-architecture-principles
            (separation-of-concerns
                (rule "Each module has single, well-defined responsibility")
                (rule "Strict modular boundaries with clear interfaces")
                (rule "Recognize when separation would harm rather than help architecture")
                (rule "Centralized main entry points with modular project layout"))
            
            (deterministic-operations
                (rule "Synchronous, predictable behavior over async complexity")
                (rule "Long-runtime stability over cutting-edge patterns")
                (rule "Production stability over development convenience")
                (rule "Cross-platform considerations in design decisions"))
            
            (performance-driven-decisions
                (rule "Choose based on workload requirements, not popular trends")
                (rule "Apply optimizations only to proven bottlenecks with measurable impact")
                (rule "Avoid premature optimization that clutters codebase")
                (rule "Maintain performance baselines and regression detection"))
            
            (code-quality-standards
                (rule "Files never exceed 150 lines (split into separate modules if needed)")
                (rule "Self-explanatory code without comments")
                (rule "Preserve readability and maintainability as primary concerns")
                (rule "KISS and DRY principles expertly applied")
                (rule "Reuse existing functions before creating new ones"))
            
            (error-handling-philosophy
                (rule "Robust without over-engineering")
                (rule "Implement what's necessary for production reliability")
                (rule "Avoid handling every possible edge case")
                (rule "Graceful failure modes and resource cleanup"))
            
            (feature-control
                (rule "Resist feature bloat and complexity creep")
                (rule "Every addition must serve core project purpose")
                (rule "Surgical approach: target exact problem with minimal code")
                (rule "Multi-language use only when justified by measurable gains"))
            
            (web-development-adaptations
                (rule "No inlining: Styles to separate files, handlers to named functions, configurations as constants")
                (rule "File size accommodation: Components ≤250 lines (DOM complexity), modules ≤150 lines")
                (rule "Async operations: API calls, user interactions, data fetching only")
                (rule "Error boundaries: Network operations, user inputs, third-party integrations")
                (rule "File colocation: Component.jsx, Component.module.css, Component.test.js")
                (rule "Component splitting: Multiple purposes or testing difficulty")
                (rule "Implementation protocol: Request architectural compliance clarification for code generation tasks"))))
    
    (phase0-requirements
        (title "Basic Must-Haves (Phase 0 - Always First)")
        (description "Every project, regardless of size, must establish these foundational systems before any feature development")
        
        (benchmarking-suite
            (requirement "Core Framework: Performance measurement with component isolation")
            (requirement "Regression Detection: Compare against previous results, fail on performance drops")
            (requirement "Baseline Management: Save and track performance baselines over time")
            (requirement "JSON Output: Structured data for automated analysis and CI integration")
            (requirement "Timeline Tracking: Historical performance data across project evolution"))
        
        (cicd-infrastructure
            (requirement "Release Workflows: Automated versioning, building, and deployment")
            (requirement "Regression Detection: Benchmark comparison on every commit/PR")
            (requirement "Quality Gates: Block merges that fail performance or quality thresholds")
            (requirement "Automated Testing: Run full test suite on code changes"))
        
        (core-architecture
            (requirement "Centralized Entry Points: Single main module that orchestrates everything")
            (requirement "Configuration Management: Externalized settings with validation")
            (requirement "Centralized Logging: Error handling and diagnostic output with JSON integration")
            (requirement "Dependency Injection: Clean separation and testable components"))
        
        (testing-infrastructure
            (requirement "Test Suite: Unit and integration tests for all components")
            (requirement "Stress Testing: Load and boundary condition validation")
            (requirement "Test Data Management: Reproducible test scenarios and cleanup")
            (requirement "Coverage Tracking: Ensure adequate test coverage before releases"))
        
        (documentation-system
            (requirement "Automated Generation: Extract documentation from code and structure")
            (requirement "Architecture Documentation: System design and component relationships")
            (requirement "API Documentation: Interface specifications and usage examples")
            (requirement "Performance Documentation: Benchmark results and optimization guides"))
        
        (critical-note "These systems must be operational before writing any application logic. They become the foundation that enables rapid, confident development."))
    
    (documentation-building-process
        (step1
            (name "Project Decomposition")
            (questions
                (question "What does \"finished\" look like?")
                (question "What are the major pieces that need to exist?")
                (question "What depends on what?")
                (question "Where are the natural stopping points?"))
            (approach "Create sections based on dependencies: Major Piece A → Major Piece B → Major Piece C with corresponding sub-tasks"))
        
        (step2
            (name "Phase Creation")
            (mandatory-phase0
                (item "Benchmarking suite with regression detection")
                (item "GitHub workflows for releases and quality gates")
                (item "Test infrastructure (unit + stress testing)")
                (item "Documentation generation system")
                (item "Centralized architecture setup"))
            (grouping-criteria
                (criterion "Dependency chains: Things that must happen in sequence")
                (criterion "Logical groupings: Related functionality that makes sense together")
                (criterion "Natural checkpoints: Places where you can validate progress")))
        
        (step3
            (name "Task Breakdown")
            (requirements
                (requirement "Specific action: What exactly needs to be done")
                (requirement "Output: What will exist when complete")
                (requirement "Success criteria: How to verify completion")
                (requirement "Integration points: How it connects to other work")))
        
        (step4
            (name "Progress Tracking System")
            (status-indicators
                (indicator (status "COMPLETED") "Done and validated")
                (indicator (status "BLOCKED") "Cannot proceed due to dependency")
                (indicator (status "READY") "Dependencies met, can start")
                (indicator (status "UNCERTAIN") "Need clarification or decision")))
        
        (step5
            (name "Quality Gates")
            (criteria
                (criterion "Does the output match what was specified?")
                (criterion "Can the next phase actually use this output?")
                (criterion "Is there enough documentation for future reference?")
                (criterion "Are there any obvious issues that need fixing?"))))
    
    (systematic-enforcement-framework
        (mandatory-checkpoints
            (architectural-compliance
                (checkpoint "SoC VALIDATION: Each module single responsibility, clear boundaries")
                (checkpoint "DETERMINISTIC BEHAVIOR: Synchronous operations, predictable outcomes")
                (checkpoint "FILE SIZE COMPLIANCE: All files ≤150 lines or properly modularized")
                (checkpoint "DRY ENFORCEMENT: No duplicate code, existing functions reused")
                (checkpoint "KISS VALIDATION: Minimal complexity, surgical implementations")
                (checkpoint "CONFIG CENTRALIZATION: No hardcoded values outside constants")
                (checkpoint "PERFORMANCE INTEGRATION: Benchmarks operational, gates passing")
                (checkpoint "PRODUCTION READINESS: Error handling, resource cleanup, cross-platform"))
            
            (code-quality-gates
                (gate "Self-explanatory naming, no comments needed")
                (gate "Performance characteristics match workload requirements")
                (gate "Every addition serves core project purpose")
                (gate "Regression detection prevents performance degradation")
                (gate "Resource utilization within defined thresholds"))
            
            (progression-blocker "Any failed checkpoint blocks phase advancement"))
        
        (mid-phase-validation
            (during-development
                (validation "INCREMENTAL COMPLIANCE: Check after each significant change")
                (validation "BENCHMARK INTEGRATION: New components measured immediately")
                (validation "DEPENDENCY ALIGNMENT: Imports match architectural boundaries")
                (validation "EDGE CASE HANDLING: Document but don't implement without plan")
                (validation "FEATURE CREEP CHECK: Question necessity of each addition"))
            
            (before-phase-completion
                (validation "FULL ARCHITECTURE AUDIT: All principles systematically verified")
                (validation "PERFORMANCE REGRESSION: Compare against established baselines")
                (validation "INTEGRATION VALIDATION: Components work within system boundaries")
                (validation "PRODUCTION SIMULATION: Test under realistic deployment constraints")))
        
        (enforcement-automation
            (validate-phase-script
                (function "Check file sizes (fail if >150 lines)")
                (function "Scan for hardcoded values outside config")
                (function "Validate import dependencies match architecture")
                (function "Run benchmark suite and check gates")
                (function "Generate compliance report"))
            
            (dry-audit-script
                (function "Detect duplicate function implementations")
                (function "Find unused imports and functions")
                (function "Identify constants that should be centralized")
                (function "Flag potential separation of concerns violations"))
            
            (cicd-workflow-integration
                (function "Run validation on every commit")
                (function "Block merges that fail compliance checks")
                (function "Generate performance regression reports")
                (function "Maintain baseline measurements over time"))))
    
    (principle-integration
        (implementation-enforcement
            (file-and-module-constraints
                (constraint "Each file ≤ 150 lines or properly split")
                (constraint "Module serves single, clear purpose")
                (constraint "No redundant code between modules")
                (constraint "Existing functions reused before creating new ones")
                (constraint "Naming conventions consistent across codebase"))
            
            (architecture-validation
                (constraint "Centralized configuration used throughout")
                (constraint "Constants referenced, no magic numbers")
                (constraint "Modular separation maintained with clear boundaries")
                (constraint "Dependencies align with separation of concerns")
                (constraint "Synchronous operations preferred over async complexity"))
            
            (performance-integration
                (constraint "Benchmarking suite integrated with all modules")
                (constraint "Regression detection operational")
                (constraint "JSON output for automated analysis")
                (constraint "Performance gates defined and enforced")
                (constraint "Timeline tracking for historical comparison"))
            
            (production-readiness
                (constraint "Cross-platform deployment considerations")
                (constraint "Real-world constraints addressed")
                (constraint "Resource cleanup on shutdown")
                (constraint "Deterministic behavior under load")
                (constraint "Error handling appropriate for production")))
        
        (scaling-adaptation-guidelines
            (single-file-scripts
                (guideline "Apply SoC within functions (input, processing, output)")
                (guideline "Benchmark core operation even if simple")
                (guideline "Validate against 150-line limit")
                (guideline "Self-explanatory function and variable names"))
            
            (small-applications
                (guideline "Strict modular boundaries with clear interfaces")
                (guideline "Centralized configuration and constants")
                (guideline "Synchronous operations with predictable flow")
                (guideline "Performance baseline establishment"))
            
            (production-systems
                (guideline "Full architectural compliance with all principles")
                (guideline "Comprehensive benchmarking and regression detection")
                (guideline "Cross-platform deployment considerations")
                (guideline "Production-grade error handling and resource management"))
            
            (multi-language-projects
                (guideline "Each language justified by measurable performance gains")
                (guideline "Maintain architectural principles across language boundaries")
                (guideline "Unified benchmarking system for all components")
                (guideline "Consistent error handling patterns across languages")))
        
        (domain-specific-adaptations
            (web-development-projects
                (adaptation "No Inlining: Styles to separate files, handlers to named functions, configs as constants")
                (adaptation "File Size Exemption: Components ≤250 lines (DOM complexity), modules ≤150 lines")
                (adaptation "Async Permitted: API calls, user interactions, data fetching only")
                (adaptation "Error Boundaries: Network ops, user inputs, third-party integrations")
                (adaptation "File Colocation: Component.jsx, Component.module.css, Component.test.js")
                (adaptation "Component Splitting: Multiple purposes or testing difficulty"))))
    
    (success-metrics
        (technical-indicators
            (indicator "All architectural principles consistently applied across codebase")
            (indicator "Performance baselines maintained throughout development lifecycle")
            (indicator "Zero production incidents related to architectural violations")
            (indicator "File size constraints adhered to without compromising functionality"))
        
        (operational-indicators
            (indicator "System uptime and reliability under production load")
            (indicator "Predictable resource utilization patterns")
            (indicator "Graceful degradation under stress conditions")
            (indicator "Maintainability preserved as codebase grows"))
        
        (development-indicators
            (indicator "Enforcement checkpoints prevent architectural drift")
            (indicator "Performance regression detection catches optimizations and degradations")
            (indicator "Code review efficiency improved through systematic validation")
            (indicator "Technical debt accumulation prevented through continuous compliance"))
        
        (documentation-quality
            (indicator "Enforcement checkpoints prevent architectural drift")
            (indicator "Quality gates block progression with incomplete work")
            (indicator "Automated validation catches compliance violations")
            (indicator "Performance baselines maintained throughout development"))
        
        (project-execution
            (indicator "Systematic validation prevents technical debt accumulation")
            (indicator "Architectural principles consistently applied across codebase")
            (indicator "Performance characteristics predictable and measurable")
            (indicator "Production readiness verified at each phase")))
    
    (conclusion "This methodology enforces discipline through automated checking and explicit validation points, preventing the gradual erosion of architectural principles during development."))