# MIT LICENSE - Copyright 2025 Jay Baleine (https://github.com/Varietyz https://banes-lab.com)
"""
File type mappings and identification logic
"""

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