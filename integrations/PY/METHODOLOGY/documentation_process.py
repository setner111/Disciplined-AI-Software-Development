# Disciplined AI Software Development Methodology © 2025 by Jay Baleine is licensed under CC BY-SA 4.0 
# https://creativecommons.org/licenses/by-sa/4.0/
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class DocumentationStep:
    name: str
    questions: List[str] = None
    approach: str = ""
    mandatory_phase0: List[str] = None
    grouping_criteria: List[str] = None
    requirements: List[str] = None
    status_indicators: Dict[str, str] = None
    criteria: List[str] = None

@dataclass
class DocumentationBuildingProcess:
    step1_project_decomposition: DocumentationStep
    step2_phase_creation: DocumentationStep
    step3_task_breakdown: DocumentationStep
    step4_progress_tracking: DocumentationStep
    step5_quality_gates: DocumentationStep

@dataclass
class SuccessMetrics:
    technical_indicators: List[str] = None
    operational_indicators: List[str] = None
    development_indicators: List[str] = None
    documentation_quality: List[str] = None
    project_execution: List[str] = None
    
    def __post_init__(self):
        if self.technical_indicators is None:
            self.technical_indicators = [
                "All architectural principles consistently applied across codebase",
                "Performance baselines maintained throughout development lifecycle",
                "Zero production incidents related to architectural violations",
                "File size constraints adhered to without compromising functionality"
            ]
        if self.operational_indicators is None:
            self.operational_indicators = [
                "System uptime and reliability under production load",
                "Predictable resource utilization patterns",
                "Graceful degradation under stress conditions",
                "Maintainability preserved as codebase grows"
            ]
        if self.development_indicators is None:
            self.development_indicators = [
                "Enforcement checkpoints prevent architectural drift",
                "Performance regression detection catches optimizations and degradations",
                "Code review efficiency improved through systematic validation",
                "Technical debt accumulation prevented through continuous compliance"
            ]
        if self.documentation_quality is None:
            self.documentation_quality = [
                "Enforcement checkpoints prevent architectural drift",
                "Quality gates block progression with incomplete work",
                "Automated validation catches compliance violations",
                "Performance baselines maintained throughout development"
            ]
        if self.project_execution is None:
            self.project_execution = [
                "Systematic validation prevents technical debt accumulation",
                "Architectural principles consistently applied across codebase",
                "Performance characteristics predictable and measurable",
                "Production readiness verified at each phase"
            ]