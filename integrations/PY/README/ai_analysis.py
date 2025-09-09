# Disciplined AI Software Development Methodology © 2025 by Jay Baleine is licensed under CC BY-SA 4.0 
# https://creativecommons.org/licenses/by-sa/4.0/
from dataclasses import dataclass
from typing import List

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