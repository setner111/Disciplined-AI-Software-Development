# MIT LICENSE - Copyright 2025 Jay Baleine (https://github.com/Varietyz https://banes-lab.com)
"""
Configuration settings for project extraction
"""
SEPARATE_FILES = False

SOLO_REPO_DOC = False

REPO_AND_PROJECT = True

INCLUDE_PATHS = [
    'concepts',
    'example_project_structures',
    'integrations',
    'mermaid_svg',
    'persona',
    'prompt_formats',
    'questions_answers',
    'scripts',
    'templates',
    'AI-PREFERENCES.md',
    'LICENSE',
    'METHODOLOGY.md',
    'README.md',
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
    'example_project_structures',
    '.env'
]

OUTPUT_DIR = '.Project_Extraction'

OUTPUT_FILE = 'EXAMPLE_PROJECT.md'

REPO_DOC_FILE = 'REPO_NAVIGATION.md'