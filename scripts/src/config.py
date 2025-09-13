# MIT LICENSE - Copyright 2025 Jay Baleine (https://github.com/Varietyz https://banes-lab.com)
"""
Configuration settings for project extraction
"""

SEPARATE_FILES = False
INCLUDE_PATHS = [
    'example_project_structures',
    'integrations',
    'persona',
    'prompt_formats',
    'scripts',
    'templates',
    'README.md',
    'METHODOLOGY.md',
    'AI-PREFERENCES.md',
    'README-persona.md'
]
EXCLUDE_PATTERNS = [
    'phicode.egg-info',
    '__pycache__',
    '.(φ)cache',
    '.pypirc',
    'node_modules',
    '.git',
    'scaffold.py',
    'EXAMPLE_PROJECT.md',
    'BENCH_DASH.md',
    'SNIPPETS.md',
    'output_example',
    'example_project_structures'
]
OUTPUT_DIR = '.Project_Extraction'
OUTPUT_FILE = 'EXAMPLE_PROJECT.md'