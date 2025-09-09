from dataclasses import dataclass
from typing import List

@dataclass
class ContextProblem:
    description: str = "AI systems work on Question → Answer patterns. When you ask for broad, multi-faceted implementations, you typically get:"
    issues: List[str] = None
    
    def __post_init__(self):
        if self.issues is None:
            self.issues = [
                "Functions that work but lack structure",
                "Repeated code across components",
                "Architectural inconsistency over sessions",
                "Context dilution causing output drift",
                "More debugging time than planning time"
            ]

@dataclass
class HowThisWorks:
    description: str = "The methodology uses four stages with systematic constraints and validation checkpoints. Each stage builds on empirical data rather than assumptions."
    principle: str = "Planning saves debugging time. Planning thoroughly upfront typically prevents days of fixing architectural issues later."

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
class WhyThisWorks:
    decision_processing: str = "AI handles \"Can you do A?\" more reliably than \"Can you do A, B, C, D, E, F, G, H?\""
    context_management: str = "Small files and bounded problems prevent the AI from juggling multiple concerns simultaneously."
    empirical_validation: str = "Performance data replaces subjective assessment. Decisions come from measurable outcomes."
    systematic_constraints: str = "Architectural checkpoints, file size limits, and dependency gates force consistent behavior."

@dataclass
class ExampleProject:
    name: str
    url: str
    description: str
    structure_link: str

@dataclass
class ExampleProjects:
    projects: List[ExampleProject]
    note: str = "You can compare the methodology principles to the codebase structure to see how the approach translates to working code."

@dataclass
class ImplementationStep:
    steps: List[str]

@dataclass
class ImplementationSteps:
    setup: ImplementationStep
    execution: ImplementationStep
    quality_assurance: ImplementationStep

@dataclass
class ConfigurationOption:
    name: str
    description: str
    example: str = ""

@dataclass
class ProjectStateExtraction:
    description: str = "Use the included project extraction tool systematically to generate structured snapshots of your codebase"
    command: str = "python scripts/project_extract.py"
    configuration_options: List[ConfigurationOption] = None
    output_features: List[str] = None
    usage: str = "Use the tool to share a complete or partial project state with the AI system, track architectural compliance, and create focused development context."
    output_examples: str = "scripts/output_example"
    
    def __post_init__(self):
        if self.configuration_options is None:
            self.configuration_options = [
                ConfigurationOption(
                    "SEPARATE_FILES = False",
                    "Single THE_PROJECT.md file (recommended for small codebases)",
                    "scripts/output_example/THE_PROJECT.md"
                ),
                ConfigurationOption(
                    "SEPARATE_FILES = True",
                    "Multiple files per directory (recommended for large codebases and focused folder work)",
                    "scripts/output_example/.Project_Extraction"
                ),
                ConfigurationOption(
                    "INCLUDE_PATHS",
                    "Directories and files to analyze"
                ),
                ConfigurationOption(
                    "EXCLUDE_PATTERNS",
                    "Skip cache directories, build artifacts, and generated files"
                )
            ]
        if self.output_features is None:
            self.output_features = [
                "Complete file contents with syntax highlighting",
                "File line counts with architectural warnings (⚠️ for 140-150 lines, ‼️ for >150 lines on code files)",
                "Tree structure visualization",
                "Ready-to-share"
            ]

@dataclass
class WhatToExpected:
    ai_behavior: str = "The methodology reduces architectural drift and context degradation compared to unstructured approaches. AI still needs occasional reminders about principles - this is normal."
    development_flow: str = "Systematic planning tends to reduce debugging cycles. Focused implementation helps minimize feature bloat. Performance data supports optimization decisions."
    code_quality: str = "Architectural consistency across components, measurable performance characteristics, maintainable structure as projects scale."

@dataclass
class LLMModel:
    name: str
    link: str

@dataclass
class LLMModels:
    description: str = "Explore the detailed Q-A for each AI model"
    models: List[LLMModel] = None
    evaluation_description: str = "All models were asked the exact same questions using the methodology documents as file uploads. This evaluation focuses on methodology understanding and operational behavior, no code was generated."
    analysis_link: str = "questions_answers/Q-A_COMPREHENSION_ANALYSIS.md"
    note: str = "This analysis does not include any code generation."
    coverage_areas: List[str] = None
    
    def __post_init__(self):
        if self.models is None:
            self.models = [
                LLMModel("Grok 3", "questions_answers/Q-A_GROK_3.md"),
                LLMModel("Claude Sonnet 4", "questions_answers/Q-A_CLAUDE_SONNET_4.md"),
                LLMModel("DeepSeek-V3", "questions_answers/Q-A_DEEPSEEK-V3.md"),
                LLMModel("Gemini 2.5 Flash", "questions_answers/Q-A_GEMINI_2.5_FLASH.md")
            ]
        if self.coverage_areas is None:
            self.coverage_areas = [
                "Methodology understanding and workflow patterns",
                "Context retention and collaborative interaction",
                "Communication adherence and AI preference compliance",
                "Project initialization and Phase 0 requirements",
                "Tool usage and technology stack compatibility",
                "Quality enforcement and violation handling",
                "User experience across different skill levels"
            ]

