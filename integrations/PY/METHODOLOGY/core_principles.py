# Disciplined AI Software Development Methodology © 2025 by Jay Baleine is licensed under CC BY-SA 4.0 
# https://creativecommons.org/licenses/by-sa/4.0/
from dataclasses import dataclass

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
class CodeArchitecturePrinciples:
    separation_of_concerns: SeparationOfConcerns
    deterministic_operations: DeterministicOperations
    performance_driven_decisions: PerformanceDrivenDecisions
    code_quality_standards: CodeQualityStandards
    error_handling_philosophy: ErrorHandlingPhilosophy
    feature_control: FeatureControl