# Disciplined AI Software Development Methodology © 2025 by Jay Baleine is licensed under CC BY-SA 4.0 
# https://creativecommons.org/licenses/by-sa/4.0/
from dataclasses import dataclass
from typing import List

@dataclass
class BenchmarkingSuite:
    requirements: List[str] = None
    
    def __post_init__(self):
        if self.requirements is None:
            self.requirements = [
                "Core Framework: Performance measurement with component isolation",
                "Regression Detection: Compare against previous results, fail on performance drops",
                "Baseline Management: Save and track performance baselines over time",
                "JSON Output: Structured data for automated analysis and CI integration",
                "Timeline Tracking: Historical performance data across project evolution"
            ]

@dataclass
class CICDInfrastructure:
    requirements: List[str] = None
    
    def __post_init__(self):
        if self.requirements is None:
            self.requirements = [
                "Release Workflows: Automated versioning, building, and deployment",
                "Regression Detection: Benchmark comparison on every commit/PR",
                "Quality Gates: Block merges that fail performance or quality thresholds",
                "Automated Testing: Run full test suite on code changes"
            ]

@dataclass
class CoreArchitecture:
    requirements: List[str] = None
    
    def __post_init__(self):
        if self.requirements is None:
            self.requirements = [
                "Centralized Entry Points: Single main module that orchestrates everything",
                "Configuration Management: Externalized settings with validation",
                "Centralized Logging: Error handling and diagnostic output with JSON integration",
                "Dependency Injection: Clean separation and testable components"
            ]

@dataclass
class TestingInfrastructure:
    requirements: List[str] = None
    
    def __post_init__(self):
        if self.requirements is None:
            self.requirements = [
                "Test Suite: Unit and integration tests for all components",
                "Stress Testing: Load and boundary condition validation",
                "Test Data Management: Reproducible test scenarios and cleanup",
                "Coverage Tracking: Ensure adequate test coverage before releases"
            ]

@dataclass
class DocumentationSystem:
    requirements: List[str] = None
    
    def __post_init__(self):
        if self.requirements is None:
            self.requirements = [
                "Automated Generation: Extract documentation from code and structure",
                "Architecture Documentation: System design and component relationships",
                "API Documentation: Interface specifications and usage examples",
                "Performance Documentation: Benchmark results and optimization guides"
            ]

@dataclass
class Phase0Requirements:
    title: str = "Basic Must-Haves (Phase 0 - Always First)"
    description: str = "Every project, regardless of size, must establish these foundational systems before any feature development"
    benchmarking_suite: BenchmarkingSuite
    cicd_infrastructure: CICDInfrastructure
    core_architecture: CoreArchitecture
    testing_infrastructure: TestingInfrastructure
    documentation_system: DocumentationSystem
    critical_note: str = "These systems must be operational before writing any application logic. They become the foundation that enables rapid, confident development."