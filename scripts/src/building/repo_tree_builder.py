# MIT LICENSE - Copyright 2025 Jay Baleine (https://github.com/Varietyz https://banes-lab.com)
"""
Repository navigation tree building with collapsible HTML sections
"""
import os
from ..files.file_utils import should_exclude, get_emoji, count_lines, get_line_count_indicator

def build_repo_tree_collapsible(directory, prefix=''):
    if should_exclude(directory):
        return []

    try:
        entries = [e for e in os.listdir(directory) if not should_exclude(os.path.join(directory, e))]
    except PermissionError:
        return [f"{prefix}└─ 🔒 [Permission Denied: {os.path.basename(directory)}]"]

    files = []
    directories = []

    for entry in entries:
        full_path = os.path.join(directory, entry)
        if os.path.isdir(full_path):
            directories.append(entry)
        else:
            files.append(entry)

    files.sort()
    directories.sort()

    ordered_entries = files + directories

    lines = []
    for i, entry in enumerate(ordered_entries):
        full_path = os.path.join(directory, entry)
        is_last = i == len(ordered_entries) - 1
        symbol = '└─' if is_last else '├─'
        new_prefix = prefix + ('    ' if is_last else '│   ')

        if os.path.isdir(full_path):
            relative_path = full_path.replace('\\', '/')
            lines.append(f'{prefix}{symbol} 📂 <a href="{relative_path}">{entry}</a>')
            lines.extend(build_repo_tree_collapsible(full_path, new_prefix))
        else:
            line_count = count_lines(full_path)
            warning = get_line_count_indicator(full_path, line_count)
            relative_path = full_path.replace('\\', '/')
            lines.append(f'{prefix}{symbol} {get_emoji(entry)} <a href="{relative_path}">{entry}</a> ({line_count} lines){warning}')

    return lines

def build_repo_tree_current_level_only(directory, prefix=''):
    if should_exclude(directory):
        return []

    try:
        entries = [e for e in os.listdir(directory) if not should_exclude(os.path.join(directory, e))]
    except PermissionError:
        return [f"{prefix}└─ 🔒 [Permission Denied: {os.path.basename(directory)}]"]

    lines = []
    files_only = [e for e in entries if os.path.isfile(os.path.join(directory, e))]

    for i, entry in enumerate(files_only):
        is_last = i == len(files_only) - 1
        symbol = '└─' if is_last else '├─'
        file_path = os.path.join(directory, entry)
        line_count = count_lines(file_path)
        warning = get_line_count_indicator(file_path, line_count)
        relative_path = file_path.replace('\\', '/')
        lines.append(f'{prefix}{symbol} {get_emoji(entry)} <a href="{relative_path}">{entry}</a> ({line_count} lines){warning}')

    return lines

def build_repo_tree(directory, prefix=''):
    if should_exclude(directory):
        return []

    try:
        entries = [e for e in os.listdir(directory) if not should_exclude(os.path.join(directory, e))]
    except PermissionError:
        return [f"{prefix}└─ 🔒 [Permission Denied: {os.path.basename(directory)}]"]

    files = []
    directories = []

    for entry in entries:
        full_path = os.path.join(directory, entry)
        if os.path.isdir(full_path):
            directories.append(entry)
        else:
            files.append(entry)

    files.sort()
    directories.sort()

    ordered_entries = files + directories

    lines = []
    for i, entry in enumerate(ordered_entries):
        full_path = os.path.join(directory, entry)
        is_last = i == len(ordered_entries) - 1
        symbol = '└─' if is_last else '├─'
        new_prefix = prefix + ('    ' if is_last else '│   ')

        if os.path.isdir(full_path):
            relative_path = full_path.replace('\\', '/')
            lines.append(f'{prefix}{symbol} 📂 <a href="{relative_path}">{entry}</a>')
            lines.extend(build_repo_tree_collapsible(full_path, new_prefix))
        else:
            line_count = count_lines(full_path)
            warning = get_line_count_indicator(full_path, line_count)
            relative_path = full_path.replace('\\', '/')
            lines.append(f'{prefix}{symbol} {get_emoji(entry)} <a href="{relative_path}">{entry}</a> ({line_count} lines){warning}')

    return lines