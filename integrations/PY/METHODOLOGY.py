from dataclasses import dataclass
from typing import List, Dict

@dataclass
class FoundationalPhilosophy:
    architectural_minimalism: str = "Every line of code must earn its place through measurable value. Build systems that work predictably in production, not demonstrations of sophistication."

@dataclass
class SeparationOfConcerns:
    single_responsibility: bool = True
    strict_modular_boundaries: bool = True
    recognize_harmful_separation: bool = True
    centralized_main_entry: bool = True

@dataclass
class DeterministicOperations:
    synchronous_over_async: bool = True
    stability_over_patterns: bool = True
    production_over_convenience: bool = True
    cross_platform_considerations: bool = True

@dataclass
class PerformanceDrivenDecisions:
    workload_over_trends: bool = True
    optimize_proven_bottlenecks_only: bool = True
    avoid_premature_optimization: bool = True
    maintain_baselines_regression_detection: bool = True

@dataclass
class CodeQualityStandards:
    max_file_lines: int = 150
    self_explanatory_code: bool = True
    readability_maintainability_priority: bool = True
    kiss_dry_principles: bool = True
    reuse_existing_functions: bool = True

@dataclass
class ErrorHandlingPhilosophy:
    robust_not_overengineered: bool = True
    production_reliability_focus: bool = True
    avoid_handling_all_edge_cases: bool = True
    graceful_failure_resource_cleanup: bool = True

@dataclass
class FeatureControl:
    resist_bloat_complexity_creep: bool = True
    additions_serve_core_purpose: bool = True
    surgical_approach_minimal_code: bool = True
    multilanguage_justified_by_gains: bool = True

@dataclass
class WebDevelopmentAdaptations:
    no_inlining: bool = True
    component_max_lines: int = 250
    module_max_lines: int = 150
    async_operations_permitted: List[str] = None
    error_boundaries_required: List[str] = None
    file_colocation_pattern: str = "Component.jsx, Component.module.css, Component.test.js"
    component_splitting_criteria: List[str] = None
    implementation_protocol: str = "Request architectural compliance clarification for code generation tasks"
    
    def __post_init__(self):
        if self.async_operations_permitted is None:
            self.async_operations_permitted = ["API calls", "user interactions", "data fetching"]
        if self.error_boundaries_required is None:
            self.error_boundaries_required = ["network operations", "user inputs", "third-party integrations"]
        if self.component_splitting_criteria is None:
            self.component_splitting_criteria = ["multiple purposes", "testing difficulty"]

@dataclass
class CodeArchitecturePrinciples:
    separation_of_concerns: SeparationOfConcerns
    deterministic_operations: DeterministicOperations
    performance_driven_decisions: PerformanceDrivenDecisions
    code_quality_standards: CodeQualityStandards
    error_handling_philosophy: ErrorHandlingPhilosophy
    feature_control: FeatureControl
    web_development_adaptations: WebDevelopmentAdaptations

@dataclass
class BenchmarkingSuite:
    requirements: List[str] = None
    
    def __post_init__(self):
        if self.requirements is None:
            self.requirements = [
                "Core Framework: Performance measurement with component isolation",
                "Regression Detection: Compare against previous results, fail on performance drops",
                "Baseline Management: Save and track performance baselines over time",
                "JSON Output: Structured data for automated analysis and CI integration",
                "Timeline Tracking: Historical performance data across project evolution"
            ]

@dataclass
class CICDInfrastructure:
    requirements: List[str] = None
    
    def __post_init__(self):
        if self.requirements is None:
            self.requirements = [
                "Release Workflows: Automated versioning, building, and deployment",
                "Regression Detection: Benchmark comparison on every commit/PR",
                "Quality Gates: Block merges that fail performance or quality thresholds",
                "Automated Testing: Run full test suite on code changes"
            ]

@dataclass
class CoreArchitecture:
    requirements: List[str] = None
    
    def __post_init__(self):
        if self.requirements is None:
            self.requirements = [
                "Centralized Entry Points: Single main module that orchestrates everything",
                "Configuration Management: Externalized settings with validation",
                "Centralized Logging: Error handling and diagnostic output with JSON integration",
                "Dependency Injection: Clean separation and testable components"
            ]

