from dataclasses import dataclass
from typing import List

@dataclass
class InteractionRules:
    avoid_enthusiasm: bool = True
    forbidden_words: List[str] = None
    avoid_em_dashes: bool = True
    no_unverifiable_percentages: bool = True
    ground_in_accuracy: bool = True
    uncertainty_flag: str = "⚠️"
    never_claim_solution: bool = True
    accurate_terminology: bool = True
    first_person_documentation: bool = True
    show_observed_behavior: bool = True
    simple_punctuation: bool = True
    no_small_talk: bool = True
    avoid_friendly_statements: bool = True
    
    def __post_init__(self):
        if self.forbidden_words is None:
            self.forbidden_words = [
                "paradigm", "revolutionary", "leader", "innovator", 
                "mathematical precision", "breakthrough", "flagship", 
                "novel", "enhanced", "sophisticated", "advanced", 
                "excellence", "fascinating", "profound"
            ]

@dataclass
class TrainingData:
    flag_unverifiable: str = "🔬"
    never_implement_unverifiable: bool = True
    state_limitations: bool = True

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

@dataclass
class MethodologyRules:
    interaction: InteractionRules
    training_data: TrainingData
    phase0_requirements: Phase0Requirements
    code_instructions: CodeInstructions
    website_specifics: WebsiteSpecifics
    
    license: str = "CC BY-SA 4.0"
    attribution_required_public: bool = True
    attribution_required_ai_collab: bool = False

def create_rules_dict():
    return {
        "interaction_rules": {
            "avoid_enthusiasm": True,
            "forbidden_words": [
                "paradigm", "revolutionary", "leader", "innovator",
                "mathematical precision", "breakthrough", "flagship",
                "novel", "enhanced", "sophisticated", "advanced",
                "excellence", "fascinating", "profound"
            ],
            "avoid_em_dashes": True,
            "no_unverifiable_percentages": True,
            "ground_in_accuracy": True,
            "uncertainty_flag": "⚠️",
            "never_claim_solution": True,
            "accurate_terminology": True,
            "first_person_documentation": True,
            "show_observed_behavior": True,
            "simple_punctuation": True,
            "no_small_talk": True,
            "avoid_friendly_statements": True
        },
        "training_data": {
            "flag_unverifiable": "🔬",
            "never_implement_unverifiable": True,
            "state_limitations": True
        },
        "phase0_requirements": {
            "benchmarking_suite": True,
            "github_workflows": True,
            "centralized_main": True,
            "test_suite": True,
            "documentation_generation": True,
            "components": [
                "regression detection", "baseline saving", "json",
                "timeline", "visual pie charts"
            ]
        },
        "code_instructions": {
            "lightweight_performant": True,
            "clean_architecture": True,
            "synchronous_operations": True,
            "separation_of_concerns": True,
            "modular_layout": True,
            "benchmarking_suite_required": True,
            "json_output_required": True,
            "optimize_bottlenecks_only": True,
            "robust_error_handling": True,
            "performance_over_trends": True,
            "readability_priority": True,
            "resist_feature_bloat": True,
            "multiple_languages_allowed": True,
            "deterministic_behavior": True,
            "code_in_artifacts": True,
            "max_file_lines": 150,
            "handle_edge_cases_collaboratively": True,
            "reuse_existing_code": True,
            "retain_naming_conventions": True,
            "no_comments": True,
            "kiss_dry_principles": True,
            "architectural_minimalism": True,
            "surgical_approach": True,
            "document_refactors": True
        },
        "website_specifics": {
            "never_inline": True,
            "max_component_lines": 250,
            "async_operations_permitted": True,
            "error_boundaries_required": True,
            "colocate_component_files": True,
            "split_multi_purpose_components": True,
            "clarify_architectural_compliance": True,
            "compliance_warning": "⚠️ Without explicit architectural reinforcement, methodology violations will occur during code generation tasks."
        },
        "metadata": {
            "license": "CC BY-SA 4.0",
            "attribution_required_public": True,
            "attribution_required_ai_collab": False
        }
    }