# MIT LICENSE - Copyright 2025 Jay Baleine (https://github.com/Varietyz https://banes-lab.com)
"""
Combined file extraction
"""
import os
from ..config.config import INCLUDE_PATHS, OUTPUT_FILE
from ..building.tree_builder import build_tree
from ..files.file_collector import collect_directory_files
from ..files.file_utils import (
    should_exclude, get_emoji, count_lines,
    get_line_count_indicator, read_file_content, format_file_content
)
from ..format.output_formatter import create_combined_content, save_file

class CombinedExtractor:
    def __init__(self):
        self.processed_paths = set()

    def extract(self):
        all_tree_lines = []
        all_files_content = []

        for path in INCLUDE_PATHS:
            if should_exclude(path) or path in self.processed_paths:
                continue

            if os.path.isfile(path):
                self._add_file_to_combined(path, all_tree_lines, all_files_content)
            elif os.path.isdir(path):
                self._add_directory_to_combined(path, all_tree_lines, all_files_content)
            else:
                self._add_missing_to_combined(path, all_tree_lines, all_files_content)

        combined_content = create_combined_content(all_tree_lines, ''.join(all_files_content))
        save_file(combined_content, OUTPUT_FILE)

    def _add_file_to_combined(self, path, all_tree_lines, all_files_content):
        line_count = count_lines(path)
        warning = get_line_count_indicator(path, line_count)
        filename = os.path.basename(path)
        all_tree_lines.append(f'{get_emoji(filename)} {filename} ({line_count} lines)')
        all_files_content.append(f"\n=== File: {path} ({line_count} lines){warning} ===\n\n")
        file_content = read_file_content(path)
        all_files_content.append(format_file_content(path, file_content))
        all_files_content.append("\n")
        self.processed_paths.add(path)

    def _add_directory_to_combined(self, path, all_tree_lines, all_files_content):
        dir_name = os.path.basename(path.rstrip(os.sep))
        all_tree_lines.append(f'📂 {dir_name}')
        all_tree_lines.extend(build_tree(path))

        files = collect_directory_files(path)
        for file_path in files:
            if file_path not in self.processed_paths:
                line_count = count_lines(file_path)
                warning = get_line_count_indicator(file_path, line_count)
                all_files_content.append(f"\n=== File: {file_path} ({line_count} lines){warning} ===\n\n")
                file_content = read_file_content(file_path)
                all_files_content.append(format_file_content(file_path, file_content))
                all_files_content.append("\n")
                self.processed_paths.add(file_path)
        self.processed_paths.add(path)

    def _add_missing_to_combined(self, path, all_tree_lines, all_files_content):
        all_tree_lines.append(f'❌ [Not found: {path}]')
        all_files_content.append(f"\n[Path not found: {path}]\n")