@dataclass
class TestingInfrastructure:
    requirements: List[str] = None
    
    def __post_init__(self):
        if self.requirements is None:
            self.requirements = [
                "Test Suite: Unit and integration tests for all components",
                "Stress Testing: Load and boundary condition validation",
                "Test Data Management: Reproducible test scenarios and cleanup",
                "Coverage Tracking: Ensure adequate test coverage before releases"
            ]

@dataclass
class DocumentationSystem:
    requirements: List[str] = None
    
    def __post_init__(self):
        if self.requirements is None:
            self.requirements = [
                "Automated Generation: Extract documentation from code and structure",
                "Architecture Documentation: System design and component relationships",
                "API Documentation: Interface specifications and usage examples",
                "Performance Documentation: Benchmark results and optimization guides"
            ]

@dataclass
class Phase0Requirements:
    title: str = "Basic Must-Haves (Phase 0 - Always First)"
    description: str = "Every project, regardless of size, must establish these foundational systems before any feature development"
    benchmarking_suite: BenchmarkingSuite
    cicd_infrastructure: CICDInfrastructure
    core_architecture: CoreArchitecture
    testing_infrastructure: TestingInfrastructure
    documentation_system: DocumentationSystem
    critical_note: str = "These systems must be operational before writing any application logic. They become the foundation that enables rapid, confident development."

@dataclass
class DocumentationStep:
    name: str
    questions: List[str] = None
    approach: str = ""
    mandatory_phase0: List[str] = None
    grouping_criteria: List[str] = None
    requirements: List[str] = None
    status_indicators: Dict[str, str] = None
    criteria: List[str] = None

@dataclass
class DocumentationBuildingProcess:
    step1_project_decomposition: DocumentationStep
    step2_phase_creation: DocumentationStep
    step3_task_breakdown: DocumentationStep
    step4_progress_tracking: DocumentationStep
    step5_quality_gates: DocumentationStep

@dataclass
class ArchitecturalCompliance:
    checkpoints: List[str] = None
    
    def __post_init__(self):
        if self.checkpoints is None:
            self.checkpoints = [
                "SoC VALIDATION: Each module single responsibility, clear boundaries",
                "DETERMINISTIC BEHAVIOR: Synchronous operations, predictable outcomes",
                "FILE SIZE COMPLIANCE: All files ≤150 lines or properly modularized",
                "DRY ENFORCEMENT: No duplicate code, existing functions reused",
                "KISS VALIDATION: Minimal complexity, surgical implementations",
                "CONFIG CENTRALIZATION: No hardcoded values outside constants",
                "PERFORMANCE INTEGRATION: Benchmarks operational, gates passing",
                "PRODUCTION READINESS: Error handling, resource cleanup, cross-platform"
            ]

@dataclass
class CodeQualityGates:
    gates: List[str] = None
    progression_blocker: str = "Any failed checkpoint blocks phase advancement"
    
    def __post_init__(self):
        if self.gates is None:
            self.gates = [
                "Self-explanatory naming, no comments needed",
                "Performance characteristics match workload requirements",
                "Every addition serves core project purpose",
                "Regression detection prevents performance degradation",
                "Resource utilization within defined thresholds"
            ]

@dataclass
class MidPhaseValidation:
    during_development: List[str] = None
    before_phase_completion: List[str] = None
    
    def __post_init__(self):
        if self.during_development is None:
            self.during_development = [
                "INCREMENTAL COMPLIANCE: Check after each significant change",
                "BENCHMARK INTEGRATION: New components measured immediately",
                "DEPENDENCY ALIGNMENT: Imports match architectural boundaries",
                "EDGE CASE HANDLING: Document but don't implement without plan",
                "FEATURE CREEP CHECK: Question necessity of each addition"
            ]
        if self.before_phase_completion is None:
            self.before_phase_completion = [
                "FULL ARCHITECTURE AUDIT: All principles systematically verified",
                "PERFORMANCE REGRESSION: Compare against established baselines",
                "INTEGRATION VALIDATION: Components work within system boundaries",
                "PRODUCTION SIMULATION: Test under realistic deployment constraints"
            ]

