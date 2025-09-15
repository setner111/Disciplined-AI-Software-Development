# MIT LICENSE - Copyright 2025 Jay Baleine (https://github.com/Varietyz https://banes-lab.com)
"""
Core project extraction functionality
"""
from ..config.config import SOLO_REPO_DOC, SEPARATE_FILES, REPO_AND_PROJECT
from .repo_extractor import RepoExtractor
from .combined_extractor import CombinedExtractor
from .separate_extractor import SeparateExtractor

class ProjectExtractor:
    def __init__(self):
        self.processed_paths = set()

    def extract(self):
        if REPO_AND_PROJECT:
            repo_extractor = RepoExtractor()
            repo_extractor.extract()

            if SEPARATE_FILES:
                separate_extractor = SeparateExtractor()
                separate_extractor.extract()
            else:
                combined_extractor = CombinedExtractor()
                combined_extractor.extract()
        elif SOLO_REPO_DOC:
            extractor = RepoExtractor()
        elif SEPARATE_FILES:
            extractor = SeparateExtractor()
        else:
            extractor = CombinedExtractor()

        if not REPO_AND_PROJECT:
            extractor.extract()