# Disciplined AI Software Development Methodology © 2025 by Jay Baleine is licensed under CC BY-SA 4.0 
# https://creativecommons.org/licenses/by-sa/4.0/
from dataclasses import dataclass
from .core_concepts import ContextProblem, HowThisWorks, WhyThisWorks, WhatToExpected, WorkflowVisualization
from .stages import FourStages, ImplementationSteps
from .projects_tools import ExampleProjects, ProjectStateExtraction
from .ai_analysis import LLMModels, FAQ

@dataclass
class DisciplinedAISoftwareDevelopment:
    title: str = "Disciplined AI Software Development - Collaborative"
    description: str = "A structured approach for working with AI on development projects. This methodology addresses common issues like code bloat, architectural drift, and context dilution through systematic constraints."
    context_problem: ContextProblem
    how_this_works: HowThisWorks
    four_stages: FourStages
    why_this_works: WhyThisWorks
    example_projects: ExampleProjects
    implementation_steps: ImplementationSteps
    project_state_extraction: ProjectStateExtraction
    what_to_expected: WhatToExpected
    llm_models: LLMModels
    faq: FAQ
    workflow_visualization: WorkflowVisualization
    license: str = "CC BY-SA 4.0"

def create_readme_dict():
    return {
        "title": "Disciplined AI Software Development - Collaborative",
        "description": "A structured approach for working with AI on development projects. This methodology addresses common issues like code bloat, architectural drift, and context dilution through systematic constraints.",
        "context_problem": {
            "description": "AI systems work on Question → Answer patterns. When you ask for broad, multi-faceted implementations, you typically get:",
            "issues": [
                "Functions that work but lack structure",
                "Repeated code across components", 
                "Architectural inconsistency over sessions",
                "Context dilution causing output drift",
                "More debugging time than planning time"
            ]
        },
        "how_this_works": {
            "description": "The methodology uses four stages with systematic constraints and validation checkpoints. Each stage builds on empirical data rather than assumptions.",
            "principle": "Planning saves debugging time. Planning thoroughly upfront typically prevents days of fixing architectural issues later."
        },
        "four_stages": {
            "stage1": {
                "name": "AI Configuration",
                "description": "Set up your AI model's custom instructions using AI-PREFERENCES.md. This establishes behavioral constraints and uncertainty flagging with ⚠️ indicators when the AI lacks certainty."
            },
            "stage2": {
                "name": "Collaborative Planning",
                "description": "Share METHODOLOGY.md with the AI to structure your project plan. Work together to:",
                "steps": [
                    "Define scope and completion criteria",
                    "Identify components and dependencies",
                    "Structure phases based on logical progression",
                    "Generate systematic tasks with measurable checkpoints"
                ],
                "output": "A development plan following dependency chains with modular boundaries."
            }
        },
        "why_this_works": {
            "decision_processing": "AI handles \"Can you do A?\" more reliably than \"Can you do A, B, C, D, E, F, G, H?\"",
            "context_management": "Small files and bounded problems prevent the AI from juggling multiple concerns simultaneously.",
            "empirical_validation": "Performance data replaces subjective assessment. Decisions come from measurable outcomes.",
            "systematic_constraints": "Architectural checkpoints, file size limits, and dependency gates force consistent behavior."
        },
        "license": "CC BY-SA 4.0"
    }