@dataclass
class FAQQuestion:
    title: str
    answer: str

@dataclass
class FAQCategory:
    questions: List[FAQQuestion]

@dataclass
class FAQ:
    origin_and_development: FAQCategory
    personal_practice: FAQCategory
    ai_development_journey: FAQCategory
    methodology_specifics: FAQCategory
    practical_implementation: FAQCategory

@dataclass
class WorkflowVisualization:
    description: str = "Mermaid flowchart showing the complete workflow from project idea through systematic implementation to completion"
    note: str = "The flowchart demonstrates the four-stage process with automated checkpoints, validation gates, and feedback loops"

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
            },
            "stage3": {
                "name": "Systematic Implementation",
                "description": "Work phase by phase, section by section. Each request follows: \"Can you implement [specific component]?\" with focused objectives.",
                "file_size_constraint": "File size stays ≤150 lines.",
                "benefits": [
                    "Smaller context windows for processing",
                    "Focused implementation over multi-function attempts",
                    "Easier sharing and debugging"
                ],
                "implementation_flow": "Request specific component → AI processes → Validate → Benchmark → Continue"
            },
            "stage4": {
                "name": "Data-Driven Iteration",
                "description": "The benchmarking suite (built first) provides performance data throughout development. Feed this data back to the AI for optimization decisions based on measurements rather than guesswork."
            }
        },
        "why_this_works": {
            "decision_processing": "AI handles \"Can you do A?\" more reliably than \"Can you do A, B, C, D, E, F, G, H?\"",
            "context_management": "Small files and bounded problems prevent the AI from juggling multiple concerns simultaneously.",
            "empirical_validation": "Performance data replaces subjective assessment. Decisions come from measurable outcomes.",
            "systematic_constraints": "Architectural checkpoints, file size limits, and dependency gates force consistent behavior."
        },
        "example_projects": [
            {
                "name": "Discord Bot Template",
                "url": "https://github.com/Varietyz/discord-js-bot-template",
                "description": "Production-ready bot foundation with plugin architecture, security, API management, and comprehensive testing. 46 files, all under 150 lines, with benchmarking suite and automated compliance checking.",
                "structure_link": "example_project_structures/DISCORDJS_TEMPLATE_PROJECT.md"
            },
            {
                "name": "PhiCode Runtime",
                "url": "https://github.com/Varietyz/phicode-runtime",
                "description": "Programming language runtime engine with transpilation, caching, security validation, and Rust acceleration. Complex system maintaining architectural discipline across 70+ modules.",
                "structure_link": "example_project_structures/PHICODE_RUNTIME_PROJECT.md"
            },
            {
                "name": "PhiPipe",
                "url": "https://github.com/Varietyz/PhiPipe",
                "description": "CI/CD regression detection system with statistical analysis, GitHub integration, and concurrent processing. Go-based service handling performance baselines and automated regression alerts.",
                "structure_link": "example_project_structures/PHIPIPE_PROJECT.md"
            }
        ],
        "implementation_steps": {
            "setup": [
                "Configure AI with AI-PREFERENCES.md as custom instructions",
                "Share METHODOLOGY.md for planning session",
                "Collaborate on project structure and phases",
                "Generate systematic development plan"
            ],
            "execution": [
                "Build Phase 0 benchmarking infrastructure first",
                "Work through phases sequentially",
                "Implement one component per interaction",
                "Run benchmarks and share results with AI",
                "Validate architectural compliance continuously"
            ],
            "quality_assurance": [
                "Performance regression detection",
                "Architectural principle validation",
                "Code duplication auditing",
                "File size compliance checking",
                "Dependency boundary verification"
            ]
        },
        "faq_categories": [
            "Origin and Development",
            "Personal Practice", 
            "AI Development Journey",
            "Methodology Specifics",
            "Practical Implementation"
        ],
        "license": "CC BY-SA 4.0"
    }