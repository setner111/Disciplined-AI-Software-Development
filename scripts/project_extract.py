# MIT LICENSE - Copyright 2025 Jay Baleine (https://github.com/Varietyz https://banes-lab.com)
"""
Project Structure Extraction Tool for AI Collaboration

USAGE:
    python project_extract.py

CONFIGURATION:
    Edit the settings in src/config.py to customize output:

    SEPARATE_FILES:
        - False: Single THE_PROJECT.md file (recommended for small codebases)
        - True: Multiple files per directory (recommended for large codebases)

    INCLUDE_PATHS:
        - List directories/files to analyze
        - Add new paths as needed for your project structure

    EXCLUDE_PATTERNS:
        - Patterns to skip (cache dirs, build artifacts, etc.)
        - Prevents cluttering output with generated files

    OUTPUT_DIR/OUTPUT_FILE:
        - Where extracted files are saved
        - Change if you need different output location

PURPOSE:
    Generates structured project snapshots for systematic AI collaboration.
    Provides complete file contents and structure for AI context sharing.
    Enforces documentation discipline through automated extraction.

    Use this to:
    1. Share complete project state with AI systems
    2. Track architectural compliance (file sizes, structure)
    3. Generate systematic documentation for methodology adherence
    4. Create focused development context for AI sessions
"""
from src.extractor import ProjectExtractor

def main():
    extractor = ProjectExtractor()
    extractor.extract()

if __name__ == '__main__':
    main()