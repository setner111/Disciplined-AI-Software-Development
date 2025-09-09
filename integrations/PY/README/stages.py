# Disciplined AI Software Development Methodology © 2025 by Jay Baleine is licensed under CC BY-SA 4.0 
# https://creativecommons.org/licenses/by-sa/4.0/
from dataclasses import dataclass
from typing import List

@dataclass
class Stage:
    name: str
    description: str
    steps: List[str] = None
    output: str = ""
    file_size_constraint: str = ""
    benefits: List[str] = None
    implementation_flow: str = ""

@dataclass
class FourStages:
    stage1_ai_configuration: Stage
    stage2_collaborative_planning: Stage
    stage3_systematic_implementation: Stage
    stage4_data_driven_iteration: Stage

@dataclass
class ImplementationStep:
    steps: List[str]

@dataclass
class ImplementationSteps:
    setup: ImplementationStep
    execution: ImplementationStep
    quality_assurance: ImplementationStep