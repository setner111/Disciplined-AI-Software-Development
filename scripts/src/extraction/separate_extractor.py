# MIT LICENSE - Copyright 2025 Jay Baleine (https://github.com/Varietyz https://banes-lab.com)
"""
Separate files extraction
"""
import os
from ..config.config import INCLUDE_PATHS
from ..building.tree_builder import build_tree_current_level_only
from ..files.file_collector import collect_directory_files
from ..files.file_utils import (
    should_exclude, get_emoji, count_lines,
    get_line_count_indicator, read_file_content, format_file_content
)
from ..format.output_formatter import create_combined_content, save_file

class SeparateExtractor:
    def extract(self):
        for path in INCLUDE_PATHS:
            if should_exclude(path):
                continue

            if os.path.isfile(path):
                self._process_single_file(path)
            elif os.path.isdir(path):
                self._process_directory_separate(path)
            else:
                self._process_missing_path(path)

    def _process_single_file(self, path):
        line_count = count_lines(path)
        filename = os.path.basename(path)
        tree_lines = [f'{get_emoji(filename)} {filename} ({line_count} lines)']
        file_content = read_file_content(path)
        formatted_content = format_file_content(path, file_content)
        warning = get_line_count_indicator(path, line_count)
        files_content = f"\n=== File: {path} ({line_count} lines){warning} ===\n\n{formatted_content}\n"
        combined_content = create_combined_content(tree_lines, files_content, f"File: {filename}")

        base_name = os.path.splitext(filename)[0]
        save_file(combined_content, f'{base_name}.md')

    def _process_directory_separate(self, path):
        self._process_all_subfolders(path)

    def _process_missing_path(self, path):
        tree_lines = [f'❌ [Not found: {path}]']
        files_content = f"\n[Path not found: {path}]\n"
        combined_content = create_combined_content(tree_lines, files_content, f"Not Found: {path}")
        save_file(combined_content, f'NotFound_{os.path.basename(path)}.md')

    def _process_all_subfolders(self, directory, parent_name=""):
        if should_exclude(directory):
            return

        dir_name = os.path.basename(directory.rstrip(os.sep))
        full_name = f"{parent_name}_{dir_name}" if parent_name else dir_name

        tree_lines = [f'📂 {dir_name}'] + build_tree_current_level_only(directory)

        files = collect_directory_files(directory, current_level_only=True)
        content_parts = []

        for file_path in files:
            line_count = count_lines(file_path)
            warning = get_line_count_indicator(file_path, line_count)
            content_parts.append(f"\n=== File: {file_path} ({line_count} lines){warning} ===\n\n")
            file_content = read_file_content(file_path)
            content_parts.append(format_file_content(file_path, file_content))
            content_parts.append("\n")

        files_content = ''.join(content_parts)
        combined_content = create_combined_content(tree_lines, files_content, f"Folder: {directory}")
        save_file(combined_content, f'{full_name}.md')

        try:
            for entry in os.listdir(directory):
                full_path = os.path.join(directory, entry)
                if os.path.isdir(full_path) and not should_exclude(full_path):
                    self._process_all_subfolders(full_path, full_name)
        except PermissionError:
            pass