@dataclass
class EnforcementAutomation:
    validate_phase_script: List[str] = None
    dry_audit_script: List[str] = None
    cicd_workflow_integration: List[str] = None
    
    def __post_init__(self):
        if self.validate_phase_script is None:
            self.validate_phase_script = [
                "Check file sizes (fail if >150 lines)",
                "Scan for hardcoded values outside config",
                "Validate import dependencies match architecture",
                "Run benchmark suite and check gates",
                "Generate compliance report"
            ]
        if self.dry_audit_script is None:
            self.dry_audit_script = [
                "Detect duplicate function implementations",
                "Find unused imports and functions",
                "Identify constants that should be centralized",
                "Flag potential separation of concerns violations"
            ]
        if self.cicd_workflow_integration is None:
            self.cicd_workflow_integration = [
                "Run validation on every commit",
                "Block merges that fail compliance checks",
                "Generate performance regression reports",
                "Maintain baseline measurements over time"
            ]

@dataclass
class SystematicEnforcementFramework:
    architectural_compliance: ArchitecturalCompliance
    code_quality_gates: CodeQualityGates
    mid_phase_validation: MidPhaseValidation
    enforcement_automation: EnforcementAutomation

@dataclass
class ConstraintGroup:
    constraints: List[str]

@dataclass
class ScalingGuideline:
    guidelines: List[str]

@dataclass
class PrincipleIntegration:
    file_module_constraints: ConstraintGroup
    architecture_validation: ConstraintGroup
    performance_integration: ConstraintGroup
    production_readiness: ConstraintGroup
    single_file_scripts: ScalingGuideline
    small_applications: ScalingGuideline
    production_systems: ScalingGuideline
    multilanguage_projects: ScalingGuideline
    web_development_projects: ScalingGuideline

@dataclass
class SuccessMetrics:
    technical_indicators: List[str] = None
    operational_indicators: List[str] = None
    development_indicators: List[str] = None
    documentation_quality: List[str] = None
    project_execution: List[str] = None
    
    def __post_init__(self):
        if self.technical_indicators is None:
            self.technical_indicators = [
                "All architectural principles consistently applied across codebase",
                "Performance baselines maintained throughout development lifecycle",
                "Zero production incidents related to architectural violations",
                "File size constraints adhered to without compromising functionality"
            ]
        if self.operational_indicators is None:
            self.operational_indicators = [
                "System uptime and reliability under production load",
                "Predictable resource utilization patterns",
                "Graceful degradation under stress conditions",
                "Maintainability preserved as codebase grows"
            ]
        if self.development_indicators is None:
            self.development_indicators = [
                "Enforcement checkpoints prevent architectural drift",
                "Performance regression detection catches optimizations and degradations",
                "Code review efficiency improved through systematic validation",
                "Technical debt accumulation prevented through continuous compliance"
            ]
        if self.documentation_quality is None:
            self.documentation_quality = [
                "Enforcement checkpoints prevent architectural drift",
                "Quality gates block progression with incomplete work",
                "Automated validation catches compliance violations",
                "Performance baselines maintained throughout development"
            ]
        if self.project_execution is None:
            self.project_execution = [
                "Systematic validation prevents technical debt accumulation",
                "Architectural principles consistently applied across codebase",
                "Performance characteristics predictable and measurable",
                "Production readiness verified at each phase"
            ]

@dataclass
class ProjectDocumentationMethodology:
    title: str = "Project Documentation Methodology"
    foundational_philosophy: FoundationalPhilosophy
    code_architecture_principles: CodeArchitecturePrinciples
    phase0_requirements: Phase0Requirements
    documentation_building_process: DocumentationBuildingProcess
    systematic_enforcement_framework: SystematicEnforcementFramework
    principle_integration: PrincipleIntegration
    success_metrics: SuccessMetrics
    conclusion: str = "This methodology enforces discipline through automated checking and explicit validation points, preventing the gradual erosion of architectural principles during development."
    license: str = "CC BY-SA 4.0"

