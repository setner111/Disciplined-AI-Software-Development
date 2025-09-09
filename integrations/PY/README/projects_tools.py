# Disciplined AI Software Development Methodology © 2025 by Jay Baleine is licensed under CC BY-SA 4.0 
# https://creativecommons.org/licenses/by-sa/4.0/
from dataclasses import dataclass
from typing import List

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