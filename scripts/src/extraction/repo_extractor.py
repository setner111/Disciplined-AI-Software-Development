# MIT LICENSE - Copyright 2025 Jay Baleine (https://github.com/Varietyz https://banes-lab.com)
import os
from ..config.config import INCLUDE_PATHS, REPO_DOC_FILE
from ..building.repo_tree_builder import build_repo_tree_collapsible
from ..files.file_utils import should_exclude, get_emoji, count_lines, get_line_count_indicator
from ..format.output_formatter import create_repo_content_collapsible, save_file

class RepoExtractor:
    def __init__(self):
        self.processed_paths = set()

    def extract(self):
        root_files = []
        directory_sections = []

        for path in INCLUDE_PATHS:
            if should_exclude(path) or path in self.processed_paths:
                continue

            if os.path.isfile(path):
                self._add_file_to_root_files(path, root_files)
            elif os.path.isdir(path):
                self._add_directory_section(path, directory_sections)
            else:
                directory_sections.append(f'❌ [Not found: {path}]')

        repo_content = create_repo_content_collapsible(root_files, directory_sections)
        save_file(repo_content, REPO_DOC_FILE)

    def _add_file_to_root_files(self, path, root_files):
        line_count = count_lines(path)
        warning = get_line_count_indicator(path, line_count)
        relative_path = path.replace('\\', '/')
        filename = os.path.basename(path)
        root_files.append(f'{get_emoji(filename)} [{filename}]({relative_path}) ({line_count} lines){warning}')
        self.processed_paths.add(path)

    def _add_directory_section(self, path, directory_sections):
        dir_name = os.path.basename(path.rstrip(os.sep))
        relative_path = path.replace('\\', '/')
        section_lines = [f'📂 <a href="{relative_path}">{dir_name}</a>']
        section_lines.extend(build_repo_tree_collapsible(path))
        directory_sections.append(section_lines)
        self.processed_paths.add(path)