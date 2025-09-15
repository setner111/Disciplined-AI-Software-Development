# MIT LICENSE - Copyright 2025 Jay Baleine (https://github.com/Varietyz https://banes-lab.com)
"""
File utilities and helper functions
"""
import os
from ..config.file_types import FILE_EMOJIS, TEXT_PATTERNS, CODE_EXTENSIONS, EXTENDED_MAP
from ..config.config import EXCLUDE_PATTERNS

def get_emoji(filename):
    filename_lower = filename.lower()
    for pattern, emoji in TEXT_PATTERNS.items():
        if pattern in filename_lower:
            return emoji
    return FILE_EMOJIS.get(os.path.splitext(filename)[1].lower(), '📄')

def should_exclude(path):
    return any(excl in path for excl in EXCLUDE_PATTERNS)

def count_lines(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return sum(1 for _ in f)
    except Exception:
        return 0

def is_code_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    return ext in CODE_EXTENSIONS

def get_line_count_indicator(file_path, line_count):
    if not is_code_file(file_path):
        return ""

    if line_count > 150:
        return " ‼️"
    elif line_count >= 140:
        return " ⚠️"
    return ""

def read_file_content(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"[Could not read file: {e}]"

def get_file_extension(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    filename = os.path.basename(file_path).lower()

    if filename in ['dockerfile', 'makefile', 'rakefile', 'gemfile', 'vagrantfile']:
        return filename

    return EXTENDED_MAP.get(ext, 'text')

def format_file_content(file_path, content):
    lang = get_file_extension(file_path)
    return f"```{lang}\n{content}\n```"