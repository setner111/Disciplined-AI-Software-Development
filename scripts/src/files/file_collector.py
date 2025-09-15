# MIT LICENSE - Copyright 2025 Jay Baleine (https://github.com/Varietyz https://banes-lab.com)
"""
File collection and directory traversal
"""
import os
from .file_utils import should_exclude

def collect_directory_files(dir_path, current_level_only=False):
    files = []
    try:
        if current_level_only:
            for filename in os.listdir(dir_path):
                full_path = os.path.join(dir_path, filename)
                if os.path.isfile(full_path) and not should_exclude(full_path):
                    files.append(full_path)
        else:
            for root, dirs, filenames in os.walk(dir_path):
                dirs[:] = [d for d in dirs if not should_exclude(os.path.join(root, d))]
                for filename in filenames:
                    full_path = os.path.join(root, filename)
                    if not should_exclude(full_path):
                        files.append(full_path)
    except Exception:
        pass
    return files