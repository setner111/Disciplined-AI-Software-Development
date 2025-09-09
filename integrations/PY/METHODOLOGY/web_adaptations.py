# Disciplined AI Software Development Methodology © 2025 by Jay Baleine is licensed under CC BY-SA 4.0 
# https://creativecommons.org/licenses/by-sa/4.0/
from dataclasses import dataclass
from typing import List

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