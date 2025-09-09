# Disciplined AI Software Development Methodology © 2025 by Jay Baleine is licensed under CC BY-SA 4.0 
# https://creativecommons.org/licenses/by-sa/4.0/
from dataclasses import dataclass
from .core_principles import FoundationalPhilosophy, CodeArchitecturePrinciples
from .web_adaptations import WebDevelopmentAdaptations, PrincipleIntegration
from .phase0_requirements import Phase0Requirements
from .documentation_process import DocumentationBuildingProcess, SuccessMetrics
from .enforcement_framework import SystematicEnforcementFramework

@dataclass
class ProjectDocumentationMethodology:
    title: str = "Project Documentation Methodology"
    foundational_philosophy: FoundationalPhilosophy
    code_architecture_principles: CodeArchitecturePrinciples
    web_development_adaptations: WebDevelopmentAdaptations
    phase0_requirements: Phase0Requirements
    documentation_building_process: DocumentationBuildingProcess
    systematic_enforcement_framework: SystematicEnforcementFramework
    principle_integration: PrincipleIntegration
    success_metrics: SuccessMetrics
    conclusion: str = "This methodology enforces discipline through automated checking and explicit validation points, preventing the gradual erosion of architectural principles during development."
    license: str = "CC BY-SA 4.0"

def create_methodology_dict():
    return {
        "title": "Project Documentation Methodology",
        "foundational_philosophy": {
            "architectural_minimalism": "Every line of code must earn its place through measurable value. Build systems that work predictably in production, not demonstrations of sophistication."
        },
        "phase0_requirements": {
            "title": "Basic Must-Haves (Phase 0 - Always First)",
            "description": "Every project, regardless of size, must establish these foundational systems before any feature development",
            "benchmarking_suite": [
                "Core Framework: Performance measurement with component isolation",
                "Regression Detection: Compare against previous results, fail on performance drops",
                "Baseline Management: Save and track performance baselines over time",
                "JSON Output: Structured data for automated analysis and CI integration",
                "Timeline Tracking: Historical performance data across project evolution"
            ],
            "cicd_infrastructure": [
                "Release Workflows: Automated versioning, building, and deployment",
                "Regression Detection: Benchmark comparison on every commit/PR",
                "Quality Gates: Block merges that fail performance or quality thresholds",
                "Automated Testing: Run full test suite on code changes"
            ],
            "core_architecture": [
                "Centralized Entry Points: Single main module that orchestrates everything",
                "Configuration Management: Externalized settings with validation",
                "Centralized Logging: Error handling and diagnostic output with JSON integration",
                "Dependency Injection: Clean separation and testable components"
            ],
            "testing_infrastructure": [
                "Test Suite: Unit and integration tests for all components",
                "Stress Testing: Load and boundary condition validation",
                "Test Data Management: Reproducible test scenarios and cleanup",
                "Coverage Tracking: Ensure adequate test coverage before releases"
            ],
            "documentation_system": [
                "Automated Generation: Extract documentation from code and structure",
                "Architecture Documentation: System design and component relationships",
                "API Documentation: Interface specifications and usage examples",
                "Performance Documentation: Benchmark results and optimization guides"
            ],
            "critical_note": "These systems must be operational before writing any application logic. They become the foundation that enables rapid, confident development."
        },
        "conclusion": "This methodology enforces discipline through automated checking and explicit validation points, preventing the gradual erosion of architectural principles during development.",
        "license": "CC BY-SA 4.0"
    }