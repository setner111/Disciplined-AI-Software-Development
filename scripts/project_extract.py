# MIT LICENSE - Copyright 2025 Jay Baleine (https://github.com/Varietyz https://banes-lab.com)
"""
Project Structure Extraction Tool for AI Collaboration

USAGE:
    python project_extract.py

CONFIGURATION:
    Edit the settings below to customize output:

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
import os

# ============================================================================
# CONFIGURATION SETTINGS
# ============================================================================

SEPARATE_FILES = False
#SEPARATE_FILES = True  # Uncomment for multiple output files

INCLUDE_PATHS = ['example_workflow']
EXCLUDE_PATTERNS = ['phicode.egg-info', '__pycache__', '.(φ)cache', '.pypirc', 'node_modules', '.git', 'scaffold.py', 'EXAMPLE_PROJECT.md', 'BENCH_DASH.md', 'SNIPPETS.md']
OUTPUT_DIR = '.Project_Extraction'
OUTPUT_FILE = 'example_workflow/EXAMPLE_PROJECT.md'

# ============================================================================
# FILE TYPE MAPPINGS
# ============================================================================

FILE_EMOJIS = {
    '.py': '🐍', '.js': '📜', '.json': '🔧', '.txt': '📄', '.md': '📝', '.html': '🌐',
    '.css': '🎨', '.jpg': '🖼️', '.jpeg': '🖼️', '.png': '🖼️', '.gif': '🖼️', '.ico': '🖼️',
    '.mp3': '🎵', '.wav': '🎵', '.mp4': '🎞️', '.pdf': '📕', '.gdoc': '🗄️', '.xlsx': '🧮',
    '.psd': '🖌️', '.φ': '🔱', '.phi': '🔱', '.agent': '🤖', '.vsix': '🔌', '.yml': '⚙️', '.yaml': '⚙️',
    '.ts': '📘', '.tsx': '📘', '.jsx': '⚛️', '.vue': '💚', '.svelte': '🧡',
    '.php': '🐘', '.rb': '💎', '.go': '🐹', '.rs': '🦀', '.swift': '🦉',
    '.java': '☕', '.cs': '💜', '.cpp': '⚡', '.c': '⚡', '.h': '📋',
    '.sql': '🗃️', '.db': '🗃️', '.sqlite': '🗃️', '.csv': '📊', 
    '.xml': '📰', '.toml': '🔧', '.ini': '🔧', '.env': '🌍',
    '.dockerfile': '🐳', '.docker': '🐳', '.sh': '🐚', '.bat': '⚫',
    '.log': '📜', '.lock': '🔒', '.zip': '📦', '.tar': '📦', '.gz': '📦',
    '.ttf': '🔤', '.otf': '🔤', '.woff': '🔤', '.svg': '🎨',
}

CODE_EXTENSIONS = {
    '.py', '.js', '.jsx', '.ts', '.tsx', '.java', '.c', '.cpp', '.cc', '.cxx',
    '.h', '.hpp', '.cs', '.vb', '.php', '.rb', '.go', '.rs', '.swift', '.kt',
    '.scala', '.clj', '.hs', '.ml', '.fs', '.elm', '.dart', '.lua', '.r',
    '.m', '.mm', '.pl', '.pm', '.φ', '.phi', '.f90', '.f95', '.f03', '.pas',
    '.ada', '.adb', '.tcl', '.vhdl', '.vhd', '.v', '.vh', '.asm', '.s',
    '.lisp', '.lsp', '.scm', '.jl', '.nim', '.zig', '.d', '.cr', '.ex',
    '.exs', '.erl', '.hrl'
}

TEXT_PATTERNS = {
    'readme': '📘', 'license': '⚖️', 'receipt': '🧾', 'faq': '❓', 'rules': '📖',
    'invitation': '💌', 'agenda': '📅', 'analytics': '📈', 'brainstorming': '🧠',
    'insights': '🔎', 'guidelines': 'ℹ️', 'tools': '🛠️', 'sponsor': '💵',
    'finished': '✅', 'bot': '🤖', 'data': '📊', 'config': '⚙️',
    'test': '🧪', 'spec': '🧪', 'benchmark': '⚡', 'performance': '📈',
    'api': '🔌', 'endpoint': '🔌', 'route': '🛣️', 'middleware': '🔄',
    'database': '🗃️', 'migration': '🔄', 'schema': '📋', 'model': '🏗️',
    'component': '🧩', 'service': '⚙️', 'utility': '🔧', 'helper': '🤝',
    'security': '🔐', 'auth': '🔐', 'permission': '🔒', 'validation': '✅',
    'error': '❌', 'exception': '⚠️', 'log': '📝', 'audit': '📋',
    'docker': '🐳', 'container': '📦', 'deploy': '🚀', 'release': '🏷️',
    'workflow': '🔄', 'pipeline': '⚡', 'action': '🎬', 'hook': '🪝',
    'plugin': '🔌', 'extension': '🧩', 'module': '📦', 'package': '📦',
    'template': '📝', 'layout': '🏗️', 'style': '🎨', 'theme': '🎨',
    'constant': '🔢', 'enum': '📝', 'interface': '🔌', 'type': '📋',
    'index': '📇', 'main': '🏠', 'entry': '🚪', 'bootstrap': '🚀',
}

EXTENDED_MAP = {
    '.py': 'python', '.js': 'javascript', '.jsx': 'jsx', '.ts': 'typescript', '.tsx': 'tsx',
    '.java': 'java', '.c': 'c', '.cpp': 'cpp', '.cc': 'cpp', '.cxx': 'cpp', '.h': 'c', '.hpp': 'cpp',
    '.cs': 'csharp', '.vb': 'vbnet', '.php': 'php', '.rb': 'ruby', '.go': 'go', '.rs': 'rust',
    '.swift': 'swift', '.kt': 'kotlin', '.scala': 'scala', '.clj': 'clojure', '.hs': 'haskell',
    '.ml': 'ocaml', '.fs': 'fsharp', '.elm': 'elm', '.dart': 'dart', '.lua': 'lua', '.r': 'r',
    '.m': 'objectivec', '.mm': 'objectivec', '.pl': 'perl', '.pm': 'perl', '.φ': 'python', '.phi': 'python',
    '.html': 'html', '.htm': 'html', '.css': 'css', '.scss': 'scss', '.sass': 'sass', '.less': 'less',
    '.vue': 'vue', '.svelte': 'svelte', '.sh': 'bash', '.bash': 'bash', '.zsh': 'bash', '.fish': 'fish',
    '.ps1': 'powershell', '.bat': 'batch', '.cmd': 'batch', '.json': 'json', '.xml': 'xml',
    '.yaml': 'yaml', '.yml': 'yaml', '.toml': 'toml', '.ini': 'ini', '.cfg': 'ini', '.conf': 'apache',
    '.properties': 'properties', '.env': 'bash', '.lock': 'json', '.md': 'markdown', '.rst': 'rst',
    '.txt': 'text', '.tex': 'latex', '.hbs': 'handlebars', '.mustache': 'mustache', '.jinja': 'jinja2',
    '.jinja2': 'jinja2', '.j2': 'jinja2', '.twig': 'twig', '.erb': 'erb', '.ejs': 'ejs', '.pug': 'pug',
    '.jade': 'jade', '.sql': 'sql', '.dockerfile': 'dockerfile', '.gradle': 'gradle', '.makefile': 'makefile',
    '.cmake': 'cmake', '.bazel': 'python', '.bzl': 'python', '.log': 'log', '.diff': 'diff',
    '.patch': 'diff', '.gitignore': 'gitignore', '.editorconfig': 'editorconfig',
}

# ============================================================================
# LOGIC
# ============================================================================

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

def build_tree_current_level_only(directory, prefix=''):
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
        lines.append(f'{prefix}{symbol} {get_emoji(entry)} {entry} ({line_count} lines){warning}')

    return lines

def build_tree(directory, prefix=''):
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
            lines.append(f'{prefix}{symbol} 📂 {entry}')
            lines.extend(build_tree(full_path, new_prefix))
        else:
            line_count = count_lines(full_path)
            warning = get_line_count_indicator(full_path, line_count)
            lines.append(f'{prefix}{symbol} {get_emoji(entry)} {entry} ({line_count} lines){warning}')

    return lines

def read_file_content(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        return f"[Could not read file: {e}]"

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

def create_combined_content(tree_lines, files_content, title="The Project"):
    tree_section = f'''## 📂 {title} - Current Tree Structure
```
{chr(10).join(tree_lines)}
```

## 📄 Project File Contents

'''
    return f'''<img src="https://banes-lab.com/assets/images/banes_lab/700px_Main_Animated.gif" width="70" />

{tree_section}{files_content}'''

def save_file(content, filename):
    if SEPARATE_FILES:
        analysis_dir = os.path.join(OUTPUT_DIR)
        os.makedirs(analysis_dir, exist_ok=True)
        output_path = os.path.join(analysis_dir, filename)
    else:
        output_path = filename

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Extraction saved to {output_path}')

def get_file_extension(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    filename = os.path.basename(file_path).lower()

    if filename in ['dockerfile', 'makefile', 'rakefile', 'gemfile', 'vagrantfile']:
        return filename

    return EXTENDED_MAP.get(ext, 'text')

def format_file_content(file_path, content):
    lang = get_file_extension(file_path)
    return f"```{lang}\n{content}\n```"

def process_all_subfolders(directory, parent_name=""):
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
                process_all_subfolders(full_path, full_name)
    except PermissionError:
        pass

def main():
    if SEPARATE_FILES:
        for path in INCLUDE_PATHS:
            if should_exclude(path):
                continue

            if os.path.isfile(path):
                line_count = count_lines(path)
                tree_lines = [f'{get_emoji(os.path.basename(path))} {os.path.basename(path)} ({line_count} lines)']
                file_content = read_file_content(path)
                formatted_content = format_file_content(path, file_content)
                warning = get_line_count_indicator(path, line_count)
                files_content = f"\n=== File: {path} ({line_count} lines){warning} ===\n\n{formatted_content}\n"
                combined_content = create_combined_content(tree_lines, files_content, f"File: {os.path.basename(path)}")

                base_name = os.path.splitext(os.path.basename(path))[0]
                save_file(combined_content, f'{base_name}.md')
            elif os.path.isdir(path):
                process_all_subfolders(path)
            else:
                tree_lines = [f'❓ [Not found: {path}]']
                files_content = f"\n[Path not found: {path}]\n"
                combined_content = create_combined_content(tree_lines, files_content, f"Not Found: {path}")
                save_file(combined_content, f'NotFound_{os.path.basename(path)}.md')
    else:
        all_tree_lines = []
        all_files_content = []
        processed_paths = set()

        for path in INCLUDE_PATHS:
            if should_exclude(path) or path in processed_paths:
                continue

            if os.path.isfile(path):
                line_count = count_lines(path)
                warning = get_line_count_indicator(path, line_count)
                all_tree_lines.append(f'{get_emoji(os.path.basename(path))} {os.path.basename(path)} ({line_count} lines)')
                all_files_content.append(f"\n=== File: {path} ({line_count} lines){warning} ===\n\n")
                file_content = read_file_content(path)
                all_files_content.append(format_file_content(path, file_content))
                all_files_content.append("\n")
                processed_paths.add(path)
            elif os.path.isdir(path):
                dir_name = os.path.basename(path.rstrip(os.sep))
                all_tree_lines.append(f'📂 {dir_name}')
                all_tree_lines.extend(build_tree(path))

                files = collect_directory_files(path)
                for file_path in files:
                    if file_path not in processed_paths:
                        line_count = count_lines(file_path)
                        warning = get_line_count_indicator(file_path, line_count)
                        all_files_content.append(f"\n=== File: {file_path} ({line_count} lines){warning} ===\n\n")
                        file_content = read_file_content(file_path)
                        all_files_content.append(format_file_content(file_path, file_content))
                        all_files_content.append("\n")
                        processed_paths.add(file_path)
                processed_paths.add(path)
            else:
                all_tree_lines.append(f'❓ [Not found: {path}]')
                all_files_content.append(f"\n[Path not found: {path}]\n")

        combined_content = create_combined_content(all_tree_lines, ''.join(all_files_content))
        save_file(combined_content, OUTPUT_FILE)

if __name__ == '__main__':
    main()