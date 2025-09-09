# Disciplined AI Software Development Methodology © 2025 by Jay Baleine is licensed under CC BY-SA 4.0 
# https://creativecommons.org/licenses/by-sa/4.0/
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
class WhyThisWorks:
    decision_processing: str = "AI handles \"Can you do A?\" more reliably than \"Can you do A, B, C, D, E, F, G, H?\""
    context_management: str = "Small files and bounded problems prevent the AI from juggling multiple concerns simultaneously."
    empirical_validation: str = "Performance data replaces subjective assessment. Decisions come from measurable outcomes."
    systematic_constraints: str = "Architectural checkpoints, file size limits, and dependency gates force consistent behavior."

@dataclass
class WhatToExpected:
    ai_behavior: str = "The methodology reduces architectural drift and context degradation compared to unstructured approaches. AI still needs occasional reminders about principles - this is normal."
    development_flow: str = "Systematic planning tends to reduce debugging cycles. Focused implementation helps minimize feature bloat. Performance data supports optimization decisions."
    code_quality: str = "Architectural consistency across components, measurable performance characteristics, maintainable structure as projects scale."

@dataclass
class WorkflowVisualization:
    description: str = "Mermaid flowchart showing the complete workflow from project idea through systematic implementation to completion"
    note: str = "The flowchart demonstrates the four-stage process with automated checkpoints, validation gates, and feedback loops"