def create_methodology_dict():
    return {
        "title": "Project Documentation Methodology",
        "foundational_philosophy": {
            "architectural_minimalism": "Every line of code must earn its place through measurable value. Build systems that work predictably in production, not demonstrations of sophistication."
        },
        "code_architecture_principles": {
            "separation_of_concerns": {
                "single_responsibility": True,
                "strict_modular_boundaries": True,
                "recognize_harmful_separation": True,
                "centralized_main_entry": True
            },
            "deterministic_operations": {
                "synchronous_over_async": True,
                "stability_over_patterns": True,
                "production_over_convenience": True,
                "cross_platform_considerations": True
            },
            "performance_driven_decisions": {
                "workload_over_trends": True,
                "optimize_proven_bottlenecks_only": True,
                "avoid_premature_optimization": True,
                "maintain_baselines_regression_detection": True
            },
            "code_quality_standards": {
                "max_file_lines": 150,
                "self_explanatory_code": True,
                "readability_maintainability_priority": True,
                "kiss_dry_principles": True,
                "reuse_existing_functions": True
            },
            "error_handling_philosophy": {
                "robust_not_overengineered": True,
                "production_reliability_focus": True,
                "avoid_handling_all_edge_cases": True,
                "graceful_failure_resource_cleanup": True
            },
            "feature_control": {
                "resist_bloat_complexity_creep": True,
                "additions_serve_core_purpose": True,
                "surgical_approach_minimal_code": True,
                "multilanguage_justified_by_gains": True
            },
            "web_development_adaptations": {
                "no_inlining": True,
                "component_max_lines": 250,
                "module_max_lines": 150,
                "async_operations_permitted": ["API calls", "user interactions", "data fetching"],
                "error_boundaries_required": ["network operations", "user inputs", "third-party integrations"],
                "file_colocation_pattern": "Component.jsx, Component.module.css, Component.test.js",
                "component_splitting_criteria": ["multiple purposes", "testing difficulty"],
                "implementation_protocol": "Request architectural compliance clarification for code generation tasks"
            }
        },
        "phase0_requirements": {
            "title": "Basic Must-Haves (Phase 0 - Always First)",
            "description": "Every project, regardless of size, must establish these foundational systems before any feature development",
            "benchmarking_suite": [
                "Core Framework: Performance measurement with component isolation",
                "Regression Detection: Compare against previous results, fail on performance drops",
                "Baseline Management: Save and track performance baselines over time",
                "JSON Output: Structured data for automated analysis and CI integration",
                "Timeline Tracking: Historical performance data across project evolution"
            ],
            "cicd_infrastructure": [
                "Release Workflows: Automated versioning, building, and deployment",
                "Regression Detection: Benchmark comparison on every commit/PR",
                "Quality Gates: Block merges that fail performance or quality thresholds",
                "Automated Testing: Run full test suite on code changes"
            ],
            "core_architecture": [
                "Centralized Entry Points: Single main module that orchestrates everything",
                "Configuration Management: Externalized settings with validation",
                "Centralized Logging: Error handling and diagnostic output with JSON integration",
                "Dependency Injection: Clean separation and testable components"
            ],
            "testing_infrastructure": [
                "Test Suite: Unit and integration tests for all components",
                "Stress Testing: Load and boundary condition validation",
                "Test Data Management: Reproducible test scenarios and cleanup",
                "Coverage Tracking: Ensure adequate test coverage before releases"
            ],
            "documentation_system": [
                "Automated Generation: Extract documentation from code and structure",
                "Architecture Documentation: System design and component relationships",
                "API Documentation: Interface specifications and usage examples",
                "Performance Documentation: Benchmark results and optimization guides"
            ],
            "critical_note": "These systems must be operational before writing any application logic. They become the foundation that enables rapid, confident development."
        },
        "success_metrics": {
            "technical_indicators": [
                "All architectural principles consistently applied across codebase",
                "Performance baselines maintained throughout development lifecycle",
                "Zero production incidents related to architectural violations",
                "File size constraints adhered to without compromising functionality"
            ],
            "operational_indicators": [
                "System uptime and reliability under production load",
                "Predictable resource utilization patterns",
                "Graceful degradation under stress conditions",
                "Maintainability preserved as codebase grows"
            ],
            "development_indicators": [
                "Enforcement checkpoints prevent architectural drift",
                "Performance regression detection catches optimizations and degradations",
                "Code review efficiency improved through systematic validation",
                "Technical debt accumulation prevented through continuous compliance"
            ]
        },
        "conclusion": "This methodology enforces discipline through automated checking and explicit validation points, preventing the gradual erosion of architectural principles during development.",
        "license": "CC BY-SA 4.0"
    }