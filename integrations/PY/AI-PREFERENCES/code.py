# Disciplined AI Software Development Methodology © 2025 by Jay Baleine is licensed under CC BY-SA 4.0 
# https://creativecommons.org/licenses/by-sa/4.0/
from dataclasses import dataclass
from typing import List

@dataclass
class Phase0Requirements:
    benchmarking_suite: bool = True
    github_workflows: bool = True
    centralized_main: bool = True
    test_suite: bool = True
    documentation_generation: bool = True
    
    components: List[str] = None
    
    def __post_init__(self):
        if self.components is None:
            self.components = [
                "regression detection", "baseline saving", "json", 
                "timeline", "visual pie charts"
            ]

@dataclass
class CodeInstructions:
    lightweight_performant: bool = True
    clean_architecture: bool = True
    synchronous_operations: bool = True
    separation_of_concerns: bool = True
    modular_layout: bool = True
    benchmarking_suite_required: bool = True
    json_output_required: bool = True
    optimize_bottlenecks_only: bool = True
    robust_error_handling: bool = True
    performance_over_trends: bool = True
    readability_priority: bool = True
    resist_feature_bloat: bool = True
    multiple_languages_allowed: bool = True
    deterministic_behavior: bool = True
    code_in_artifacts: bool = True
    max_file_lines: int = 150
    handle_edge_cases_collaboratively: bool = True
    reuse_existing_code: bool = True
    retain_naming_conventions: bool = True
    no_comments: bool = True
    kiss_dry_principles: bool = True
    architectural_minimalism: bool = True
    surgical_approach: bool = True
    document_refactors: bool = True

@dataclass
class WebsiteSpecifics:
    never_inline: bool = True
    max_component_lines: int = 250
    async_operations_permitted: bool = True
    error_boundaries_required: bool = True
    colocate_component_files: bool = True
    split_multi_purpose_components: bool = True
    clarify_architectural_compliance: bool = True
    compliance_warning: str = "⚠️ Without explicit architectural reinforcement, methodology violations will occur during code generation tasks."