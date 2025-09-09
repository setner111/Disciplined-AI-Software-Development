# Disciplined AI Software Development Methodology © 2025 by Jay Baleine is licensed under CC BY-SA 4.0 
# https://creativecommons.org/licenses/by-sa/4.0/
from dataclasses import dataclass
from .interaction import InteractionRules, TrainingData
from .code import Phase0Requirements, CodeInstructions, WebsiteSpecifics

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