<img src="https://banes-lab.com/assets/images/banes_lab/700px_Main_Animated.gif" width="70" />

## 📂 The Project - Current Tree Structure
```
📂 src
└─ 📂 phicode_engine
    ├─ 🐍 __init__.py (25 lines)
    ├─ 🏠 __main__.py (7 lines)
    ├─ 🐍 engine.py (44 lines)
    ├─ 📂 api
    │   ├─ 🐍 __init__.py (6 lines)
    │   ├─ 🐍 cli.py (37 lines)
    │   ├─ 🐍 http_server.py (133 lines)
    │   └─ 🐍 subprocess_handler.py (75 lines)
    ├─ 📂 benchsuite
    │   ├─ 🐍 __init__.py (28 lines)
    │   ├─ 🔱 bench_cache.φ (28 lines)
    │   ├─ 🔱 bench_extreme_stress.φ (67 lines)
    │   ├─ 🔱 bench_memory.φ (39 lines)
    │   ├─ 🔱 bench_stress.φ (39 lines)
    │   ├─ 🔱 bench_symbol_density.φ (51 lines)
    │   ├─ 🔱 bench_transpiler.φ (27 lines)
    │   ├─ 🔱 bench_transpiler_patterns.φ (107 lines)
    │   ├─ 🔱 bench_transpiler_scaling.φ (82 lines)
    │   ├─ ⚡ benchmark_cli.py (7 lines)
    │   ├─ ⚡ benchmark_commands.py (32 lines)
    │   ├─ ⚡ benchmark_core.py (125 lines)
    │   ├─ ⚡ benchmark_prints.py (14 lines)
    │   ├─ ⚡ benchmark_visualizer.py (87 lines)
    │   ├─ 🐍 system_info.py (67 lines)
    │   └─ 📂 simulation
    │       ├─ 🔱 simulate_concurrency.φ (81 lines)
    │       ├─ 🔱 simulate_crash.φ (111 lines)
    │       ├─ 🔱 simulate_import_burst.φ (52 lines)
    │       ├─ 🔱 simulate_phimmuno_threat.φ (99 lines)
    │       ├─ 🔱 simulate_stress_transpiler.φ (65 lines)
    │       └─ 🔱 simulate_workload_cache.φ (47 lines)
    ├─ 📂 config
    │   ├─ ⚙️ config.py (133 lines)
    │   └─ 🐍 version.py (6 lines)
    ├─ 📂 core
    │   ├─ 📝 phicode_logger.py (12 lines)
    │   ├─ 📂 cache
    │   │   ├─ 🐍 phicode_bytecode.py (136 lines)
    │   │   ├─ 🐍 phicode_cache.py (83 lines)
    │   │   ├─ 🐍 phicode_cache_ops.py (73 lines)
    │   │   └─ ✅ phicode_cache_validation.py (38 lines)
    │   ├─ 📂 importing
    │   │   ├─ 🐍 phicode_central.py (52 lines)
    │   │   ├─ 🐍 phicode_finder.py (108 lines)
    │   │   └─ 🐍 phicode_importer.py (18 lines)
    │   ├─ 📂 interpreter
    │   │   ├─ 🐍 phicode_args.py (57 lines)
    │   │   ├─ 🐍 phicode_executor.py (45 lines)
    │   │   ├─ 🐍 phicode_exit_handlers.py (25 lines)
    │   │   ├─ 🐍 phicode_interpreter.py (85 lines)
    │   │   ├─ 🐍 phicode_interpreter_display.py (57 lines)
    │   │   ├─ 🐍 phicode_switch.py (68 lines)
    │   │   └─ 📂 cli
    │   │       ├─ 🐍 phicode_cli.py (92 lines)
    │   │       ├─ 🐍 phicode_cli_handlers.py (107 lines)
    │   │       └─ 🐍 phicode_cli_parser.py (39 lines)
    │   ├─ 📂 mod
    │   │   └─ ⚙️ phicode_config_generator.py (35 lines)
    │   ├─ 📂 runtime
    │   │   ├─ 🐍 phicode_loader.py (56 lines)
    │   │   ├─ 🐍 phicode_runtime.py (131 lines)
    │   │   └─ 🐍 shutdown_handler.py (79 lines)
    │   └─ 📂 transpilation
    │       ├─ 🐍 phicode_to_python.py (137 lines)
    │       ├─ ⚙️ symbol_config.py (96 lines)
    │       └─ 🐍 symbol_optimization.py (33 lines)
    ├─ 📂 installers
    │   ├─ 🐍 __init__.py (3 lines)
    │   ├─ 🐍 binary_installer.py (89 lines)
    │   ├─ 🐍 phimmuno_installer.py (46 lines)
    │   └─ 🐍 phirust_installer.py (46 lines)
    ├─ 📂 rust
    │   ├─ 🐍 __init__.py (7 lines)
    │   ├─ 🐍 phirust_accelerator.py (77 lines)
    │   └─ 🐍 phirust_cli.py (48 lines)
    └─ 📂 security
        ├─ 🐍 __init__.py (6 lines)
        ├─ 🐍 phimmuno_cli.py (48 lines)
        └─ 🐍 phimmuno_validator.py (53 lines)
📂 rust_scripts
├─ 📂 phimmuno_engine
│   ├─ 🔧 Cargo.toml (12 lines)
│   ├─ 🏠 main.rs (29 lines)
│   └─ 🏷️ release.yml (39 lines)
└─ 📂 phirust_transpiler
    ├─ 🔧 Cargo.toml (16 lines)
    ├─ 🏠 main.rs (160 lines) ‼️
    ├─ 🏷️ release.yml (39 lines)
    └─ 🦀 threat_detector.rs (30 lines)
🔧 pyproject.toml (43 lines)
⚖️ LICENSE (44 lines)
```

## 📄 Project File Contents


=== File: src\phicode_engine\engine.py (44 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
import os
from .core.interpreter.cli.phicode_cli import parse_args
from .core.interpreter.phicode_exit_handlers import handle_early_exit_flags
from .core.runtime.phicode_runtime import run
from .core.phicode_logger import logger

def main():
    args = None
    try:
        args = parse_args()
        if handle_early_exit_flags(args):
            return

        is_switched = os.environ.get('PHICODE_ALREADY_SWITCHED', '0') == '1'

        if not is_switched:
            if args.bypass:
                logger.warning("   🔓 SECURITY BYPASS ENABLED")
                logger.warning("Threat detection is DISABLED for this execution.")
            else:
                logger.warning("   ⚠️  SECURITY WARNING ⚠️")
                logger.warning("This engine executes code on your machine.")
                logger.warning("Only provide input from trusted sources.")
                logger.warning("🔍 All code is screened for dangerous patterns before execution.")

        if args.debug:
            logger.setLevel("DEBUG")
            logger.debug("Debug mode enabled via centralized args")

        run(args)

    except KeyboardInterrupt:
        logger.info("Execution interrupted by user")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        if args and args.debug:
            import traceback
            traceback.print_exc()

if __name__ == "__main__":
    main()
```

=== File: src\phicode_engine\__init__.py (25 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
from .core.importing.phicode_importer import install_phicode_importer
from .core.transpilation.phicode_to_python import transpile_symbols, get_symbol_mappings
from .config.version import __version__

try:
    from .rust import try_rust_acceleration, handle_rust_commands
    _HAS_RUST = True
except ImportError:
    _HAS_RUST = False
    try_rust_acceleration = None
    handle_rust_commands = None

__version__
__all__ = [
    "install_phicode_importer",
    "transpile_symbols", 
    "get_symbol_mappings",
    "main"
]

if _HAS_RUST:
    __all__.extend(["try_rust_acceleration", "handle_rust_commands"])
```

=== File: src\phicode_engine\__main__.py (7 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
from .engine import main

if __name__ == "__main__":
    main()
```

=== File: src\phicode_engine\api\cli.py (37 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
import argparse
import sys
from .http_server import start_server
from .subprocess_handler import PhicodeSubprocessHandler
from ..config.config import ENGINE, SERVER
from ..core.phicode_logger import logger

def main():
    parser = argparse.ArgumentParser(description=f" {SERVER}")
    parser.add_argument("--host", default="localhost", help="Server host (default: localhost)")
    parser.add_argument("--port", type=int, default=8000, help="Server port (default: 8000)")
    parser.add_argument("--timeout", type=int, default=30, help="Execution timeout in seconds")

    args = parser.parse_args()

    logger.info(f"🔍 Checking {ENGINE} availability...")
    handler = PhicodeSubprocessHandler()
    info = handler.get_engine_info()

    if not info["success"]:
        logger.error(f"❌ {ENGINE} not available: {info['error']}")
        logger.info(f"💡 Make sure {ENGINE} is installed: pip install phicode")
        sys.exit(1)

    logger.info(f"✅ {ENGINE} Available!")

    try:
        start_server(args.host, args.port)
    except Exception as e:
        logger.error(f"❌ Failed to start {SERVER}: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```

=== File: src\phicode_engine\api\http_server.py (133 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
import http.server
import socketserver
import json
from .subprocess_handler import PhicodeSubprocessHandler
from ..config.config import SERVER, ENGINE
from ..core.phicode_logger import logger
from ..security.phimmuno_validator import is_content_safe, is_security_enabled

class PhicodeHTTPServer(http.server.BaseHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.handler = PhicodeSubprocessHandler()
        super().__init__(*args, **kwargs)

    def do_POST(self):
        if self.path == '/execute':
            self._handle_execute()
        elif self.path == '/convert':
            self._handle_convert()
        else:
            self._send_error(404, f"{SERVER} Endpoint not found")

    def do_GET(self):
        if self.path == '/info':
            self._handle_info()
        elif self.path == '/symbols':
            self._handle_symbols()
        else:
            self._send_error(404, f"{SERVER} Endpoint not found")

    def _handle_convert(self):
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            if content_length == 0:
                self._send_error(400, "Empty request body")
                return

            post_data = self.rfile.read(content_length).decode('utf-8')
            payload = json.loads(post_data)

            if 'code' not in payload or 'target' not in payload:
                self._send_error(400, "Missing 'code' or 'target' field")
                return

            if is_security_enabled() and not is_content_safe(payload.get('code', '')):
                self._send_error(403, "Security threat detected")
                return

            result = self.handler.convert_code(payload['code'], payload['target'])
            self._send_json_response(result)

        except json.JSONDecodeError:
            self._send_error(400, "Invalid JSON")
        except Exception as e:
            self._send_error(500, f"{SERVER} error: {str(e)}")

    def _handle_symbols(self):
        result = self.handler.get_symbol_mappings()
        self._send_json_response(result)

    def _handle_execute(self):
        try:
            content_length = int(self.headers.get('Content-Length', 0))
            if content_length == 0:
                self._send_error(400, "Empty request body")
                return

            post_data = self.rfile.read(content_length).decode('utf-8')
            payload = json.loads(post_data)

            if 'code' not in payload:
                self._send_error(400, "Missing 'code' field")
                return

            if is_security_enabled() and not is_content_safe(payload.get('code', '')):
                self._send_error(403, "Security threat detected")
                return

            result = self.handler.execute_code(
                payload['code'],
                payload.get('type', 'auto')
            )
            self._send_json_response(result)

        except json.JSONDecodeError:
            self._send_error(400, "Invalid JSON")
        except Exception as e:
            self._send_error(500, f"{SERVER} error: {str(e)}")

    def _handle_info(self):
        result = self.handler.get_engine_info()
        self._send_json_response(result)

    def _send_json_response(self, data):
        response_body = json.dumps(data, ensure_ascii=False)
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', str(len(response_body.encode('utf-8'))))
        self.end_headers()
        self.wfile.write(response_body.encode('utf-8'))

    def _send_error(self, code, message):
        error_data = {"success": False, "error": message}
        response_body = json.dumps(error_data)
        self.send_response(code)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', str(len(response_body)))
        self.end_headers()
        self.wfile.write(response_body.encode('utf-8'))

def start_server(host: str = "localhost", port: int = 8000):
    try:
        with socketserver.TCPServer((host, port), PhicodeHTTPServer) as httpd:
            logger.info(f"🌐 {SERVER} running on http://{host}:{port}")
            logger.info("📋 Endpoints:")
            logger.info("   POST /execute - Execute φ or Python code")
            logger.info("   POST /convert - Convert Python ↔ φ")
            logger.info(f"   GET  /info    - {ENGINE} info")
            logger.info("   GET  /symbols - Symbol mappings")

            if is_security_enabled():
                logger.info("🛡️  Security validation: ENABLED")
            else:
                logger.info("🛡️  Security validation: DISABLED (install with --phimmuno)")

            logger.info("🔄 Press Ctrl+C to stop")
            httpd.serve_forever()
    except KeyboardInterrupt:
        logger.info(f"\nℹ️  {SERVER} stopped")
    except Exception as e:
        logger.error(f"❌ {SERVER} error: {e}")
```

=== File: src\phicode_engine\api\subprocess_handler.py (75 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
import sys
import subprocess
import time
from ..config.config import ENGINE, BADGE, SYMBOL, PYTHON_TO_PHICODE, PHICODE_VERSION

try:
    import regex as re
except ImportError:
    import re

class PhicodeSubprocessHandler:
    def __init__(self, timeout: int = 30):
        self.timeout = timeout
        self.phicode_to_python = {v: k for k, v in PYTHON_TO_PHICODE.items()}

    def execute_code(self, code: str, code_type: str = "auto") -> dict:
        start_time = time.perf_counter()
        if code_type == "phicode" or (code_type == "auto" and self._is_phicode(code)):
            # Development HAX:
            # script = f'import sys; sys.path.insert(0, r"{os.path.dirname(os.path.dirname(os.path.dirname(__file__)))}"); from phicode_engine.core.transpilation.phicode_to_python import transpile_symbols; exec(transpile_symbols("""{code}"""))'
            #PRODUCTION: 
            script = f'from phicode_engine.core.transpilation.phicode_to_python import transpile_symbols; exec(transpile_symbols("""{code}"""))'

        else:
            script = code
        try:
            result = subprocess.run([sys.executable, '-c', script], capture_output=False, text=True, timeout=self.timeout)
            return {"success": result.returncode == 0, "output": result.stdout, "error": result.stderr if result.returncode != 0 else None, "execution_time": time.perf_counter() - start_time}
        except subprocess.TimeoutExpired:
            return {"success": False, "error": f"Timeout ({self.timeout}s)"}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def convert_code(self, code: str, target: str) -> dict:
        try:
            if target == "phicode":
                converted = self._python_to_phi(code)
                symbols_used = [sym for sym in PYTHON_TO_PHICODE.values() if sym in converted]
                return {"success": True, "converted": converted, "symbols_used": symbols_used, "target": target}
            elif target == "python":
                converted = self._phi_to_python(code)
                return {"success": True, "converted": converted, "target": target}
            else:
                return {"success": False, "error": f"Invalid target: {target}"}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def get_symbol_mappings(self) -> dict:
        return {"success": True, "python_to_phicode": PYTHON_TO_PHICODE, "phicode_to_python": self.phicode_to_python, "symbol_count": len(PYTHON_TO_PHICODE)}

    def _python_to_phi(self, code: str) -> str:
        converted = code
        for python_kw, phi_symbol in sorted(PYTHON_TO_PHICODE.items(), key=lambda x: len(x[0]), reverse=True):
            pattern = rf'\b{re.escape(python_kw)}\b'
            converted = re.sub(pattern, phi_symbol, converted)
        return converted

    def _phi_to_python(self, code: str) -> str:
        converted = code
        for phi_symbol, python_kw in self.phicode_to_python.items():
            converted = converted.replace(phi_symbol, python_kw)
        return converted

    def get_engine_info(self) -> dict:
        try:
            result = subprocess.run([sys.executable, '-c', 'import sys; print(f"{sys.implementation.name} {sys.version_info.major}.{sys.version_info.minor}")'], capture_output=True, text=True, timeout=5)
            return {"success": True, "engine": ENGINE, "badge": BADGE, "symbol": SYMBOL, "python_info": result.stdout.strip(), "api_version": PHICODE_VERSION}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def _is_phicode(self, code: str) -> bool:
        return any(symbol in code for symbol in PYTHON_TO_PHICODE.values())
```

=== File: src\phicode_engine\api\__init__.py (6 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
from .subprocess_handler import PhicodeSubprocessHandler
from .http_server import start_server
from .cli import main
```

=== File: src\phicode_engine\benchsuite\benchmark_cli.py (7 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
from .benchmark_commands import parse_benchmark_command

def run_benchmarks():
    parse_benchmark_command()
```

=== File: src\phicode_engine\benchsuite\benchmark_commands.py (32 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
import sys
import os

def parse_benchmark_command():
    try:
        from phicode_engine.core.importing.phicode_importer import install_phicode_importer
        benchsuite_dir = os.path.dirname(__file__)
        install_phicode_importer(benchsuite_dir)
    except ImportError:
        pass

    if "--simulation" in sys.argv:
        from phicode_engine.benchsuite.simulation import run_simulations
        run_simulations.main()
        return True

    if "--full" in sys.argv:
        from phicode_engine.benchsuite.benchmark_core import run_full_benchmark_report
        run_full_benchmark_report()
        return True

    if "--json" in sys.argv:
        from phicode_engine.benchsuite.benchmark_core import run_json_benchmarks
        run_json_benchmarks()
        return True

    from phicode_engine.benchsuite.benchmark_core import run_interactive_benchmarks
    run_interactive_benchmarks()
    return True
```

=== File: src\phicode_engine\benchsuite\benchmark_core.py (125 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
import json
import sys
import subprocess
import os
from datetime import datetime
from phicode_engine.config.config import BADGE, BENCHMARK_FOLDER_PATH, SECONDARY_FILE_TYPE, MAIN_FILE_TYPE, ENGINE, SYMBOL
from phicode_engine.core.phicode_logger import logger

def _find_files(directory, prefix, suffix):
    try:
        return [os.path.join(directory, entry.name)
                for entry in os.scandir(directory)
                if entry.is_file() and
                    entry.name.startswith(prefix) and
                    entry.name.endswith(suffix)]
    except OSError:
        return []

def discover_benchmarks():
    benchsuite_dir = os.path.dirname(__file__)

    engine_phi = _find_files(benchsuite_dir, "bench_", MAIN_FILE_TYPE)

    simulation_dir = os.path.join(benchsuite_dir, "simulation")
    simulation_phi = _find_files(simulation_dir, "simulate_", MAIN_FILE_TYPE) if os.path.exists(simulation_dir) else []

    project_phi = _find_files(BENCHMARK_FOLDER_PATH, "", MAIN_FILE_TYPE) if os.path.exists(BENCHMARK_FOLDER_PATH) else []
    project_py = _find_files(BENCHMARK_FOLDER_PATH, "", SECONDARY_FILE_TYPE) if os.path.exists(BENCHMARK_FOLDER_PATH) else []

    return {
        "engine": engine_phi,
        "simulation": simulation_phi,
        "project": project_phi + project_py,
        "all": engine_phi + simulation_phi + project_phi + project_py
    }

def execute_benchmark_file(file_path: str):
    try:
        name = os.path.splitext(os.path.basename(file_path))[0]
        benchsuite_dir = os.path.dirname(file_path)

        intesive_benchmarks = ["extreme", "crash", "phimmuno"]

        if any(keyword in name for keyword in intesive_benchmarks):
            timeout = 5*60
        else:
            timeout = 60

        result = subprocess.run([sys.executable, '-m', 'phicode_engine', name], capture_output=True, text=True, cwd=benchsuite_dir, timeout=timeout)

        return {"status": "completed" if result.returncode == 0 else "error", "output": result.stdout, "error": result.stderr if result.returncode != 0 else None}
    except subprocess.TimeoutExpired:
        return {"status": "timeout", "error": f"Benchmark timeout ({timeout}s)"}
    except Exception as e:
        return {"status": "failed", "error": str(e)}

def run_json_benchmarks():
    discovered = discover_benchmarks()
    results = {}
    for benchmark in discovered['all']:
        name = os.path.splitext(os.path.basename(benchmark))[0]
        results[name] = execute_benchmark_file(benchmark)
    logger.info(json.dumps(results, indent=2))

def run_full_benchmark_report():
    from phicode_engine.benchsuite.benchmark_visualizer import generate_visualization_report, export_results_csv
    from phicode_engine.benchsuite.system_info import format_system_report

    logger.info("🔄 Running full benchmark suite...")

    results = {}
    for benchmark in discover_benchmarks()['all']:
        name = os.path.splitext(os.path.basename(benchmark))[0]
        logger.info(f"⚡ Executing {name}...")
        results[name] = execute_benchmark_file(benchmark)

    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")
    hour_dir = os.path.join(BENCHMARK_FOLDER_PATH, now.strftime("%Y%m%d"), now.strftime("%H"))
    os.makedirs(hour_dir, exist_ok=True)

    # Write all outputs
    files = {
        f"{BADGE}bench_results_{timestamp}.json": lambda f: json.dump({"system": format_system_report(), "results": results}, f, indent=2),
        f"{BADGE}bench_results_{timestamp}.csv": lambda f: f.write(export_results_csv(results)),
        f"{BADGE}bench_results_{timestamp}.md": lambda f: f.write(generate_visualization_report(results))
    }

    for name, func in files.items():
        with open(os.path.join(hour_dir, name), "w") as f:
            func(f)

    logger.info(f"✅ Complete report package generated in {hour_dir}")
    logger.info(" → 📄 benchmark_results.json")
    logger.info(" → 📊 benchmark_results.csv")
    logger.info(" → 📈 benchmark_report.md (with Mermaid diagrams)")

def run_interactive_benchmarks():
    discovered = discover_benchmarks()

    from .benchmark_prints import print_benchsuite_entry
    print_benchsuite_entry(discovered, ENGINE, SYMBOL)

    selection = input("\nEnter selection (1-5): ").strip()
    logger.info(f"> Auto-executing discovered {SYMBOL} files...")

    if selection == "1":
        benchmarks = discovered['engine']
    elif selection == "2":
        benchmarks = discovered['project'] or []
    elif selection == "3":
        benchmarks = discovered['all']
    elif selection == "5":
        benchmarks = discovered['simulation']
    else:
        benchmarks = discovered['engine'][:2]

    for benchmark in benchmarks:
        result = execute_benchmark_file(benchmark)
        logger.info(result["output"])

    logger.info("💡 Additional options: --json --full")
```

=== File: src\phicode_engine\benchsuite\benchmark_prints.py (14 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
def print_benchsuite_entry(discovered, ENGINE, SYMBOL):
    print(f"{ENGINE} Self-Validation")
    print("=" * 30)
    print(f"Auto-discovered benchmarks:")
    print(f"  ✅ Engine self-benchmarks ({len(discovered['engine'])} {SYMBOL} files)")
    print(f"  ✅ Simulation benchmarks ({len(discovered['simulation'])} {SYMBOL} files)")
    print(f"  ✅ Project benchmarks ({len(discovered['project'])} {SYMBOL} files)")
    print("\nSelect benchmarks to run:")
    print("1. Engine Self-Validation\n2. Project Performance Analysis")
    print("3. Combined Analysis\n4. Quick Performance Check")
    print("5. Workload Simulation")
```

=== File: src\phicode_engine\benchsuite\benchmark_visualizer.py (87 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
import json
from typing import Dict

def generate_mermaid_performance_chart(results: Dict) -> str:
    chart_lines = ["graph TD"]

    for name, data in results.items():
        if data.get("status") != "completed":
            continue

        output = data.get("output", "")
        if "chars/sec" in output:
            speed = _extract_metric(output, "chars/sec")
            chart_lines.append(f'    {name}["{name}<br/>{speed} chars/sec"]')
        elif "Hit Rate" in output:
            rate = _extract_metric(output, "Hit Rate")
            chart_lines.append(f'    {name}["{name}<br/>Hit Rate: {rate}"]')
        elif "MB" in output:
            memory = _extract_metric(output, "MB")
            chart_lines.append(f'    {name}["{name}<br/>{memory}MB"]')
        else:
            chart_lines.append(f'    {name}["{name}<br/>✓ Completed"]')

    return "\n".join(chart_lines)

def create_performance_summary_chart(results: Dict) -> str:
    passed = sum(1 for r in results.values() if r.get("status") == "completed")
    total = len(results)

    chart = f"""flowchart LR
    A[Φ Engine Benchmarks] --> B["{passed}/{total} Passed"]
    B --> C[Performance Validated]

    style A fill:#e1f5fe
    style B fill:#c8e6c9
    style C fill:#dcedc8"""

    return chart

def export_results_csv(results: Dict) -> str:
    lines = ["Benchmark,Status,Output"]

    for name, data in results.items():
        status = data.get("status", "unknown")
        output = data.get("output", "").replace("\n", " | ").replace(",", ";")
        lines.append(f"{name},{status},{output}")

    return "\n".join(lines)

def _extract_metric(text: str, metric: str) -> str:
    lines = text.split("\n")
    for line in lines:
        if metric in line:
            parts = line.split(metric)[0].split()
            if parts:
                return parts[-1].replace(":", "")
    return "N/A"

def generate_visualization_report(results: Dict, format: str = "mermaid") -> str:
    if format == "mermaid":
        performance_chart = generate_mermaid_performance_chart(results)
        summary_chart = create_performance_summary_chart(results)

        return f"""# Φ Engine Performance Report

## Summary
```mermaid
{summary_chart}
```

## Detailed Performance
```mermaid
{performance_chart}
```

## Results Data
{len(results)} benchmarks executed
"""

    elif format == "csv":
        return export_results_csv(results)

    else:
        return json.dumps(results, indent=2)
```

=== File: src\phicode_engine\benchsuite\bench_cache.φ (28 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the PhiCode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
← phicode_engine.core.cache.phicode_cache ⇒ _cache
← phicode_engine.config.config ⇒ PYTHON_TO_PHICODE

ƒ report(name, result):
    π(f"{name}: {result}")

initial_size = ℓ(_cache.python_cache)

symbols = list(PYTHON_TO_PHICODE.values())[:5]
test_sources = []

∀ i, symbol ∈ №(symbols):
    test_sources.append(f"{symbol} x: π(x + {i})")

operation_count = 0
∀ source ∈ test_sources * 3:
    _cache.get_python_source(f"test_{operation_count}", source)
    operation_count += 1

final_size = ℓ(_cache.python_cache)
cache_growth = final_size - initial_size
hit_rate = ⭱(0, (operation_count - cache_growth) / operation_count) ¿ operation_count > 0 ⋄ 0

report("Cache Hit Rate", f"{hit_rate:.2f}")
report("Cache Growth", f"{cache_growth} entries")
```

=== File: src\phicode_engine\benchsuite\bench_extreme_stress.φ (67 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the PhiCode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
⇒ time

← phicode_engine.core.transpilation.phicode_to_python ⇒ SymbolTranspiler
← phicode_engine.benchsuite ⇒ report
transpiler = SymbolTranspiler()

base_pattern = """
ƒ process_data(data):
    ∴:
        ∀ item ∈ data:
            ¿ item ≡ Ø ∨ ¬ item.is_valid():
                ⇉
            ¿ hasattr(item, 'value') ∧ item.value > 0:
                result = calculate_result(item)
                ¿ result ≡ ¬ Ø:
                    ⟲ result * 2
        ⟲ ✓
    ⛒ Exception ↦ e:
        ↑ RuntimeError("Processing failed") ← e
    ⇗:
        π("Cleanup completed")
"""

ƒ generate_stress_content(base_pattern: str, target_size: int) -> str:
    content = ""
    ↻ ℓ(content) < target_size:
        content += base_pattern + "\n"
    ⟲ content[:target_size]

stress_stages = [
    ("stressed", 5_000_000),
    ("extreme", 6_500_000),
    ("deadly", 8_000_000),
    ("atomic", 10_000_000)
]

∀ stage_name, size ∈ stress_stages:
    π(f"\n{stage_name.upper()} STAGE: {size:,} chars ({size/1024/1024:.1f}MB)")

    content = generate_stress_content(base_pattern, size)

    start_time = time.perf_counter()
    result = transpiler.transpile(content)
    end_time = time.perf_counter()

    elapsed = end_time - start_time
    chars_per_sec = ℓ(content) / elapsed

    π(f"Time: {elapsed:.3f}s")
    π(f"Speed: {chars_per_sec:,.0f} chars/sec")
    π(f"Output size: {len(result):,} chars")

    report(f"{stage_name}_input_size", f"{len(content):,} chars")
    report(f"{stage_name}_output_size", f"{len(result):,} chars")
    report(f"{stage_name}_time", f"{elapsed:.3f}s")
    report(f"{stage_name}_speed", f"{chars_per_sec:,.0f} chars/sec")
    report(f"{stage_name}_throughput_mb", f"{len(content)/1024/1024/elapsed:.2f} MB/sec")

    ¿ chars_per_sec >= 3_000_000:
        π("✅ Extreme performance achieved (≥ 3M chars/sec)")
        report(f"{stage_name}_status", "EXTREME_PERFORMANCE_ACHIEVED")
    ⋄:
        π("⚠️ Below target performance")
        report(f"{stage_name}_status", "BELOW_TARGET_PERFORMANCE")
```

=== File: src\phicode_engine\benchsuite\bench_memory.φ (39 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the PhiCode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
← phicode_engine.core.cache.phicode_bytecode ⇒ BytecodeManager
← phicode_engine.config.config ⇒ PYTHON_TO_PHICODE, MAIN_FILE_TYPE
⇒ os

∴:
    ⇒ psutil
    HAS_PSUTIL = ✓
⛒ ImportError:
    HAS_PSUTIL = ⊥

ƒ report(name, result):
    π(f"{name}: {result}")

¿ ¬ HAS_PSUTIL:
    report("Memory Usage", "psutil not available - install with: pip install psutil")
⋄:
    process = psutil.Process(os.getpid())
    initial_memory = process.memory_info().rss / 1024 / 1024

    symbols = list(PYTHON_TO_PHICODE.values())
    test_code = """
for i in range(100):
   if i % 2 == 0:
       print(f"Even: {i}")
   else:
       print(f"Odd: {i}")
"""

    ∀ i ∈ ⟪(5):
        BytecodeManager.compile_and_cache(test_code, f"test_memory_{i}{MAIN_FILE_TYPE}")

    final_memory = process.memory_info().rss / 1024 / 1024
    memory_increase = final_memory - initial_memory

    report("Memory Usage", f"{final_memory:.1f}MB")
    report("Memory Delta", f"{memory_increase:+.1f}MB")
```

=== File: src\phicode_engine\benchsuite\bench_stress.φ (39 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the PhiCode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
← phicode_engine.core.transpilation.phicode_to_python ⇒ transpile_symbols
← phicode_engine.config.config ⇒ PYTHON_TO_PHICODE, CACHE_BATCH_SIZE
⇒ time
⇒ threading

ƒ report(name, result):
    π(f"{name}: {result}")

symbols = list(PYTHON_TO_PHICODE.values())
test_content = f"{symbols[0]} x {symbols[2]} range(50): {symbols[20]}(x) {symbols[6]} x % 2: ⟲ x * 2 {symbols[9]}: ⟲ x" * 20

results = []

ƒ worker():
    start = time.perf_counter()
    ∀ _ ∈ ⟪(CACHE_BATCH_SIZE):
        transpile_symbols(test_content)
    end = time.perf_counter()
    results.append(end - start)

thread_count = 4
threads = [threading.Thread(target=worker) ∀ _ ∈ ⟪(thread_count)]

start_time = time.perf_counter()
∀ t ∈ threads:
    t.start()
∀ t ∈ threads:
    t.join()
total_time = time.perf_counter() - start_time

avg_worker_time = ∑(results) / ℓ(results) ¿ results ⋄ 0
operations_per_sec = (thread_count * CACHE_BATCH_SIZE) / total_time ¿ total_time > 0 ⋄ 0

report("Concurrent Stress Test", f"{total_time:.2f}s total")
report("Average Worker Time", f"{avg_worker_time:.2f}s")
report("Operations Per Second", f"{operations_per_sec:.0f}")
```

=== File: src\phicode_engine\benchsuite\bench_symbol_density.φ (51 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the PhiCode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
⇒ time
⇒ statistics
⇒ gc

← phicode_engine.core.transpilation.phicode_to_python ⇒ SymbolTranspiler
← phicode_engine.benchsuite ⇒ report

transpiler = SymbolTranspiler()

ƒ run_timing_test(content: str, iterations: int = 5) -> dict:
    times = []
    transpiler.transpile(content)

    ∀ i ∈ ⟪(iterations):
        gc.collect()
        start_time = time.perf_counter()
        result = transpiler.transpile(content)
        end_time = time.perf_counter()
        times.append(end_time - start_time)

    chars_per_sec = [ℓ(content) / t ∀ t ∈ times]
    ⟲ {
        "content_size": ℓ(content),
        "avg_time_ms": statistics.mean(times) * 1000,
        "avg_chars_per_sec": statistics.mean(chars_per_sec),
    }

base_text = "x = 1\ny = 2\nz = x + y\n"
densities = [0, 10, 25, 50, 75, 100]

∀ density ∈ densities:
    ¿ density == 0:
        content = base_text * 1000
    ⋄:
        symbol_chars = int(ℓ(base_text) * density / 100)
        symbol_part = "∀ ∈ π ≡ ∧ ∨ ¬" * (symbol_chars // 7 + 1)
        content = (symbol_part[:symbol_chars] + base_text) * 100

    π(f"\nSymbol Density: {density}%")
    π(f"Content Size: {len(content):,} chars")

    result = run_timing_test(content)

    π(f"Speed: {result['avg_chars_per_sec']:,.0f} chars/sec")

    report(f"density_{density}_speed", f"{result['avg_chars_per_sec']:,.0f} chars/sec")
    report(f"density_{density}_size", f"{len(content):,} chars")
    report(f"density_{density}_efficiency", f"{result['avg_chars_per_sec'] / len(content) * 1000:.2f} speed/KB")
```

=== File: src\phicode_engine\benchsuite\bench_transpiler.φ (27 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the PhiCode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
← phicode_engine.core.transpilation.phicode_to_python ⇒ transpile_symbols
← phicode_engine.config.config ⇒ PYTHON_TO_PHICODE
⇒ time

ƒ generate_test_content(size):
    symbols = list(PYTHON_TO_PHICODE.values())[:10]
    base_content = ""
    ∀ symbol ∈ symbols:
        base_content += f"{symbol} x: π(x) "
    multiplier = ⭱(1, size // ℓ(base_content))
    ⟲ base_content * multiplier

ƒ report(name, result):
    π(f"{name}: {result}")

test_sizes = [1000, 10000, 100000]

∀ test_size ∈ test_sizes:
    test_content = generate_test_content(test_size)
    start = time.perf_counter()
    result = transpile_symbols(test_content)
    end = time.perf_counter()
    chars_per_sec = ℓ(test_content) / (end - start)
    report(f"Transpile {test_size} chars", f"{chars_per_sec:.0f} chars/sec")
```

=== File: src\phicode_engine\benchsuite\bench_transpiler_patterns.φ (107 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the PhiCode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
⇒ time
⇒ statistics
⇒ gc

← phicode_engine.core.transpilation.phicode_to_python ⇒ SymbolTranspiler
← phicode_engine.benchsuite ⇒ report

transpiler = SymbolTranspiler()

test_patterns = {
            "simple": "∀ x ∈ data: π(x)",
            "medium": """
∀ item ∈ items:
    ¿ item.is_valid() ∧ item.status == "active":
        π(f"Processing {item}")
        result = process_item(item)
        ¿ result ≡ ¬ Ø:
            π(f"Success: {result}")
        ⋄:
            π("Failed to process")
            """,
            "complex": """
# Complex phi code with many symbols
ƒ process_data(data):
    ∴:
        ∀ item ∈ data:
            ¿ item ≡ Ø ∨ ¬ item.is_valid():
                ⇉

            ¿ hasattr(item, 'value') ∧ item.value > 0:
                result = calculate_result(item)
                ¿ result ≡ ¬ Ø:
                    π(f"Item {item.id}: {result}")
                    yield_value = result * 2
                    ⟰ yield_value
                ⋄:
                    π("Calculation failed")

        ⟲ ✓
    ⛒ Exception ↦ e:
        π(f"Error: {e}")
        ↑ RuntimeError("Processing failed") ← e
    ⇗:
        π("Cleanup completed")

True_val = ✓
False_val = ⊥
None_val = Ø
            """,
            "heavy_symbols": "∀ ∈ ∧ ∨ ¬ ≡ ≢ ⇉ ⇲ ∴ ⛒ ⇗ ↑ ⟲ ⟰ π" * 50,
            "mixed_content": '''
"""
This == a string with ∀ symbols that should NOT be transpiled
"""
ƒ main():
    # This comment has ∀ symbols too
    data = "∀ x ∈ test"  # String literals protected
    for i in ⟪(10):  # This should be transpiled
        print(f"Value: {i}")
        ¿ i == 5:
            break  # ⇲
        ''',
}

ƒ run_timing_test(content: str, iterations: int = 5) -> dict:
    times = []
    transpiler.transpile(content)

    ∀ i ∈ ⟪(iterations):
        gc.collect()
        start_time = time.perf_counter()
        result = transpiler.transpile(content)
        end_time = time.perf_counter()
        times.append(end_time - start_time)

    chars_per_sec = [ℓ(content) / t ∀ t ∈ times]
    ⟲ {
        "content_size": ℓ(content),
        "avg_time_ms": statistics.mean(times) * 1000,
        "avg_chars_per_sec": statistics.mean(chars_per_sec),
    }

∀ name, pattern ∈ test_patterns.items():
    π(f"\nPattern: {name}")
    π(f"Size: {len(pattern):,} chars")

    result = run_timing_test(pattern, iterations=10)

    π(f"Average Time: {result['avg_time_ms']:.3f}ms")
    π(f"Average Speed: {result['avg_chars_per_sec']:,.0f} chars/sec")

    report(f"pattern_{name}_speed", f"{result['avg_chars_per_sec']:,.0f} chars/sec")
    report(f"pattern_{name}_time", f"{result['avg_time_ms']:.3f}ms")
    report(f"pattern_{name}_size", f"{len(pattern)} chars")

    ¿ result['avg_chars_per_sec'] >= 1_200_000:
        π("✅ Rust acceleration confirmed")
        report(f"pattern_{name}_status", "RUST_CONFIRMED")
    ⤷ result['avg_chars_per_sec'] >= 100_000:
        π("⚠️ Possible acceleration, below target")
        report(f"pattern_{name}_status", "POSSIBLE_ACCELERATION")
    ⋄:
        π("❌ Python fallback detected")
        report(f"pattern_{name}_status", "PYTHON_FALLBACK")
```

=== File: src\phicode_engine\benchsuite\bench_transpiler_scaling.φ (82 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the PhiCode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
⇒ time
⇒ statistics
⇒ gc

← phicode_engine.core.transpilation.phicode_to_python ⇒ SymbolTranspiler
← phicode_engine.benchsuite ⇒ report

transpiler = SymbolTranspiler()

base_pattern = """
ƒ process_data(data):
    ∴:
        ∀ item ∈ data:
            ¿ item ≡ Ø ∨ ¬ item.is_valid():
                ⇉
            ¿ hasattr(item, 'value') ∧ item.value > 0:
                result = calculate_result(item)
                ¿ result ≡ ¬ Ø:
                    ⟲ result * 2
        ⟲ ✓
    ⛒ Exception ↦ e:
        ↑ RuntimeError("Processing failed") ← e
    ⇗:
        π("Cleanup completed")
"""

ƒ generate_stress_content(base_pattern: str, target_size: int) -> str:
    content = ""
    ↻ ℓ(content) < target_size:
        content += base_pattern + "\n"
    ⟲ content[:target_size]

ƒ run_timing_test(content: str, iterations: int = 3) -> dict:
    times = []
    transpiler.transpile(content)

    ∀ i ∈ ⟪(iterations):
        gc.collect()
        start_time = time.perf_counter()
        result = transpiler.transpile(content)
        end_time = time.perf_counter()
        times.append(end_time - start_time)

    chars_per_sec = [ℓ(content) / t ∀ t ∈ times]
    ⟲ {
        "content_size": ℓ(content),
        "avg_time_ms": statistics.mean(times) * 1000,
        "avg_chars_per_sec": statistics.mean(chars_per_sec),
    }

sizes = [1_000, 10_000, 50_000, 100_000, 500_000, 1_000_000]
results = {}

∀ size ∈ sizes:
    π(f"\nTesting {size:,} chars...")
    content = generate_stress_content(base_pattern, size)

    result = run_timing_test(content)
    results[size] = result

    π(f"Time: {result['avg_time_ms']:.3f}ms")
    π(f"Speed: {result['avg_chars_per_sec']:,.0f} chars/sec")

    report(f"scale_{size}_speed", f"{result['avg_chars_per_sec']:,.0f} chars/sec")
    report(f"scale_{size}_time", f"{result['avg_time_ms']:.3f}ms")
    report(f"scale_{size}_throughput", f"{result['avg_chars_per_sec'] / 1000:.1f}K chars/sec")

    ¿ size > 1_000:
        prev_size = sizes[sizes.index(size) - 1]
        prev_speed = results[prev_size]["avg_chars_per_sec"]
        current_speed = result["avg_chars_per_sec"]
        degradation = (prev_speed - current_speed) / prev_speed * 100

        ¿ degradation > 20:
            π(f"⚠️ Performance degradation: {degradation:.1f}%")
            report(f"scale_{size}_degradation", f"{degradation:.1f}% degradation")
        ⋄:
            π(f"Performance stable: {degradation:+.1f}%")
            report(f"scale_{size}_stability", f"{degradation:+.1f}% change")
```

=== File: src\phicode_engine\benchsuite\system_info.py (67 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
import sys
import platform
from typing import Dict, Optional

def get_system_fingerprint() -> Dict[str, str]:
    try:
        import psutil
        memory_gb = round(psutil.virtual_memory().total / (1024**3), 1)
        cpu_count = psutil.cpu_count(logical=False)
        cpu_logical = psutil.cpu_count(logical=True)
    except ImportError:
        memory_gb = "unknown"
        cpu_count = "unknown"
        cpu_logical = "unknown"

    return {
        "os": f"{platform.system()} {platform.release()}",
        "python": f"{sys.implementation.name} {sys.version_info.major}.{sys.version_info.minor}",
        "cpu_physical": str(cpu_count),
        "cpu_logical": str(cpu_logical),
        "memory_gb": str(memory_gb),
        "arch": platform.machine()
    }

def get_performance_baseline() -> float:
    import time

    start = time.perf_counter()
    total = 0
    for i in range(100000):
        total += i * i
    end = time.perf_counter()

    baseline = 100000 / (end - start)
    return round(baseline, 0)

def normalize_result(raw_result: float, baseline: Optional[float] = None) -> float:
    if baseline is None:
        baseline = get_performance_baseline()

    reference_baseline = 1000000.0
    normalized = raw_result * (reference_baseline / baseline)
    return round(normalized, 2)

def format_system_report() -> str:
    info = get_system_fingerprint()
    baseline = get_performance_baseline()

    report = f"""System Information:
  OS: {info['os']}
  Python: {info['python']}
  CPU: {info['cpu_physical']} cores ({info['cpu_logical']} logical)
  Memory: {info['memory_gb']} GB
  Architecture: {info['arch']}
  Performance Baseline: {baseline:,.0f} ops/sec"""

    return report

def get_reproducibility_hash() -> str:
    import hashlib

    info = get_system_fingerprint()
    stable_info = f"{info['os']}-{info['python']}-{info['cpu_physical']}-{info['arch']}"
    return hashlib.md5(stable_info.encode()).hexdigest()[:8]
```

=== File: src\phicode_engine\benchsuite\__init__.py (28 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
import os
from phicode_engine.core.importing.phicode_importer import install_phicode_importer
from .benchmark_cli import run_benchmarks
from phicode_engine.core.phicode_logger import logger

install_phicode_importer(os.path.dirname(__file__))

def get_system_info():
    try:
        from .system_info import get_system_fingerprint
        return get_system_fingerprint()
    except ImportError:
        return {"error": "system_info module not available"}

def generate_performance_chart(results):
    try:
        from .benchmark_visualizer import generate_mermaid_performance_chart
        return generate_mermaid_performance_chart(results)
    except ImportError:
        return "benchmark_visualizer module not available"

def report(name: str, result):
    logger.info(f"📊 {name}: {result}")

__all__ = ["run_benchmarks", "get_system_info", "generate_performance_chart", "report"]
```

=== File: src\phicode_engine\benchsuite\simulation\simulate_concurrency.φ (81 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the PhiCode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
⇒ time
⇒ threading
← phicode_engine.core.transpilation.phicode_to_python ⇒ transpile_symbols
← phicode_engine.core.cache.phicode_cache ⇒ _cache
← phicode_engine.core.cache.phicode_bytecode ⇒ BytecodeManager, _flush_batch_writes
← phicode_engine.config.config ⇒ PYTHON_TO_PHICODE, MAIN_FILE_TYPE

symbols = list(PYTHON_TO_PHICODE.values())

test_code = f"""
def worker_function(worker_id):
    results = []
    for i in range(10):
        if i % 2 == 0:
            value = f"worker_{{worker_id}}_item_{{i}}"
            results.append(value)
    return results
"""

results = []
errors = []

ƒ worker_thread(worker_id):
    ∴:
        start = time.perf_counter()

        ∀ operation ∈ ⟪(50):
            cache_key = f"worker_{worker_id}_op_{operation}"

            transpiled = transpile_symbols(test_code)

            _cache.get_python_source(cache_key, test_code)

            BytecodeManager.compile_and_cache(transpiled, f"{cache_key}{MAIN_FILE_TYPE}")

        end = time.perf_counter()
        results.append((worker_id, end - start))

    ⛒ Exception ↦ e:
        errors.append((worker_id, str(e)))

thread_count = 8
threads = []

start_time = time.perf_counter()

∀ i ∈ ⟪(thread_count):
    t = threading.Thread(target=worker_thread, args=(i,))
    threads.append(t)
    t.start()

∀ t ∈ threads:
    t.join()

total_time = time.perf_counter() - start_time

_flush_batch_writes()

successful_workers = ℓ(results)
failed_workers = ℓ(errors)

¿ results:
    avg_worker_time = ∑(time ∀ _, time ∈ results) / ℓ(results)
    fastest_worker = ⭳(time ∀ _, time ∈ results)
    slowest_worker = ⭱(time ∀ _, time ∈ results)
⋄:
    avg_worker_time = fastest_worker = slowest_worker = 0

π(f"  Workers: {thread_count}")
π(f"  Successful: {successful_workers}")
π(f"  Failed: {failed_workers}")
π(f"  Total time: {total_time*1000:.1f}ms")
π(f"  Avg worker time: {avg_worker_time*1000:.1f}ms")
π(f"  Fastest worker: {fastest_worker*1000:.1f}ms")
π(f"  Slowest worker: {slowest_worker*1000:.1f}ms")

¿ errors:
    π(f"  Errors: {[f'Worker {w}: {e}' for w, e in errors[:3]]}")
```

=== File: src\phicode_engine\benchsuite\simulation\simulate_crash.φ (111 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the PhiCode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
⇒ time
⇒ threading
← phicode_engine.core.transpilation.phicode_to_python ⇒ transpile_symbols
← phicode_engine.core.cache.phicode_cache ⇒ _cache
← phicode_engine.core.cache.phicode_bytecode ⇒ BytecodeManager, _flush_batch_writes
← phicode_engine.config.config ⇒ MAIN_FILE_TYPE

crash_iterations = 1100 # sequential stress
cache_operations = 10000 # saturation test
worker_ops = 350
thread_count = 16 # * ops_multiplier = concurrent operations
ops_multiplier = 150
large_cache_ops = 10000 # cache growth test

test_code = """
def complex_operation(data):
    results = []
    for item in data:
        if item is not None and len(str(item)) > 0:
            try:
                processed = str(item).strip().lower()
                if processed in ['valid', 'active', 'processed', 'ready']:
                    for i in range(10):
                        nested_result = f"item_{item}_iteration_{i}"
                        results.append(nested_result)
                        if i % 3 == 0:
                            results.extend([f"extra_{j}" for j in range(5)])
                    return results
            except Exception as e:
                continue
        else:
            continue
    return results or ['default']
"""

start_time = time.perf_counter()

∀ i ∈ ⟪(crash_iterations):
    transpile_symbols(test_code)

transpiler_time = time.perf_counter() - start_time
π(f"    {crash_iterations} transpilations: {transpiler_time*1000:.1f}ms")
π(f"    Throughput: {len(test_code) * crash_iterations / transpiler_time:.0f} chars/sec")

start_time = time.perf_counter()

∀ i ∈ ⟪(cache_operations):
    cache_key = f"crash_test_{i}"
    _cache.get_python_source(cache_key, test_code)

cache_time = time.perf_counter() - start_time
π(f"    {cache_operations} cache ops: {cache_time*1000:.1f}ms")
π(f"    Ops/sec: {cache_operations / cache_time:.0f}")

results = []
errors = []

ƒ chaos_worker(worker_id):
    ∴:
        start = time.perf_counter()
        ∀ op ∈ ⟪(worker_ops):
            cache_key = f"chaos_{worker_id}_{op}"
            transpiled = transpile_symbols(test_code)
            _cache.get_python_source(cache_key, test_code)
            BytecodeManager.compile_and_cache(transpiled, f"{cache_key}{MAIN_FILE_TYPE}")

        end = time.perf_counter()
        results.append((worker_id, end - start))
    ⛒ Exception ↦ e:
        errors.append((worker_id, str(e)))

threads = []
chaos_start = time.perf_counter()

∀ i ∈ ⟪(thread_count):
    t = threading.Thread(target=chaos_worker, args=(i,))
    threads.append(t)
    t.start()

∀ t ∈ threads:
    t.join()

chaos_time = time.perf_counter() - chaos_start
_flush_batch_writes()

total_ops = thread_count * ops_multiplier
successful_workers = ℓ(results)
failed_workers = ℓ(errors)

π(f"    {thread_count} workers × {ops_multiplier} ops = {total_ops} total operations")
π(f"    Total time: {chaos_time*1000:.1f}ms")
π(f"    Successful workers: {successful_workers}")
π(f"    Failed workers: {failed_workers}")
π(f"    Ops/sec: {total_ops / chaos_time:.0f}")

¿ errors:
    π(f"    First 3 errors: {[f'Worker {w}: {str(e)[:50]}...' for w, e in errors[:3]]}")

memory_start = time.perf_counter()

∀ i ∈ ⟪(large_cache_ops):
    large_key = f"memory_pressure_{i}_{i*123}"
    large_code = test_code * (i % 5 + 1)
    _cache.get_python_source(large_key, large_code)

memory_time = time.perf_counter() - memory_start
π(f"    {large_cache_ops} large cache entries: {memory_time*1000:.1f}ms")
π(f"    Cache size: {len(_cache.python_cache)} entries")
```

=== File: src\phicode_engine\benchsuite\simulation\simulate_import_burst.φ (52 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the PhiCode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
⇒ time
⇒ sys
← phicode_engine.core.importing.phicode_importer ⇒ install_phicode_importer
← phicode_engine.core.importing.phicode_finder ⇒ PhicodeFinder

start = time.perf_counter()

test_paths = [f"/test/path_{i}" ∀ i ∈ ⟪(500)]

∀ path ∈ test_paths:
    install_phicode_importer(path)

registration_time = time.perf_counter() - start

phi_finders = [finder ∀ finder ∈ sys.meta_path ¿ isinstance(finder, PhicodeFinder)]

π(f"  Importer registrations: {len(test_paths)}")
π(f"  Registration time: {registration_time*1000:.1f}ms")
π(f"  Avg per registration: {registration_time*1000/len(test_paths):.2f}ms")
π(f"  PhicodeFinders ∈ meta_path: {len(phi_finders)}")

start = time.perf_counter()

∀ path ∈ test_paths[:10]:
    install_phicode_importer(path)

dedup_time = time.perf_counter() - start
phi_finders_after = [finder ∀ finder ∈ sys.meta_path ¿ isinstance(finder, PhicodeFinder)]

π(f"  Deduplication test: {dedup_time*1000:.1f}ms")
π(f"  Finders after dedup: {len(phi_finders_after)}")
π(f"  Deduplication working: {len(phi_finders_after) == len(phi_finders)}")

start = time.perf_counter()

test_modules = [f"nonexistent_module_{i}" ∀ i ∈ ⟪(1000)]

∀ module_name ∈ test_modules:
    ∀ finder ∈ phi_finders[:5]:
        ∴:
            finder.find_spec(module_name, Ø)
        ⛒:
            ⋯

lookup_time = time.perf_counter() - start

π(f"  Module lookups: {len(test_modules) * 5}")
π(f"  Lookup time: {lookup_time*1000:.1f}ms")
π(f"  Avg per lookup: {lookup_time*1000/(len(test_modules)*5):.2f}ms")
```

=== File: src\phicode_engine\benchsuite\simulation\simulate_phimmuno_threat.φ (99 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the PhiCode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
← phicode_engine.security.phimmuno_validator ⇒ is_content_safe
← phicode_engine.core.transpilation.phicode_to_python ⇒ transpile_symbols

ƒ report(name, result):
    π(f"{name}: {result}")

python_threats = [
    "eval('malicious')",
    "exec(user_input)",
    "subprocess.call(['rm', '-rf', '/'])",
    "os.system('dangerous command')",
    "__import__('subprocess').call(['evil'])",
    "getattr(__builtins__, 'exec')('code')",
    "compile(untrusted, '<string>', 'exec')",
    "globals()['eval']('payload')",
]

phi_threats = [
    "eval('bad_code')",
    "⇒ subprocess\nsubprocess.call(['rm'])",
    "⇒ os\nos.system('malware')",
    "__import__('eval')('code')",
]

python_blocked = 0
∀ i, threat ∈ №(python_threats):
    is_safe = is_content_safe(threat)
    status = "✅ Blocked" ¿ ¬ is_safe ⋄ "❌ Allowed"
    π(f"  Python #{i+1}: {status} - {threat[:30]}...")
    ¿ ¬ is_safe:
        python_blocked += 1

python_block_rate = (python_blocked / ℓ(python_threats)) * 100
report("Python threat block rate", f"{python_block_rate:.1f}%")

phi_blocked = 0
∀ i, phi_code ∈ №(phi_threats):
    ∴:
        transpiled = transpile_symbols(phi_code)
        is_safe = is_content_safe(transpiled)

        ¿ ¬ is_safe:
            status = "✅ Blocked after transpilation"
            phi_blocked += 1
        ⋄:
            status = "❌ Allowed after transpilation"

        π(f"  φ #{i+1}: {status}")
        π(f"    φ: {phi_code[:25]}...")
        π(f"    →: {transpiled[:25]}...")

    ⛒ Exception ↦ e:
        ¿ "Security" ∈ str(e):
            status = "✅ Blocked during transpilation"
            phi_blocked += 1
            π(f"  φ #{i+1}: {status}")
        ⋄:
            π(f"  φ #{i+1}: ❌ Error - {str(e)[:30]}...")

phi_block_rate = (phi_blocked / ℓ(phi_threats)) * 100 ¿ phi_threats ⋄ 100
report("φ transpilation block rate", f"{phi_block_rate:.1f}%")

engine_threats = [
    "← phicode_engine.core ⇒ *",
    "⇒ phicode_engine; phicode_engine.__file__",
    "__import__('phicode_engine.config.config')",
]

engine_blocked = 0
∀ i, threat ∈ №(engine_threats):
    is_safe = is_content_safe(threat)
    status = "✅ Blocked" ¿ ¬ is_safe ⋄ "⚠️ Allowed"
    π(f"  Engine #{i+1}: {status}")
    ¿ ¬ is_safe:
        engine_blocked += 1

engine_block_rate = (engine_blocked / ℓ(engine_threats)) * 100
report("Engine-specific block rate", f"{engine_block_rate:.1f}%")

total_threats = ℓ(python_threats) + ℓ(phi_threats) + ℓ(engine_threats)
total_blocked = python_blocked + phi_blocked + engine_blocked
overall_rate = (total_blocked / total_threats) * 100

π(f"  Direct Python: {python_blocked}/{len(python_threats)} blocked")
π(f"  φ Transpilation: {phi_blocked}/{len(phi_threats)} blocked")
π(f"  Engine-specific: {engine_blocked}/{len(engine_threats)} blocked")
report("Overall threat protection", f"{overall_rate:.1f}%")

¿ overall_rate >= 95:
    π("Excellent threat protection")
⤷ overall_rate >= 85:
    π("Good threat protection")
⤷ overall_rate >= 70:
    π("Moderate threat protection")
⋄:
    π("Insufficient threat protection")
```

=== File: src\phicode_engine\benchsuite\simulation\simulate_stress_transpiler.φ (65 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the PhiCode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
⇒ time
← phicode_engine.core.transpilation.phicode_to_python ⇒ transpile_symbols
← phicode_engine.config.config ⇒ PYTHON_TO_PHICODE

symbols = list(PYTHON_TO_PHICODE.values())

light_symbols = f"""
ƒ simple_func():
    ⟲ "hello world"
"""

medium_symbols = f"""
ƒ process_items(data):
    results = []
    ∀ item ∈ data:
        ¿ item ≡ ¬ Ø:
            ¿ isinstance(item, str):
                results.append(item.upper())
            ⋄:
                results.append(str(item))
    ⟲ results
"""

heavy_symbols = f"""
ƒ complex_workflow(items):
    ∀ item ∈ items:
        ¿ item ≡ ¬ Ø ∧ len(item) > 0:
            ∴:
                processed = item.strip().lower()
                ¿ processed ∈ ['valid', 'active']:
                    π(f"Processing: {{processed}}")
                    ⟲ processed
            ⛒ Exception ↦ e:
                π(f"Error: {{e}}")
                ⇉
        ⋄:
            ⇉
    ⟲ Ø
"""

test_cases = [
    ("Light symbols", light_symbols, 500),
    ("Medium symbols", medium_symbols, 300),
    ("Heavy symbols", heavy_symbols, 200)
]

∀ test_name, code, iterations ∈ test_cases:
    start = time.perf_counter()

    ∀ _ ∈ ⟪(iterations):
        result = transpile_symbols(code)

    end = time.perf_counter()
    total_time = end - start

    chars_processed = ℓ(code) * iterations
    throughput = chars_processed / total_time

    π(f"  {test_name}:")
    π(f"    Iterations: {iterations}")
    π(f"    Time: {total_time*1000:.1f}ms")
    π(f"    Throughput: {throughput:.0f} chars/sec")
```

=== File: src\phicode_engine\benchsuite\simulation\simulate_workload_cache.φ (47 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the PhiCode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
⇒ time
← phicode_engine.core.cache.phicode_cache ⇒ _cache
← phicode_engine.core.cache.phicode_bytecode ⇒ BytecodeManager, _flush_batch_writes
← phicode_engine.config.config ⇒ PYTHON_TO_PHICODE, MAIN_FILE_TYPE

symbols = list(PYTHON_TO_PHICODE.values())

patterns = [
    "def process_data(items):\n    return [x*2 for x in items]",
    "if condition:\n    print('executed')\nelse:\n    print('skipped')",
    "for i in range(10):\n    if i % 2:\n        print(i)",
    "def validate(data):\n    return data is not None and len(data) > 0"
]

start_time = time.perf_counter()
cache_hits = 0
cache_misses = 0

∀ file_id ∈ ⟪(100):
    ∀ pattern_id, pattern ∈ №(patterns):
        cache_key = f"file_{file_id}_pattern_{pattern_id}"

        initial_size = ℓ(_cache.python_cache)

        result = _cache.get_python_source(cache_key, pattern)

        BytecodeManager.compile_and_cache(result, f"{cache_key}{MAIN_FILE_TYPE}")

        ¿ ℓ(_cache.python_cache) > initial_size:
            cache_misses += 1
        ⋄:
            cache_hits += 1

_flush_batch_writes()

total_time = time.perf_counter() - start_time
total_ops = cache_hits + cache_misses
hit_rate = cache_hits / total_ops ¿ total_ops > 0 ⋄ 0

π(f"  Operations: {total_ops}")
π(f"  Cache hits: {cache_hits}")
π(f"  Hit rate: {hit_rate:.2f}")
π(f"  Total time: {total_time*1000:.1f}ms")
π(f"  Avg per op: {total_time*1000/total_ops:.1f}ms")
```

=== File: src\phicode_engine\config\config.py (133 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
import os

# Versioning
PHICODE_VERSION = '2.6.0'

PHIRUST_VERSION = '1.0.0'

PHIMMUNO_VERSION = "1.0.0"

#--- -  - -  - ---#
## IN-HOUSE DEPS ##
#---  --   --  ---#

PHIRUST_BINARY_NAME = "phirust-transpiler"
PHIMMUNO_BINARY_NAME = "phimmuno-engine"

PHIRUST_RELEASE_BASE = f"https://github.com/Varietyz/{PHIRUST_BINARY_NAME}/releases/download/v{PHIRUST_VERSION}"
PHIMMUNO_RELEASE_BASE = f"https://github.com/Varietyz/{PHIMMUNO_BINARY_NAME}/releases/download/v{PHIMMUNO_VERSION}"


#--- -  - -  - ---#
## MAIN SETTINGS ##
#---  --   --  ---#

# Branding
ENGINE_NAME = "Phicode"
API_NAME = "APHI"
RUST_NAME = "PhiRust"
SECURITY_NAME = "Phimmuno"
DAEMON_TOOL = "Phiemon"

# Branding Symbol(s)
SYMBOL = "φ"

# Branding Badge(s)
BADGE = f"({SYMBOL})" # (φ)

# Process Names
ENGINE = f"{BADGE} {ENGINE_NAME} Engine"
SERVER = f"{BADGE} {API_NAME} Server"
SCRIPT = f"{BADGE} {RUST_NAME}"
SECURITY = f"{BADGE} {SECURITY_NAME} Engine"

# File types
MAIN_FILE_TYPE = f".{SYMBOL}" # .φ
SECONDARY_FILE_TYPE = ".py"
TERTIARY_FILE_TYPE = ".phi"

# Config Location
CONFIG_FILE_TYPE = ".json"
CONFIG_FILE = f"config{CONFIG_FILE_TYPE}" # config.json

CUSTOM_FOLDER_PATH = f".{BADGE}/{CONFIG_FILE}"   # .(φ)/config.json
CUSTOM_FOLDER_PATH_2 = f".phicode/{CONFIG_FILE}"     # .phicode/config.json
BENCHMARK_FOLDER_PATH = f".{BADGE}/benchmark_results"  # .(φ)/benchmark

# Cache Location
COMPILE_FOLDER_NAME = f"com{SYMBOL}led"    # comφled

CACHE_PATH = f".{BADGE}cache"  # .(φ)cache
CACHE_FILE_TYPE = f"{MAIN_FILE_TYPE}ca"  # .φca


#---  --  ---#
## TWEAKING ##
#--- -  - ---#

# Cache Configuration
CACHE_MAX_SIZE = int(os.getenv('PHICODE_CACHE_SIZE', 512))
CACHE_MMAP_THRESHOLD = int(os.getenv('PHICODE_MMAP_THRESHOLD', 8 * 1024))
CACHE_BATCH_SIZE = int(os.getenv('PHICODE_BATCH_SIZE', 5))

# Buffer Sizes
POSIX_BUFFER_SIZE = 128 * 1024
WINDOWS_BUFFER_SIZE = 64 * 1024
CACHE_BUFFER_SIZE = POSIX_BUFFER_SIZE if os.name == 'posix' else WINDOWS_BUFFER_SIZE

# Retry Configuration
MAX_FILE_RETRIES = 3
RETRY_BASE_DELAY = 0.01

# Performance Thresholds
STARTUP_WARNING_MS = 150

# Validation Configuration
VALIDATION_ENABLED = os.getenv('PHICODE_VALIDATION', 'true').lower() == 'true'
STRICT_VALIDATION = os.getenv('PHICODE_STRICT', 'false').lower() == 'true'

# Env
IMPORT_ANALYSIS_ENABLED = os.getenv('PHICODE_IMPORT_ANALYSIS', 'true').lower() == 'true'

# Interpreter Override Configuration
INTERPRETER_PYTHON_PATH = os.getenv('PHITON_PATH')  # Custom Python for C extensions
INTERPRETER_PYPY_PATH = os.getenv('PHIPY_PATH', 'pypy3')  # Custom PyPy for pure Python

# Rust Transpiler Configuration
RUST_SIZE_THRESHOLD = 300000  # From here Rust outperforms Python consistently

#---  --  ---#
## LISTINGS ##
#--- -  - ---#

# Default C Extensions for Interpreter Selection
DEFAULT_C_EXTENSIONS = [
    'numpy', 'pandas', 'scipy', 'matplotlib', 'torch',
    'tensorflow', 'opencv-python', 'tracemalloc'
]

# Default Phicode Map
PYTHON_TO_PHICODE = {
    "False": "⊥", "None": "Ø", "True": "✓", "and": "∧", "as": "↦",
    "assert": "‼", "async": "⟳", "await": "⌛", "break": "⇲", "class": "ℂ",
    "continue": "⇉", "def": "ƒ", "del": "∂", "elif": "⤷", "else": "⋄",
    "except": "⛒", "finally": "⇗", "for": "∀", "from": "←", "global": "⟁",
    "if": "¿", "import": "⇒", "in": "∈", "is": "≡", "lambda": "λ",
    "nonlocal": "∇", "not": "¬", "or": "∨", "pass": "⋯", "raise": "↑",
    "return": "⟲", "try": "∴", "while": "↻", "with": "∥", "yield": "⟰",
    "print": "π", "match": "⟷", "case": "▷",
    "len": "ℓ", "range": "⟪", "enumerate": "№", "zip": "⨅",
    "sum": "∑", "max": "⭱", "min": "⭳", "abs": "∣",
    "type": "τ", "walrus": "≔"
}

# Finding Project Root
PROJECT_ROOT = [
    'pyproject.toml', 'setup.py', '.git', 'requirements.txt', '.env',
    '.φc', 'README.md', 'LICENSE', 'app', 'lib', 'tests', 'benchmark',
    'scripts', 'φ-src', 'φ-scripts', 'φ-files', 'φ-root', 'φ-branch',
    '.pypirc', 'docs', 'phicode', '.gitignore', '.vscode', '.idea'
]
```

=== File: src\phicode_engine\config\version.py (6 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
from .config import PHICODE_VERSION

__version__ = PHICODE_VERSION
```

=== File: src\phicode_engine\core\phicode_logger.py (12 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
import logging
from ..config.config import BADGE

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
formatter = logging.Formatter(BADGE + ' - '+'%(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)
```

=== File: src\phicode_engine\core\cache\phicode_bytecode.py (136 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
import importlib.util
import marshal
import os
import hashlib
import sys
from ..phicode_logger import logger
from ...config.config import CACHE_BATCH_SIZE, CACHE_PATH, CACHE_FILE_TYPE, COMPILE_FOLDER_NAME

try:
    import xxhash
    _HAS_XXHASH = True
except ImportError:
    _HAS_XXHASH = False

_pending_cache_writes = []

def _flush_batch_writes():
    global _pending_cache_writes
    if not _pending_cache_writes:
        return

    written_files = []
    try:
        for pyc_path, data in _pending_cache_writes:
            tmp_path = pyc_path + '.tmp'
            with open(tmp_path, 'wb', buffering=64*1024) as f:
                f.write(data)
                f.flush()
                written_files.append((tmp_path, pyc_path))

        if written_files:
            sync_file = written_files[0][0]
            try:
                with open(sync_file, 'r+b') as f:
                    os.fsync(f.fileno())
            except OSError as e:
                logger.warning(f"Sync failed for {sync_file}: {e}")

        for tmp_path, pyc_path in written_files:
            os.replace(tmp_path, pyc_path)

        _pending_cache_writes.clear()

    except OSError as e:
        logger.warning(f"Batch cache write failed: {e}")
        for tmp_path, _ in written_files:
            try:
                os.remove(tmp_path)
            except OSError:
                pass
        _pending_cache_writes.clear()

class BytecodeManager:
    @staticmethod
    def _fast_hash_path(path: str) -> str:
        path_bytes = path.encode('utf-8')
        return (xxhash.xxh64(path_bytes).hexdigest()[:16] if _HAS_XXHASH
                else hashlib.md5(path_bytes).hexdigest()[:16])

    @staticmethod
    def _get_pyc_path(path: str) -> str:
        safe_name = BytecodeManager._fast_hash_path(path)
        impl_name = sys.implementation.name
        version = f"{sys.version_info.major}{sys.version_info.minor}"
        cache_dir = os.path.join(os.getcwd(), CACHE_PATH, f'{COMPILE_FOLDER_NAME}_{impl_name}_{version}')
        os.makedirs(cache_dir, exist_ok=True)
        return os.path.join(cache_dir, f"{safe_name}" + CACHE_FILE_TYPE)

    @staticmethod
    def _is_pyc_valid(pyc_path: str, source_hash: bytes) -> bool:
        if not os.path.exists(pyc_path):
            return False
        try:
            with open(pyc_path, 'rb', buffering=32*1024) as f:
                header = f.read(16)
                if header[:4] != importlib.util.MAGIC_NUMBER:
                    return False
                flags = int.from_bytes(header[4:8], 'little')
                return header[8:16] == source_hash if flags & 0x01 else False
        except OSError:
            return False

    @staticmethod
    def _load_pyc(pyc_path: str):
        with open(pyc_path, 'rb', buffering=32*1024) as f:
            f.read(16)
            return marshal.load(f)

    @staticmethod
    def _queue_pyc_write(pyc_path: str, code, source_hash: bytes):
        global _pending_cache_writes

        try:
            data = bytearray()
            data += importlib.util.MAGIC_NUMBER
            data += (0x01).to_bytes(4, 'little')
            data += source_hash
            data += marshal.dumps(code)

            _pending_cache_writes.append((pyc_path, data))

            if len(_pending_cache_writes) >= CACHE_BATCH_SIZE:
                _flush_batch_writes()

        except Exception as e:
            logger.warning(f"Failed to queue bytecode cache: {e}")

    @classmethod
    def compile_and_cache(cls, python_source: str, path: str):
        pyc_path = cls._get_pyc_path(path)
        source_hash = hashlib.sha256(python_source.encode()).digest()[:8]

        if cls._is_pyc_valid(pyc_path, source_hash):
            try:
                from .phicode_cache import _cache
                if _cache._verify_cache_integrity(pyc_path):
                    return cls._load_pyc(pyc_path)
                else:
                    logger.warning(f"Cache integrity check failed for {pyc_path}, recompiling")
            except Exception as e:
                logger.warning(f"Failed to load cached bytecode, recompiling: {e}")

        try:
            import ast
            tree = ast.parse(python_source, filename=path)
            code = compile(tree, filename=path, mode='exec', optimize=2, dont_inherit=True)
            cls._queue_pyc_write(pyc_path, code, source_hash)
            return code
        except Exception as compile_error:
            logger.error(f"Compilation failed for {path}: {compile_error}")
            simple_code = compile(python_source, path, 'exec')
            logger.info(f"Executed {path} without cache optimization")
            return simple_code
```

=== File: src\phicode_engine\core\cache\phicode_cache.py (83 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
import os
import sys
from threading import RLock
from collections import OrderedDict
from typing import Optional, Tuple
from ..transpilation.phicode_to_python import transpile_symbols
from ...config.config import CACHE_PATH, CACHE_MAX_SIZE, IMPORT_ANALYSIS_ENABLED
from .phicode_cache_ops import CacheOperations
from .phicode_cache_validation import CacheValidation

class PhicodeCache(CacheOperations, CacheValidation):
    def __init__(self, cache_dir=CACHE_PATH):
        super().__init__()
        self.cache_dir = os.path.abspath(cache_dir)
        os.makedirs(self.cache_dir, exist_ok=True)
        self.source_cache = OrderedDict()
        self.python_cache = OrderedDict()
        self.spec_cache = OrderedDict()
        self._lock = RLock()
        self._canon_cache = {}
        self.interpreter_hints = OrderedDict()

    def _evict_if_needed(self, cache):
        if len(cache) > CACHE_MAX_SIZE:
            evict_count = min(CACHE_MAX_SIZE // 4, len(cache) - CACHE_MAX_SIZE + 64)
            for _ in range(evict_count):
                cache.popitem(last=False)

    def get_source(self, path: str) -> Optional[str]:
        with self._lock:
            if path in self.source_cache:
                self.source_cache.move_to_end(path)
                return self.source_cache[path]

            source = self._read_file(path)
            if source is not None:
                self.source_cache[path] = source
                self._evict_if_needed(self.source_cache)
            return source

    def get_python_source(self, path: str, phicode_source: str) -> str:
        cache_key = self._fast_hash(phicode_source)

        with self._lock:
            if cache_key in self.python_cache:
                self.python_cache.move_to_end(cache_key)
                return self.python_cache[cache_key]

            python_source = transpile_symbols(phicode_source)
            if IMPORT_ANALYSIS_ENABLED:
                optimal_interpreter = self._quick_interpreter_check(python_source)
                self.interpreter_hints[cache_key] = optimal_interpreter
                self._evict_if_needed(self.interpreter_hints)
            self.python_cache[cache_key] = python_source
            self._evict_if_needed(self.python_cache)
            return python_source

    def get_spec(self, key: Tuple[str, str]) -> Optional[object]:
        with self._lock:
            if key in self.spec_cache:
                self.spec_cache.move_to_end(key)
                return self.spec_cache[key]
            return None

    def set_spec(self, key: Tuple[str, str], value: object):
        with self._lock:
            self.spec_cache[key] = value
            self._evict_if_needed(self.spec_cache)

    def get_interpreter_hint(self, path: str, phicode_source: str) -> str:
        if not IMPORT_ANALYSIS_ENABLED:
            return sys.executable
        cache_key = self._fast_hash(phicode_source)
        with self._lock:
            if cache_key in self.interpreter_hints:
                self.interpreter_hints.move_to_end(cache_key)
                return self.interpreter_hints[cache_key]
        return sys.executable

_cache = PhicodeCache()
```

=== File: src\phicode_engine\core\cache\phicode_cache_ops.py (73 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
import os
import mmap
import hashlib
import time
import errno
from typing import Optional
from ..phicode_logger import logger
from ...config.config import CACHE_BUFFER_SIZE, CACHE_MMAP_THRESHOLD, MAX_FILE_RETRIES, RETRY_BASE_DELAY

try:
    import xxhash
    _HAS_XXHASH = True
except ImportError:
    _HAS_XXHASH = False

class CacheOperations:
    def __init__(self):
        pass

    def _canonicalize_path(self, path: str) -> str:
        if len(self._canon_cache) > 1000:
            self._canon_cache.clear()
        if path not in self._canon_cache:
            self._canon_cache[path] = os.path.realpath(path)
        return self._canon_cache[path]

    def _retry_file_op(self, operation):
        for attempt in range(MAX_FILE_RETRIES):
            try:
                return operation()
            except OSError as e:
                if e.errno in (errno.EBUSY, errno.EAGAIN) and attempt < MAX_FILE_RETRIES - 1:
                    delay = RETRY_BASE_DELAY * (2 ** attempt)
                    time.sleep(delay)
                    continue
                logger.warning(f"File operation failed after {attempt + 1} attempts: {e}")
                if attempt == MAX_FILE_RETRIES - 1:
                    return None
                raise

    def _read_file(self, path: str) -> Optional[str]:
        canon_path = self._canonicalize_path(path)

        def _do_read():
            try:
                file_size = os.path.getsize(canon_path)

                if file_size > CACHE_MMAP_THRESHOLD:
                    with open(canon_path, 'rb') as f:
                        try:
                            with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as mm:
                                return mm.read().decode('utf-8')
                        except (OSError, ValueError):
                            f.seek(0)
                            return f.read().decode('utf-8')
                else:
                    with open(canon_path, 'r', encoding='utf-8', buffering=CACHE_BUFFER_SIZE) as f:
                        return f.read()
            except OSError as e:
                logger.debug(f"File read failed {canon_path}: {e}")
                return None
            except UnicodeDecodeError as e:
                logger.warning(f"Encoding error {canon_path}: {e}")
                return None

        return self._retry_file_op(_do_read)

    def _fast_hash(self, data: str) -> str:
        data_bytes = data.encode('utf-8')
        return xxhash.xxh64(data_bytes).hexdigest() if _HAS_XXHASH else hashlib.md5(data_bytes).hexdigest()
```

=== File: src\phicode_engine\core\cache\phicode_cache_validation.py (38 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
import os
import importlib.util
import marshal
from ...config.config import INTERPRETER_PYPY_PATH, INTERPRETER_PYTHON_PATH, DEFAULT_C_EXTENSIONS

class CacheValidation:
    def _verify_cache_integrity(self, cache_path: str) -> bool:
        try:
            if not os.path.exists(cache_path):
                return False

            with open(cache_path, 'rb') as f:
                header = f.read(16)
                if len(header) < 16:
                    return False

                if header[:4] != importlib.util.MAGIC_NUMBER:
                    return False

                try:
                    f.seek(16)
                    marshal.load(f)
                    return True
                except (EOFError, ValueError, TypeError):
                    return False

        except (OSError, ValueError):
            return False

    def _quick_interpreter_check(self, python_source: str) -> str:
        c_extensions = DEFAULT_C_EXTENSIONS
        for ext in c_extensions:
            if f'import {ext}' in python_source or f'from {ext}' in python_source:
                return INTERPRETER_PYTHON_PATH or 'python3'
        return INTERPRETER_PYPY_PATH or 'pypy3'
```

=== File: src\phicode_engine\core\importing\phicode_central.py (52 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
import os
from .phicode_importer import install_phicode_importer
from ...config.config import PROJECT_ROOT, MAIN_FILE_TYPE

def install_project_wide_importer(project_root: str = None, recursive: bool = True):
    if project_root is None:
        project_root = os.getcwd()

    phi_directories = discover_phi_directories(project_root, recursive)

    for directory in phi_directories:
        install_phicode_importer(directory)

    return phi_directories

def discover_phi_directories(root_path: str, recursive: bool = True) -> list:
    phi_dirs = set()

    if recursive:
        for root, dirs, files in os.walk(root_path):
            if any(f.endswith(MAIN_FILE_TYPE) for f in files):
                phi_dirs.add(root)
    else:
        try:
            if any(entry.is_file() and entry.name.endswith(MAIN_FILE_TYPE)
                for entry in os.scandir(root_path)):
                phi_dirs.add(root_path)
        except OSError:
            pass

    return sorted(list(phi_dirs))

def auto_install_on_import():
    try:
        current = os.getcwd()
        markers = PROJECT_ROOT

        project_root = current
        for root, dirs, files in os.walk(current):
            if any(marker in files or marker in dirs for marker in markers):
                project_root = root
                break

        install_project_wide_importer(project_root)

    except Exception:
        install_phicode_importer(os.getcwd())

auto_install_on_import()
```

=== File: src\phicode_engine\core\importing\phicode_finder.py (108 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
import importlib.abc
import importlib.util
import importlib.machinery
import os
import sys
from functools import lru_cache
from typing import Optional, Tuple
from ..cache.phicode_cache import _cache
from ..runtime.phicode_loader import PhicodeLoader
from ...config.config import MAIN_FILE_TYPE, TERTIARY_FILE_TYPE, SECONDARY_FILE_TYPE

try:
    from ..runtime.phicode_loader import _flush_batch_writes
except ImportError:
    def _flush_batch_writes(): pass

class PhicodeFinder(importlib.abc.MetaPathFinder):
    __slots__ = ('base_path', '_canon_base_path')

    def __init__(self, base_path: str):
        self.base_path = os.path.abspath(base_path)
        self._canon_base_path = os.path.realpath(self.base_path)

    def _is_stdlib_module(self, fullname: str) -> bool:
        if fullname in sys.builtin_module_names:
            return True
        try:
            spec = importlib.machinery.PathFinder.find_spec(fullname)
            if spec and spec.origin:
                return any(path in spec.origin for path in [
                    'site-packages', 'dist-packages', 'lib/python', 'Lib\\',
                    sys.prefix, sys.base_prefix
                ])
        except (ImportError, ValueError, TypeError):
            pass
        return False

    @lru_cache(maxsize=256)
    def _get_file_path(self, fullname: str) -> Optional[str]:
        parts = fullname.split('.')
        base = os.path.join(self._canon_base_path, *parts)
        for ext in [MAIN_FILE_TYPE, TERTIARY_FILE_TYPE, SECONDARY_FILE_TYPE]:
            candidate = base + ext
            try:
                if os.path.isfile(candidate):
                    return candidate
            except OSError:
                continue
        return None

    @lru_cache(maxsize=256)
    def _get_package_paths(self, fullname: str) -> Optional[Tuple[str, str]]:
        parts = fullname.split('.')
        package_dir = os.path.join(self._canon_base_path, *parts)
        for ext in [MAIN_FILE_TYPE, TERTIARY_FILE_TYPE, SECONDARY_FILE_TYPE]:
            init_file = os.path.join(package_dir, '__init__' + ext)
            if os.path.isfile(init_file):
                return package_dir, init_file
        return None

    def find_spec(self, fullname: str, path, target=None):
        if self._is_stdlib_module(fullname):
            return None

        cache_key = (fullname, self._canon_base_path)
        cached = _cache.get_spec(cache_key)

        if cached:
            spec, cached_mtime = cached
            try:
                if os.path.getmtime(spec.origin) == cached_mtime:
                    return spec
            except OSError:
                _cache.set_spec(cache_key, None)

        filename = self._get_file_path(fullname)
        if filename:
            loader = PhicodeLoader(filename) if filename.endswith((MAIN_FILE_TYPE, TERTIARY_FILE_TYPE)) else None
            spec = importlib.util.spec_from_file_location(
                fullname, filename, loader=loader,
                submodule_search_locations=[os.path.dirname(filename)] if os.path.isdir(filename) else None
            )
            try:
                _cache.set_spec(cache_key, (spec, os.path.getmtime(filename)))
            except OSError:
                pass
            return spec

        package_result = self._get_package_paths(fullname)
        if package_result:
            package_dir, init_file = package_result
            loader = PhicodeLoader(init_file) if init_file.endswith((MAIN_FILE_TYPE, TERTIARY_FILE_TYPE)) else None
            spec = importlib.util.spec_from_file_location(
                fullname, init_file, loader=loader, submodule_search_locations=[package_dir]
            )
            try:
                _cache.set_spec(cache_key, (spec, os.path.getmtime(init_file)))
            except OSError:
                pass
            return spec

        return None

    def __del__(self):
        _flush_batch_writes()
```

=== File: src\phicode_engine\core\importing\phicode_importer.py (18 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
import sys
import os
from .phicode_finder import PhicodeFinder

def install_phicode_importer(base_path: str):
    base_path = os.path.abspath(base_path)

    for finder in sys.meta_path:
        if (isinstance(finder, PhicodeFinder) and
            hasattr(finder, 'base_path') and
            finder.base_path == base_path):
            return

    finder = PhicodeFinder(base_path)
    sys.meta_path.insert(0, finder)
```

=== File: src\phicode_engine\core\interpreter\phicode_args.py (57 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
import sys
import contextlib
from dataclasses import dataclass, field
from typing import List, Optional

@contextlib.contextmanager
def _argv_context(target_argv: List[str]):
    original = sys.argv
    try:
        sys.argv = target_argv
        yield
    finally:
        sys.argv = original

@dataclass
class PhicodeArgs:
    module_or_file: str = "main"
    debug: bool = False
    bypass: bool = False
    remaining_args: List[str] = field(default_factory=list)
    interpreter: Optional[str] = None
    list_interpreters: bool = False
    show_versions: bool = False
    version: bool = False
    benchmark: bool = False
    _original_argv: List[str] = field(default_factory=list)

    def __post_init__(self):
        if not self._original_argv:
            self._original_argv = sys.argv.copy()

    @property
    def should_exit_early(self) -> bool:
        return any([self.version, self.list_interpreters, self.interpreter, self.benchmark and not self.module_or_file])

    def get_module_argv(self) -> List[str]:
        return ['__main__'] + self.remaining_args

_current_args: Optional[PhicodeArgs] = None
_is_switched_execution = False

def get_current_args() -> Optional[PhicodeArgs]:
    return _current_args

def is_switched_execution() -> bool:
    return _is_switched_execution

def _set_current_args(args: PhicodeArgs):
    global _current_args
    _current_args = args

def _set_switched_execution(switched: bool):
    global _is_switched_execution
    _is_switched_execution = switched
```

=== File: src\phicode_engine\core\interpreter\phicode_executor.py (45 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
from ..phicode_logger import logger

class ModuleExecutor:
    @staticmethod
    def execute_module(module, code, should_be_main: bool):
        if should_be_main:
            module.__dict__['__name__'] = "__main__"

            from .phicode_args import get_current_args, _argv_context
            current_args = get_current_args()

            if current_args:
                with _argv_context(current_args.get_module_argv()):
                    ModuleExecutor._execute_code(module, code)
            else:
                ModuleExecutor._execute_code(module, code)
        else:
            ModuleExecutor._execute_code(module, code)

    @staticmethod
    def _execute_code(module, code):
        try:
            exec(code, module.__dict__)
        except ImportError:
            try:
                import importlib.util
                importlib.util.find_spec(module.__name__)
            except ModuleNotFoundError as error:
                logger.error(f"⛔ Module {module.__name__} not found or contains a typo: {error}")
                raise
            try:
                if "python" not in __import__('sys').implementation.name.lower():
                    from .phicode_switch import InterpreterSwitcher
                    logger.warning(f"⚠️ Import of {module.__name__} failed under {__import__('sys').implementation.name}",
                                    "🔬 Attempting to switch to a Python interpreter")
                    if InterpreterSwitcher.attempt_switch("python3", module.__name__):
                        return
            except Exception as final_error:
                logger.error(f"⛔ Interpreter switch failed for {module.__name__}: {final_error}",
                            "🔍 Please verify your environment setup or try a different interpreter.",
                            f"🛠️ Current interpreter: {__import__('sys').implementation.name}. Ensure compatibility with Phicode.")
            raise
```

=== File: src\phicode_engine\core\interpreter\phicode_exit_handlers.py (25 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
import sys
from .phicode_args import PhicodeArgs
from .phicode_interpreter_display import print_interpreters, show_interpreter_info
from ...config.config import ENGINE, PHICODE_VERSION
from ..phicode_logger import logger


def handle_early_exit_flags(args: PhicodeArgs) -> bool:
    if args.version:
        logger.info(f"{ENGINE} version {PHICODE_VERSION}")
        logger.info(f"Running on: {sys.implementation.name} {sys.version}")
        return True

    if args.list_interpreters:
        print_interpreters(args.show_versions)
        return True

    if args.interpreter:
        show_interpreter_info(args.interpreter)
        return True

    return False
```

=== File: src\phicode_engine\core\interpreter\phicode_interpreter.py (85 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
import sys
import shutil
import subprocess
from functools import lru_cache
from typing import Optional, List

class InterpreterSelector:
    def __init__(self):
        self.current_interpreter = sys.executable
        self.current_impl = sys.implementation.name

    def find_available_interpreters(self) -> List[str]:
        candidates = ["pypy3", "pypy", "python3", "python", sys.executable]

        available = []
        for candidate in candidates:
            full_path = shutil.which(candidate)
            if full_path:
                available.append(full_path)

        return list(dict.fromkeys(available))

    @lru_cache(maxsize=32)
    def get_interpreter_version(self, interpreter: str) -> Optional[str]:
        try:
            result = subprocess.run(
                [interpreter, "-c", 'import sys; print(f"{sys.implementation.name}-{sys.version_info.major}.{sys.version_info.minor}")'],
                capture_output=True,
                text=True,
                timeout=5,
            )
            if result.returncode == 0 and result.stdout:
                return result.stdout.strip()
            return None
        except (subprocess.TimeoutExpired, FileNotFoundError, OSError):
            return None

    def is_pypy(self, interpreter: str) -> bool:
        version = self.get_interpreter_version(interpreter)
        return version is not None and "pypy" in version.lower()

    def get_interpreter_path(self, interpreter_name: str) -> Optional[str]:
        return shutil.which(interpreter_name)

    def get_current_info(self) -> dict:
        return {
            "path": self.current_interpreter,
            "implementation": self.current_impl,
            "version": f"{sys.version_info.major}.{sys.version_info.minor}",
            "is_pypy": self.current_impl == "pypy",
            "full_version": sys.version
        }

    def get_recommended_interpreter(self) -> Optional[str]:
        available = self.find_available_interpreters()

        for interp in available:
            if self.is_pypy(interp):
                return interp

        return available[0] if available else None

    def get_usage_instructions(self) -> List[str]:
        instructions = []
        available = self.find_available_interpreters()

        pypy_found = any(self.is_pypy(interp) for interp in available)

        if pypy_found:
            instructions.append("For optimal performance:")
            instructions.append("  pypy3 -m phicode <module>")
            instructions.append("")

        instructions.append("For CPython:")
        instructions.append("  python -m phicode <module>")

        if not pypy_found:
            instructions.append("")
            instructions.append("Install PyPy for faster symbolic processing:")
            instructions.append("   pip install pypy3")

        return instructions
```

=== File: src\phicode_engine\core\interpreter\phicode_interpreter_display.py (57 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
import sys
from ..phicode_logger import logger


def print_interpreters(show_versions=False):
    from .phicode_interpreter import InterpreterSelector

    selector = InterpreterSelector()
    available = selector.find_available_interpreters()
    current = sys.executable

    info = {}
    for interp in available:
        version = selector.get_interpreter_version(interp) if show_versions else "unknown"
        info[interp] = {"version": version, "is_pypy": selector.is_pypy(interp)}

    available.sort(key=lambda i: (i != current, not info[i]['is_pypy'], i.lower()))

    logger.info("Available Python Interpreters:")
    logger.info("-" * 50)
    for interp in available:
        data = info[interp]
        star = "⭐" if interp == current else "  "
        icon = "🚀" if data["is_pypy"] else "🔍"
        version_text = f"({data['version']})" if show_versions else ""
        hint = " ← Currently running" if interp == current else ""
        logger.info(f"{star} {icon} {interp:15s} {version_text}{hint}")

    logger.info("\n💡 Usage:")
    logger.info("   pypy3 -m phicode_engine <module>   # PyPy")
    logger.info("   python -m phicode_engine <module>  # CPython")


def show_interpreter_info(name: str):
    from .phicode_interpreter import InterpreterSelector

    selector = InterpreterSelector()
    path = selector.get_interpreter_path(name)

    if not path:
        logger.error(f"Interpreter '{name}' not found")
        return

    version = selector.get_interpreter_version(path)
    is_pypy = selector.is_pypy(path)

    logger.info(f"\nInterpreter Info:")
    logger.info(f"  Name: {name}")
    logger.info(f"  Path: {path}")
    logger.info(f"  Version: {version or 'unknown'}")
    logger.info(f"  Type: {'PyPy 🚀' if is_pypy else 'CPython 🔍'}")

    if not is_pypy:
        logger.info(f"  💡 Usage: {name} -m phicode_engine <module>")
```

=== File: src\phicode_engine\core\interpreter\phicode_switch.py (68 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
import os
import sys
import shutil
import subprocess
from ..phicode_logger import logger

class InterpreterSwitcher:
    @staticmethod
    def attempt_switch(optimal_interpreter: str, original_module_name: str):
        if optimal_interpreter == sys.executable:
            logger.debug(f"✅ Already using optimal interpreter: {optimal_interpreter}")
            return False

        env_switched = os.environ.get('PHICODE_ALREADY_SWITCHED', '0') == '1'
        if env_switched:
            logger.debug(f"🔄 Switch already attempted, staying with: {sys.executable}")
            return False

        if os.path.sep not in optimal_interpreter:
            interpreter_path = shutil.which(optimal_interpreter)
            if not interpreter_path:
                logger.warning(f"🛑 Interpreter not found: {optimal_interpreter}")
                return False
        else:
            interpreter_path = optimal_interpreter
            if not os.path.isfile(interpreter_path):
                logger.warning(f"🚫 Interpreter path invalid: {interpreter_path}")
                return False

        try:
            from ..cache.phicode_bytecode import _flush_batch_writes
            _flush_batch_writes()

            try:
                from .phicode_args import get_current_args
                current_args = get_current_args()
                target_args = current_args.remaining_args if current_args else []
            except Exception:
                target_args = []

            original_argv = sys.argv.copy()

            cmd_parts = [interpreter_path]

            if original_argv[0] == sys.executable:
                cmd_parts.extend(original_argv[1:])
            else:
                cmd_parts.extend(['-m', 'phicode_engine'])
                cmd_parts.extend(original_argv[1:])

            logger.debug(f"⚡ Interpreter switch command: {cmd_parts}")
            logger.info(f"🔄 Switching to optimal interpreter: {optimal_interpreter}")

            env = os.environ.copy()
            env['PHICODE_ALREADY_SWITCHED'] = '1'

            result = subprocess.run(cmd_parts, cwd=os.getcwd(), env=env)
            sys.exit(result.returncode)

        except Exception as e:
            logger.warning(f"⚠️ Failed to switch to {interpreter_path}: {e}")
            logger.info("👟 Continuing with current interpreter")
            return False

        return True
```

=== File: src\phicode_engine\core\interpreter\cli\phicode_cli.py (92 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
import sys
from typing import List, Optional
from .phicode_cli_parser import build_parser
from .phicode_cli_handlers import (
    handle_security_install, handle_security_status,
    handle_benchmark, handle_api_server,
    handle_config_generate, handle_config_reset
)
from ..phicode_args import PhicodeArgs, _set_current_args, _set_switched_execution
from ...phicode_logger import logger

def parse_args(argv: Optional[List[str]] = None) -> PhicodeArgs:
    if argv is None:
        argv = sys.argv[1:]

    if any(arg.startswith("--phimmuno") for arg in argv):
        try:
            from ....security.phimmuno_cli import handle_phimmuno_commands
            handle_phimmuno_commands(argv)
        except ImportError:
            logger.error("Phimmuno module not available")
        sys.exit(0)

    if any(arg.startswith("--phirust") for arg in argv):
        try:
            from ....rust.phirust_cli import handle_rust_commands
            handle_rust_commands(argv)
        except ImportError:
            logger.error("Rust module not available")
        sys.exit(0)

    if "--security-install" in argv:
        handle_security_install()

    if "--security-status" in argv:
        handle_security_status()

    if "--benchmark" in argv:
        handle_benchmark(argv)

    if "--api-server" in argv:
        handle_api_server(argv)

    if "--config-generate" in argv:
        handle_config_generate()

    if "--config-reset" in argv:
        handle_config_reset()

    if "--interpreter-switch" in argv:
        _set_switched_execution(True)
        idx = argv.index("--interpreter-switch")
        del argv[idx]
        if idx < len(argv) and not argv[idx].startswith("-"):
            module_name = argv[idx]
            del argv[idx]
        else:
            module_name = "main"
        remaining = argv[:]
        bypass = "--bypass" in remaining
        args = PhicodeArgs(
            module_or_file=module_name,
            debug=False,
            bypass=bypass,
            remaining_args=remaining,
            interpreter=None,
            list_interpreters=False,
            show_versions=False,
            version=False
        )
        _set_current_args(args)
        return args

    parser = build_parser()
    parsed = parser.parse_args(argv)

    args = PhicodeArgs(
        module_or_file=parsed.module_or_file,
        debug=parsed.debug,
        bypass=parsed.bypass,
        remaining_args=argv,
        interpreter=parsed.interpreter,
        list_interpreters=parsed.list_interpreters,
        show_versions=parsed.show_versions,
        version=parsed.version,
    )

    _set_current_args(args)
    return args
```

=== File: src\phicode_engine\core\interpreter\cli\phicode_cli_handlers.py (107 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
import sys
import os
from ...phicode_logger import logger
from ....config.config import SECURITY_NAME, RUST_NAME, DAEMON_TOOL

def handle_security_install():
    try:
        from ....installers.phirust_installer import install_phirust_binary
        from ....installers.phimmuno_installer import install_phimmuno_binary
        install_phirust_binary()
        install_phimmuno_binary()
        logger.info("🔒 Security binaries installed successfully")
    except ImportError:
        logger.error("Security installer not available")
    except Exception as e:
        logger.error(f"Security installation failed: {e}")
    sys.exit(0)

def handle_security_status():
    try:
        from ....installers.phirust_installer import get_binary_path as get_phirust_path
        from ....installers.phimmuno_installer import get_binary_path as get_phimmuno_path

        phirust_installed = os.path.exists(get_phirust_path())
        phimmuno_installed = os.path.exists(get_phimmuno_path())

        logger.info("🔒 Security Status:")
        logger.info(f"  {RUST_NAME} Transpiler: {'✅ Installed' if phirust_installed else '❌ Not installed'}")
        logger.info(f"  {SECURITY_NAME} Engine: {'✅ Installed' if phimmuno_installed else '❌ Not installed'}")

        if phirust_installed and phimmuno_installed:
            logger.info("🛡️ Full security suite available")
        else:
            logger.info("💡 Run: phicode --security-install")
    except ImportError:
        logger.error("Security status checker not available")
    sys.exit(0)

def handle_benchmark(argv):
    try:
        from ....benchsuite import run_benchmarks
        original_argv = sys.argv
        sys.argv = ['phicode'] + argv
        try:
            run_benchmarks()
        finally:
            sys.argv = original_argv
    except ImportError:
        logger.error("Benchsuite module not available")
    sys.exit(0)

def handle_api_server(argv):
    try:
        port_idx = argv.index("--api-port") + 1 if "--api-port" in argv else None
        api_port = int(argv[port_idx]) if port_idx and port_idx < len(argv) else 8000
    except (ValueError, IndexError):
        api_port = 8000

    from ....api.cli import main as api_main
    sys.argv = ['phicode-api', '--port', str(api_port)]
    api_main()
    sys.exit(0)

def handle_config_generate():
    from ...mod.phicode_config_generator import generate_default_config
    generate_default_config()
    logger.info("Default configuration generated")
    logger.info("💡 Edit the config file to customize symbols and settings")
    sys.exit(0)

def handle_config_reset():
    from ...mod.phicode_config_generator import reset_config
    if reset_config():
        logger.info("Configuration reset successfully")
    else:
        logger.info("No configuration to reset")
    sys.exit(0)

def handle_daemon_start(argv):
    script = argv[argv.index("--phiemon") + 1] if len(argv) > argv.index("--phiemon") + 1 else "main"
    name = None
    max_restarts = 5

    if "--name" in argv:
        name = argv[argv.index("--name") + 1]
    if "--max-restarts" in argv:
        max_restarts = int(argv[argv.index("--max-restarts") + 1])

    from ...runtime.phicode_daemon import start_daemon
    start_daemon(script, name, max_restarts)
    sys.exit(0)

def handle_daemon_status():
    from ...runtime.phicode_daemon import get_daemon_status

    status = get_daemon_status()
    if status:
        logger.info(f"{DAEMON_TOOL}: {status['name']}")
        logger.info(f"Script: {status['script']}")
        logger.info(f"Restarts: {status['restarts']}/{status['max_restarts']}")
        logger.info(f"Uptime: {status['uptime']:.0f}s")
    else:
        logger.info(f"No {DAEMON_TOOL} running")
    sys.exit(0)
```

=== File: src\phicode_engine\core\interpreter\cli\phicode_cli_parser.py (39 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
import argparse
from ....config.config import ENGINE, SERVER, DAEMON_TOOL

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=f"{ENGINE}")

    parser.add_argument("module_or_file", nargs="?", default="main")
    parser.add_argument("--debug", action="store_true")
    parser.add_argument("--bypass", action="store_true", help="Bypass security checks")
    parser.add_argument("--version", action="store_true")
    parser.add_argument("--list-interpreters", action="store_true")
    parser.add_argument("--show-versions", action="store_true")

    parser.add_argument("--config-generate", action="store_true", help="Generate default configuration")
    parser.add_argument("--config-reset", action="store_true", help="Reset configuration")

    parser.add_argument("--api-server", action="store_true", help=f"Start local {SERVER}")
    parser.add_argument("--api-port", type=int, default=8000, help=f"{SERVER} port")

    parser.add_argument("--security-install", action="store_true", help="Install security binaries")
    parser.add_argument("--security-status", action="store_true", help="Check security binary status")

    parser.add_argument("--benchmark", action="store_true", help="Engine Benchmark suite")

    parser.add_argument("--phiemon", help=f"Start as {DAEMON_TOOL} process")
    parser.add_argument("--phiemon-status", action="store_true", help=f"Show {DAEMON_TOOL} status")
    parser.add_argument("--name", help=f"Process name for {DAEMON_TOOL}")
    parser.add_argument("--max-restarts", type=int, default=5, help="Max restart attempts")

    interp_group = parser.add_mutually_exclusive_group()
    interp_group.add_argument("--interpreter")
    interp_group.add_argument("--python", action="store_const", const="python", dest="interpreter")
    interp_group.add_argument("--pypy", action="store_const", const="pypy3", dest="interpreter")
    interp_group.add_argument("--cpython", action="store_const", const="python3", dest="interpreter")

    return parser
```

=== File: src\phicode_engine\core\mod\phicode_config_generator.py (35 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
import os
import json
from ...config.config import CUSTOM_FOLDER_PATH, SYMBOL, PYTHON_TO_PHICODE
from ..phicode_logger import logger


def generate_default_config():
    default_symbols = {python_kw: symbol for python_kw, symbol in PYTHON_TO_PHICODE.items()}

    config = {
        "file_extension": f".{SYMBOL}",
        "symbols": default_symbols,
    }

    config_dir = os.path.dirname(CUSTOM_FOLDER_PATH)
    os.makedirs(config_dir, exist_ok=True)

    with open(CUSTOM_FOLDER_PATH, 'w', encoding='utf-8') as f:
        json.dump(config, f, indent=2, ensure_ascii=False)

    logger.info(f"Configuration generated: {CUSTOM_FOLDER_PATH}")
    return CUSTOM_FOLDER_PATH


def reset_config():
    if os.path.exists(CUSTOM_FOLDER_PATH):
        os.remove(CUSTOM_FOLDER_PATH)
        logger.info(f"Configuration reset: {CUSTOM_FOLDER_PATH}")
        return True
    else:
        logger.info("No configuration file to reset")
        return False
```

=== File: src\phicode_engine\core\runtime\phicode_loader.py (56 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
import importlib.abc
import os
from ..cache.phicode_cache import _cache
from ..phicode_logger import logger
from ..cache.phicode_bytecode import BytecodeManager
from ..interpreter.phicode_executor import ModuleExecutor
from ..interpreter.phicode_switch import InterpreterSwitcher
from ...config.config import ENGINE, IMPORT_ANALYSIS_ENABLED

_switch_executed = False
_original_module_name = None
_main_module_name = None

class PhicodeLoader(importlib.abc.Loader):
    __slots__ = ('path',)

    def __init__(self, path: str):
        self.path = path

    def create_module(self, spec):
        return None

    def exec_module(self, module):
        global _switch_executed, _original_module_name
        phicode_source = _cache.get_source(self.path)
        if phicode_source is None:
            logger.error(f"Failed to read: {self.path}")
            raise ImportError(f"Cannot read {self.path}")

        try:
            python_source = _cache.get_python_source(self.path, phicode_source)

            if IMPORT_ANALYSIS_ENABLED and not _switch_executed:
                optimal_interpreter = _cache.get_interpreter_hint(self.path, phicode_source)
                if optimal_interpreter != __import__('sys').executable:
                    _original_module_name = os.path.abspath(self.path)
                    _switch_executed = True
                    if InterpreterSwitcher.attempt_switch(optimal_interpreter, _original_module_name):
                        return

            module_name = getattr(module, '__name__', '')
            should_be_main = (module_name == (_original_module_name or _main_module_name) and
                            (_original_module_name or _main_module_name) is not None)

            code = BytecodeManager.compile_and_cache(python_source, self.path)
            ModuleExecutor.execute_module(module, code, should_be_main)

        except SyntaxError as e:
            logger.error(f"Syntax error in {self.path} at line {e.lineno}: {e.msg}")
            raise SyntaxError(f"{ENGINE} syntax error in {self.path}: {e}") from e

    def _get_module_name(self):
        return os.path.splitext(os.path.basename(self.path))[0]
```

=== File: src\phicode_engine\core\runtime\phicode_runtime.py (131 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
import sys
import os
import time
import traceback
import importlib
from ..importing.phicode_importer import install_phicode_importer
from .shutdown_handler import install_shutdown_handler, register_cleanup, cleanup_cache_temp_files
from ..interpreter.phicode_interpreter import InterpreterSelector
from ..phicode_logger import logger
from ..cache.phicode_bytecode import _flush_batch_writes
from ..interpreter.phicode_args import PhicodeArgs, _argv_context
from ...config.config import STARTUP_WARNING_MS, ENGINE_NAME, MAIN_FILE_TYPE, SECONDARY_FILE_TYPE, TERTIARY_FILE_TYPE

def run(args: PhicodeArgs):
    start_time = time.perf_counter()

    is_switched = os.environ.get('PHICODE_ALREADY_SWITCHED', '0') == '1'
    if not is_switched:
        _show_interpreter_recommendations()

    install_shutdown_handler()
    register_cleanup(cleanup_cache_temp_files)
    register_cleanup(_flush_batch_writes)

    module_name, phicode_src_folder, is_phicode_file = _resolve_module(args.module_or_file)
    phicode_src_folder = os.path.realpath(phicode_src_folder)

    if not os.path.isdir(phicode_src_folder):
        logger.error(f"Source folder not found: {phicode_src_folder}")
        sys.exit(2)

    install_phicode_importer(phicode_src_folder)
    logger.debug(f"{ENGINE_NAME} importer ready for: {phicode_src_folder}")

    if is_phicode_file:
        try:
            import phicode_engine.core.runtime.phicode_loader as loader_module
            setattr(loader_module, "_main_module_name", module_name)
            logger.debug(f"Set main module: {module_name}")
        except ImportError as e:
            logger.warning(f"Could not set main module name: {e}")

    startup_time = (time.perf_counter() - start_time) * 1000
    if startup_time > STARTUP_WARNING_MS:
        logger.warning(f"Slow startup detected: {startup_time:.1f}ms")

    _execute_module(module_name, is_phicode_file, args)
    _flush_batch_writes()

def _show_interpreter_recommendations():
    selector = InterpreterSelector()
    current = selector.get_current_info()
    recommended = selector.get_recommended_interpreter()
    if not current["is_pypy"] and selector.is_pypy(recommended):
        if recommended and selector.is_pypy(recommended):
            logger.info("💡 For 3x faster symbolic processing, use PyPy:")
            logger.info(f"   pypy3 -m phicode_engine <module>")

def _resolve_module(module_or_file):
    if os.path.isfile(module_or_file):
        folder = os.path.dirname(os.path.abspath(module_or_file))
        name = os.path.splitext(os.path.basename(module_or_file))[0]
        is_phi = module_or_file.endswith((MAIN_FILE_TYPE, TERTIARY_FILE_TYPE))
        logger.debug(f"Resolved file: {module_or_file} -> script: {name}, folder: {folder}")
        return name, folder, is_phi
    else:
        cwd = os.getcwd()
        phi_file = os.path.join(cwd, f"{module_or_file}" + MAIN_FILE_TYPE)
        phi_alt_file = os.path.join(cwd, f"{module_or_file}" + TERTIARY_FILE_TYPE)
        py_file = os.path.join(cwd, f"{module_or_file}" + SECONDARY_FILE_TYPE)

        if os.path.isfile(phi_file):
            logger.debug(f"Found {ENGINE_NAME} script: {phi_file}")
            return module_or_file, cwd, True
        elif os.path.isfile(phi_alt_file):
            logger.debug(f"Found {ENGINE_NAME} script: {phi_alt_file}")
            return module_or_file, cwd, True
        elif os.path.isfile(py_file):
            logger.debug(f"Found Python script: {py_file}")
            return module_or_file, cwd, False
        else:
            logger.debug(f"Treating as module name: {module_or_file}")
            return module_or_file, cwd, False

def _execute_module(module_name, is_phicode_file, args):
    try:
        logger.debug(f"Importing module: {module_name}")
        module = importlib.import_module(module_name)

        if not is_phicode_file:
            if hasattr(module, "main") and callable(getattr(module, "main")):
                logger.debug(f"Calling main() with args: {args.remaining_args}")

                with _argv_context(args.get_module_argv()):
                    try:
                        module.main(args.remaining_args if args.remaining_args else None)
                    except Exception as e:
                        _handle_main_error(e, args.debug)
            else:
                logger.debug(f"No main() function found in {module_name}")

        logger.debug(f"Module {module_name} executed successfully")

    except ImportError as e:
        _handle_import_error(module_name, e, args.debug)
    except Exception as e:
        _handle_execution_error(module_name, e, args.debug)

def _handle_main_error(error, debug):
    logger.error(f"Error in main() function: {error}")
    if debug:
        traceback.print_exc()

def _handle_import_error(module_name, error, debug):
    if debug:
        logger.error(f"Debug: Import error for module '{module_name}':")
        traceback.print_exc()
    else:
        logger.error(f"Failed to import module '{module_name}': {error}")
    sys.exit(2)

def _handle_execution_error(module_name, error, debug):
    if debug:
        logger.error(f"Debug: Execution error for module '{module_name}':")
        traceback.print_exc()
    else:
        logger.error(f"Error running module '{module_name}': {error}")
    sys.exit(3)
```

=== File: src\phicode_engine\core\runtime\shutdown_handler.py (79 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
import os
import signal
import atexit
from threading import RLock
from ..phicode_logger import logger
from ...config.config import CACHE_PATH

class ShutdownHandler:
    __slots__ = ('_shutdown_hooks', '_lock', '_shutting_down')

    def __init__(self):
        self._shutdown_hooks = []
        self._lock = RLock()
        self._shutting_down = False

    def register_hook(self, func, *args, **kwargs):
        with self._lock:
            if not self._shutting_down:
                self._shutdown_hooks.append((func, args, kwargs))
                logger.debug(f"Registered shutdown hook: {func.__name__}")

    def _run_hooks(self):
        with self._lock:
            if self._shutting_down:
                logger.warning("Shutdown hooks already executed (ignoring duplicate call)")
                return
            self._shutting_down = True
            logger.info(f"Running {len(self._shutdown_hooks)} shutdown hooks...")
            for func, args, kwargs in reversed(self._shutdown_hooks):
                try:
                    logger.debug(f"Executing hook: {func.__name__}")
                    func(*args, **kwargs)
                except Exception as e:
                    logger.error(f"Shutdown hook {func.__name__} failed: {str(e)}", exc_info=True)
                    pass

    def _signal_handler(self, signum, frame):
        signal_name = {signal.SIGINT: "SIGINT", signal.SIGTERM: "SIGTERM"}.get(signum, str(signum))
        logger.info(f"Caught signal {signal_name}, initiating graceful shutdown...")
        self._run_hooks()
        raise SystemExit(0)

    def install(self):
        logger.debug("Installing shutdown handler...")
        signal.signal(signal.SIGINT, self._signal_handler)
        if hasattr(signal, 'SIGTERM'):
            signal.signal(signal.SIGTERM, self._signal_handler)
        atexit.register(self._run_hooks)
        logger.info("Shutdown handler ready & listening (SIGINT/SIGTERM + atexit)")

_shutdown_handler = ShutdownHandler()

def register_cleanup(func, *args, **kwargs):
    _shutdown_handler.register_hook(func, *args, **kwargs)

def install_shutdown_handler():
    _shutdown_handler.install()

def cleanup_cache_temp_files():
    cache_dir = CACHE_PATH
    if os.path.exists(cache_dir):
        try:
            logger.debug(f"Cleaning up cache dir: {cache_dir}")
            removed_files = 0
            for root, dirs, files in os.walk(cache_dir):
                for file in files:
                    if file.endswith('.tmp') or file.endswith('.lock'):
                        try:
                            os.remove(os.path.join(root, file))
                            removed_files += 1
                        except OSError as e:
                            logger.warning(f"Failed to delete {file}: {str(e)}")
            logger.info(f"Cleaned up {removed_files} temporary cache files")
        except Exception as e:
            logger.error(f"Cache cleanup failed: {str(e)}", exc_info=True)
            pass
```

=== File: src\phicode_engine\core\transpilation\phicode_to_python.py (137 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
from functools import lru_cache
from typing import Dict
from ...config.config import PYTHON_TO_PHICODE, RUST_SIZE_THRESHOLD

try:
    import regex as re
except ImportError:
    import re

try:
    from .symbol_config import load_custom_symbols, has_custom_ascii_identifiers, get_ascii_detection_pattern
    from .symbol_optimization import get_optimized_symbol_order
    _HAS_MODULES = True
except ImportError:
    _HAS_MODULES = False
    load_custom_symbols = None
    has_custom_ascii_identifiers = None
    get_ascii_detection_pattern = None
    get_optimized_symbol_order = None

_STRING_PATTERN = re.compile(
    r'('
    r'(?:[rRuUbBfF]{,2})"""[\s\S]*?"""|'
    r'(?:[rRuUbBfF]{,2})\'\'\'[\s\S]*?\'\'\'|'
    r'(?:[rRuUbBfF]{,2})"[^"\n]*"|'
    r'(?:[rRuUbBfF]{,2})\'[^\'\n]*\'|'
    r'#[^\n]*'
    r')',
    re.DOTALL
)

PHICODE_TO_PYTHON = {v: k for k, v in PYTHON_TO_PHICODE.items()}

@lru_cache(maxsize=1)
def get_symbol_mappings() -> Dict[str, str]:
    if _HAS_MODULES and load_custom_symbols:
        custom_symbols = load_custom_symbols()
        base_mapping = PHICODE_TO_PYTHON.copy()

        if custom_symbols:
            for python_kw, symbol in custom_symbols.items():
                base_mapping[symbol] = python_kw

        return base_mapping
    return PHICODE_TO_PYTHON

@lru_cache(maxsize=1)
def build_transpilation_pattern() -> re.Pattern:
    mappings = get_symbol_mappings()

    if _HAS_MODULES and get_optimized_symbol_order:
        sorted_symbols = get_optimized_symbol_order(mappings)
    else:
        sorted_symbols = sorted(mappings.keys(), key=len, reverse=True)

    if _HAS_MODULES and has_custom_ascii_identifiers and has_custom_ascii_identifiers():
        escaped_symbols = []
        for sym in sorted_symbols:
            if sym.isidentifier() and sym.isascii():
                escaped_symbols.append(rf"\b{re.escape(sym)}\b")
            else:
                escaped_symbols.append(re.escape(sym))
    else:
        escaped_symbols = [re.escape(sym) for sym in sorted_symbols]

    return re.compile('|'.join(escaped_symbols))

class SymbolTranspiler:
    def __init__(self):
        self._mappings = None
        self._pattern = None
        self._ascii_detection_pattern = None

    def _has_phi_symbols(self, source: str) -> bool:
        try:
            view = memoryview(source.encode('utf-8'))
            for byte in view:
                if byte > 127:
                    return True
        except (UnicodeEncodeError, MemoryError):
            if any(ord(c) > 127 for c in source):
                return True

        if self._ascii_detection_pattern is None:
            if _HAS_MODULES and get_ascii_detection_pattern:
                self._ascii_detection_pattern = get_ascii_detection_pattern()
            else:
                self._ascii_detection_pattern = None

        if self._ascii_detection_pattern and self._ascii_detection_pattern.search(source):
            return True

        return False

    def get_mappings(self) -> Dict[str, str]:
        if self._mappings is None:
            self._mappings = get_symbol_mappings()
        return self._mappings

    def transpile(self, source: str) -> str:
        if not self._has_phi_symbols(source):
            return source

        if len(source) >= RUST_SIZE_THRESHOLD:
            from ...rust.phirust_accelerator import try_rust_acceleration
            bypass_security = _should_bypass_security()
            rust_result = try_rust_acceleration(source, self.get_mappings(), bypass_security)
            if rust_result is not None:
                return rust_result

        if self._pattern is None:
            self._pattern = build_transpilation_pattern()

        parts = _STRING_PATTERN.split(source)
        mappings = self.get_mappings()

        result = []
        for i, part in enumerate(parts):
            if i % 2 == 0:
                result.append(self._pattern.sub(lambda m: mappings[m.group(0)], part))
            else:
                result.append(part)

        return ''.join(result)

_transpiler = SymbolTranspiler()

def transpile_symbols(source: str) -> str:
    return _transpiler.transpile(source)

def _should_bypass_security() -> bool:
    from ...core.interpreter.phicode_args import get_current_args
    current_args = get_current_args()
    return current_args and current_args.bypass
```

=== File: src\phicode_engine\core\transpilation\symbol_config.py (96 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
import os
import json
from functools import lru_cache
from typing import Dict
from ...core.phicode_logger import logger
from ...config.config import VALIDATION_ENABLED, STRICT_VALIDATION, CUSTOM_FOLDER_PATH, CUSTOM_FOLDER_PATH_2

try:
    import regex as re
except ImportError:
    import re

def _validate_custom_symbols(symbols: Dict[str, str]) -> Dict[str, str]:
    if not VALIDATION_ENABLED:
        return symbols

    validated = {}
    conflicts = []

    from .phicode_to_python import PHICODE_TO_PYTHON

    for python_kw, symbol in symbols.items():
        if symbol in PHICODE_TO_PYTHON and PHICODE_TO_PYTHON[symbol] == python_kw:
            continue

        if symbol in PHICODE_TO_PYTHON:
            conflicts.append(f"Symbol '{symbol}' conflicts with built-in mapping")
            continue

        if not python_kw.isidentifier():
            logger.warning(f"Invalid Python identifier: '{python_kw}', skipping")
            continue

        validated[python_kw] = symbol

    if conflicts and STRICT_VALIDATION:
        raise ValueError(f"Symbol conflicts detected: {'; '.join(conflicts)}")
    elif conflicts:
        _log_conflicts_once(conflicts)

    return validated

def _log_conflicts_once(conflicts: list):
    conflict_msg = '; '.join(conflicts)
    if not hasattr(_log_conflicts_once, '_logged'):
        _log_conflicts_once._logged = set()

    conflict_hash = hash(conflict_msg)
    if conflict_hash not in _log_conflicts_once._logged:
        logger.warning(f"Symbol conflicts ignored: {conflict_msg}")
        _log_conflicts_once._logged.add(conflict_hash)

@lru_cache(maxsize=1)
def load_custom_symbols() -> Dict[str, str]:
    config_paths = [CUSTOM_FOLDER_PATH, CUSTOM_FOLDER_PATH_2]

    for config_path in config_paths:
        if os.path.exists(config_path):
            try:
                with open(config_path, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                raw_symbols = config.get('symbols', {})
                return _validate_custom_symbols(raw_symbols)
            except json.JSONDecodeError as e:
                logger.warning(f"Invalid JSON in {config_path}: {e}")
            except Exception as e:
                logger.warning(f"Failed to load symbols from {config_path}: {e}")

    return {}

@lru_cache(maxsize=1)
def has_custom_ascii_identifiers() -> bool:
    custom_symbols = load_custom_symbols()
    return any(symbol.isidentifier() and symbol.isascii() for symbol in custom_symbols.values())

@lru_cache(maxsize=1)
def get_ascii_detection_pattern() -> re.Pattern:
    custom_symbols = load_custom_symbols()
    ascii_symbols = [sym for sym in custom_symbols.values() if sym.isascii()]

    if not ascii_symbols:
        return None

    sorted_symbols = sorted(ascii_symbols, key=len, reverse=True)
    escaped_symbols = []

    for sym in sorted_symbols:
        if sym.isidentifier():
            escaped_symbols.append(rf"\b{re.escape(sym)}\b")
        else:
            escaped_symbols.append(re.escape(sym))

    return re.compile('|'.join(escaped_symbols))
```

=== File: src\phicode_engine\core\transpilation\symbol_optimization.py (33 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
from typing import Dict, List

_COMMON_SYMBOL_ORDER = ['∀', '∈', 'λ', '→', '≡', 'π', '∧', '∨', '¬', 'ƒ', '⟲', '∴']

def get_optimized_symbol_order(mappings: Dict[str, str]) -> List[str]:
    symbols = list(mappings.keys())

    common_symbols = [s for s in _COMMON_SYMBOL_ORDER if s in symbols]
    other_symbols = [s for s in symbols if s not in _COMMON_SYMBOL_ORDER]

    other_symbols.sort(key=len, reverse=True)

    return common_symbols + other_symbols

def estimate_symbol_frequency(source: str, mappings: Dict[str, str]) -> Dict[str, int]:
    frequency = {}
    for symbol in mappings.keys():
        count = source.count(symbol)
        if count > 0:
            frequency[symbol] = count
    return frequency

def get_adaptive_symbol_order(source: str, mappings: Dict[str, str]) -> List[str]:
    frequency = estimate_symbol_frequency(source, mappings)

    if not frequency:
        return get_optimized_symbol_order(mappings)

    symbols = list(mappings.keys())
    return sorted(symbols, key=lambda s: (frequency.get(s, 0), len(s)), reverse=True)
```

=== File: src\phicode_engine\installers\binary_installer.py (89 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
import os
import shutil
import subprocess
import urllib.request
import tempfile
import time
from ..core.phicode_logger import logger
from ..config.config import MAX_FILE_RETRIES, RETRY_BASE_DELAY

def download_binary(url: str, binary_path: str, script_name: str) -> bool:
    try:
        logger.info(f"Downloading from: {url}")

        for attempt in range(MAX_FILE_RETRIES):
            tmp_path = None
            try:
                with tempfile.NamedTemporaryFile(delete=False, suffix='.exe') as tmp:
                    tmp_path = tmp.name

                urllib.request.urlretrieve(url, tmp_path)
                time.sleep(0.1)

                if os.path.exists(binary_path):
                    os.remove(binary_path)

                shutil.move(tmp_path, binary_path)
                tmp_path = None

                logger.info(f"{script_name} Binary download successful")
                return True

            except (urllib.error.URLError, OSError) as e:
                if tmp_path and os.path.exists(tmp_path):
                    try:
                        time.sleep(0.1)
                        os.remove(tmp_path)
                    except OSError:
                        pass

                if attempt < MAX_FILE_RETRIES - 1:
                    delay = RETRY_BASE_DELAY * (2 ** attempt)
                    logger.info(f"Download attempt {attempt + 1} failed, retrying in {delay}s: {e}")
                    time.sleep(delay)
                else:
                    logger.error(f"Download failed after {MAX_FILE_RETRIES} attempts: {e}")
                    return False

        return False

    except Exception as e:
        logger.error(f"{script_name} Binary download failed: {e}")
        return False

def cargo_install(git_url: str, binary_name: str, binary_path: str) -> bool:
    if not shutil.which("cargo"):
        logger.debug("Cargo not available")
        return False

    try:
        root_dir = os.path.dirname(os.path.dirname(binary_path))  # ~/.phicode
        logger.debug("Attempting cargo install...")

        result = subprocess.run([
            "cargo", "install", "--git", git_url,
            "--bin", binary_name, "--root", root_dir
        ], capture_output=True, text=True, timeout=300)

        if result.returncode == 0:
            logger.debug("Cargo install successful")
            return True
        else:
            logger.debug(f"Cargo install failed: {result.stderr}")
            return False

    except (subprocess.SubprocessError, subprocess.TimeoutExpired) as e:
        logger.debug(f"Cargo install error: {e}")
        return False

def ensure_bin_directory():
    bin_dir = os.path.join(os.path.expanduser("~"), ".phicode", "bin")
    try:
        os.makedirs(bin_dir, exist_ok=True)
    except OSError as e:
        logger.error(f"Failed to create directory: {e}")
        raise
    return bin_dir
```

=== File: src\phicode_engine\installers\phimmuno_installer.py (46 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
import os
from ..core.phicode_logger import logger
from ..config.config import SECURITY_NAME, PHIMMUNO_RELEASE_BASE, PHIMMUNO_BINARY_NAME
from .binary_installer import download_binary, cargo_install, ensure_bin_directory

def get_binary_path() -> str:
    binary_name = PHIMMUNO_BINARY_NAME
    if os.name == 'nt':
        binary_name += ".exe"
    return os.path.join(os.path.expanduser("~"), ".phicode", "bin", binary_name)

def install_phimmuno_binary():
    logger.info(f"Installing {SECURITY_NAME} Security Engine...")

    binary_path = get_binary_path()
    if os.path.exists(binary_path):
        logger.info(f"{SECURITY_NAME} Engine already installed: {binary_path}")
        return

    ensure_bin_directory()

    if _download_binary(binary_path):
        logger.info(f"{SECURITY_NAME} Engine installed: {binary_path}")
        return

    if _cargo_install(binary_path):
        logger.info(f"{SECURITY_NAME} Engine built via cargo")
        return

    logger.error(f"Failed to install {SECURITY_NAME} Engine")
    logger.info("Manual installation: cargo install --git https://github.com/Varietyz/phimmuno-engine")
    raise RuntimeError(f"{SECURITY_NAME} installation failed")

def _download_binary(binary_path: str) -> bool:
    url = f"{PHIMMUNO_RELEASE_BASE}/phimmuno-engine.exe"
    return download_binary(url, binary_path, SECURITY_NAME)

def _cargo_install(binary_path: str) -> bool:
    return cargo_install(
        "https://github.com/Varietyz/phimmuno-engine",
        PHIMMUNO_BINARY_NAME,
        binary_path
    )
```

=== File: src\phicode_engine\installers\phirust_installer.py (46 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
import os
from ..core.phicode_logger import logger
from ..config.config import SCRIPT, RUST_NAME, PHIRUST_RELEASE_BASE, PHIRUST_BINARY_NAME
from .binary_installer import download_binary, cargo_install, ensure_bin_directory

def get_binary_path() -> str:
    binary_name = PHIRUST_BINARY_NAME
    if os.name == 'nt':
        binary_name += ".exe"
    return os.path.join(os.path.expanduser("~"), ".phicode", "bin", binary_name)

def install_phirust_binary():
    logger.info(f"Installing {SCRIPT} Accelerator...")

    binary_path = get_binary_path()
    if os.path.exists(binary_path):
        logger.info(f"{RUST_NAME} Accelerator already installed: {binary_path}")
        return

    ensure_bin_directory()

    if _download_binary(binary_path):
        logger.info(f"{RUST_NAME} Accelerator installed: {binary_path}")
        return

    if _cargo_install(binary_path):
        logger.info(f"{RUST_NAME} Accelerator built via cargo")
        return

    logger.error(f"Failed to install {SCRIPT} Accelerator")
    logger.info("Manual installation: cargo install --git https://github.com/Varietyz/phirust-transpiler")
    raise RuntimeError("Rust installation failed")

def _download_binary(binary_path: str) -> bool:
    url = f"{PHIRUST_RELEASE_BASE}/phirust-transpiler.exe"
    return download_binary(url, binary_path, SCRIPT)

def _cargo_install(binary_path: str) -> bool:
    return cargo_install(
        "https://github.com/Varietyz/phirust-transpiler",
        PHIRUST_BINARY_NAME,
        binary_path
    )
```

=== File: src\phicode_engine\installers\__init__.py (3 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
```

=== File: src\phicode_engine\rust\phirust_accelerator.py (77 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
import os
import subprocess
import json
from typing import Optional, Dict
from ..core.phicode_logger import logger
from ..config.config import RUST_NAME, SCRIPT

_rust_binary_path = None
_json_encoder = json.JSONEncoder(separators=(',', ':'), ensure_ascii=False)
_cached_symbols_json = None
_cached_mappings_hash = None

def try_rust_acceleration(source: str, mappings: Dict[str, str], bypass_security: bool = False) -> Optional[str]:
    try:
        return _try_rust_transpile(source, mappings, bypass_security)
    except Exception as e:
        logger.debug(f"{RUST_NAME} acceleration failed: {e}")
        return None

def _get_cached_symbols_json(mappings: Dict[str, str]) -> str:
    global _cached_symbols_json, _cached_mappings_hash

    current_hash = str(hash(frozenset(mappings.items())))

    if _cached_symbols_json is None or _cached_mappings_hash != current_hash:
        _cached_symbols_json = _json_encoder.encode(mappings)
        _cached_mappings_hash = current_hash

    return _cached_symbols_json

def _try_rust_transpile(source: str, mappings: Dict[str, str], bypass_security: bool) -> Optional[str]:
    global _rust_binary_path

    if _rust_binary_path is None:
        binary_name = "phirust-transpiler.exe" if os.name == 'nt' else "phirust-transpiler"
        binary_path = os.path.join(os.path.expanduser("~"), ".phicode", "bin", binary_name)
        if os.path.exists(binary_path):
            _rust_binary_path = binary_path
            logger.debug(f"Found {SCRIPT} Accelerator: {binary_path}")
        else:
            _rust_binary_path = False
            logger.debug(f"{RUST_NAME} Accelerator not found, using Python fallback")

    if not _rust_binary_path:
        return None

    try:
        symbols_json = _get_cached_symbols_json(mappings)

        cmd = [_rust_binary_path, "--symbols", symbols_json]
        if bypass_security:
            cmd.append("--bypass")

        result = subprocess.run(
            cmd,
            input=source,
            capture_output=True,
            text=True,
            timeout=5
        )

        if result.returncode == 0:
            logger.debug(f"{RUST_NAME} transpilation successful")
            return result.stdout.rstrip('\n\r')
        else:
            logger.debug(f"{RUST_NAME} transpilation failed: {result.stderr}")
            return None

    except subprocess.TimeoutExpired:
        logger.warning(f"{RUST_NAME} transpilation timeout, using Python fallback")
        return None
    except (subprocess.SubprocessError, OSError) as e:
        logger.debug(f"{RUST_NAME} transpilation error: {e}")
        return None
```

=== File: src\phicode_engine\rust\phirust_cli.py (48 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
import os
import sys
from typing import List
from ..core.phicode_logger import logger
from ..config.config import RUST_NAME

def handle_rust_commands(argv: List[str]):
    if "--phirust" in argv:
        _handle_install()
    elif "--phirust-status" in argv:
        _handle_status()
    elif "--phirust-remove" in argv:
        _handle_remove()
    else:
        logger.error("Unknown Rust command")
        sys.exit(1)

def _handle_install():
    try:
        from ..installers.phirust_installer import install_phirust_binary
        install_phirust_binary()
    except ImportError as e:
        logger.error(f"{RUST_NAME} installer not available: {e}")
        sys.exit(1)

def _handle_status():
    from ..installers.phirust_installer import get_binary_path
    binary_path = get_binary_path()
    if os.path.exists(binary_path):
        logger.info(f"{RUST_NAME} Accelerator installed: {binary_path}")
    else:
        logger.info(f"{RUST_NAME} Accelerator not installed. Install with: phicode --phirust")

def _handle_remove():
    from ..installers.phirust_installer import get_binary_path
    binary_path = get_binary_path()
    if os.path.exists(binary_path):
        try:
            os.remove(binary_path)
            logger.info(f"{RUST_NAME} Accelerator removed")
        except OSError as e:
            logger.error(f"Failed to remove {RUST_NAME} Accelerator: {e}")
            sys.exit(1)
    else:
        logger.info(f"{RUST_NAME} Accelerator not installed")
```

=== File: src\phicode_engine\rust\__init__.py (7 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
from .phirust_accelerator import try_rust_acceleration
from .phirust_cli import handle_rust_commands

__all__ = ["try_rust_acceleration", "handle_rust_commands"]
```

=== File: src\phicode_engine\security\phimmuno_cli.py (48 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
import os
import sys
from typing import List
from ..core.phicode_logger import logger
from ..config.config import SECURITY_NAME

def handle_phimmuno_commands(argv: List[str]):
    if "--phimmuno" in argv:
        _handle_install()
    elif "--phimmuno-status" in argv:
        _handle_status()
    elif "--phimmuno-remove" in argv:
        _handle_remove()
    else:
        logger.error("Unknown Phimmuno command")
        sys.exit(1)

def _handle_install():
    try:
        from ..installers.phimmuno_installer import install_phimmuno_binary
        install_phimmuno_binary()
    except ImportError as e:
        logger.error(f"{SECURITY_NAME} installer not available: {e}")
        sys.exit(1)

def _handle_status():
    from ..installers.phimmuno_installer import get_binary_path
    binary_path = get_binary_path()
    if os.path.exists(binary_path):
        logger.info(f"{SECURITY_NAME} Engine installed: {binary_path}")
    else:
        logger.info(f"{SECURITY_NAME} Engine not installed. Install with: phicode --phimmuno")

def _handle_remove():
    from ..installers.phimmuno_installer import get_binary_path
    binary_path = get_binary_path()
    if os.path.exists(binary_path):
        try:
            os.remove(binary_path)
            logger.info(f"{SECURITY_NAME} Engine removed")
        except OSError as e:
            logger.error(f"Failed to remove {SECURITY_NAME} Engine: {e}")
            sys.exit(1)
    else:
        logger.info(f"{SECURITY_NAME} Engine not installed")
```

=== File: src\phicode_engine\security\phimmuno_validator.py (53 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
import subprocess
import os
from typing import Optional
from ..core.phicode_logger import logger

class SecurityValidator:
    def __init__(self):
        self._binary_path = self._find_binary()
        self._enabled = self._binary_path is not None

    def is_enabled(self) -> bool:
        return self._enabled

    def validate(self, content: str) -> bool:
        if not self._enabled:
            return True

        try:
            result = subprocess.run(
                [self._binary_path],
                input=content, text=True,
                capture_output=True, timeout=1
            )

            if result.returncode != 0:
                logger.warning("🛡️ Security threat detected and blocked")

            return result.returncode == 0
        except Exception as e:
            logger.debug(f"Security validation failed: {e}")
            return True

    def _find_binary(self) -> Optional[str]:
        binary_name = "phimmuno-engine.exe" if os.name == 'nt' else "phimmuno-engine"
        binary_path = os.path.join(os.path.expanduser("~"), ".phicode", "bin", binary_name)

        if os.path.exists(binary_path):
            logger.debug("🛡️ Phimmuno security engine enabled")
            return binary_path

        logger.debug("🛡️ Phimmuno not installed - security validation disabled")
        return None

_validator = SecurityValidator()

def is_security_enabled() -> bool:
    return _validator.is_enabled()

def is_content_safe(content: str) -> bool:
    return _validator.validate(content)
```

=== File: src\phicode_engine\security\__init__.py (6 lines) ===

```python
# Copyright 2025 Baleine Jay
# Licensed under the Phicode Non-Commercial License (https://banes-lab.com/licensing)
# Commercial use requires a paid license. See link for details.
from .phimmuno_validator import is_content_safe

__all__ = ["is_content_safe"]
```

=== File: rust_scripts\phimmuno_engine\Cargo.toml (12 lines) ===

```toml
[package]
name = "phimmuno-engine"
version = "0.1.0"
edition = "2024"

[dependencies]
aho-corasick = "1.1.3"

[profile.release]
lto = true
strip = true
opt-level = 3
```

=== File: rust_scripts\phimmuno_engine\main.rs (29 lines) ===

```rust
// Copyright 2025 Baleine Jay
// Licensed under the PhiCode Non-Commercial License (https://banes-lab.com/licensing)
// Commercial use requires a paid license. See link for details.
use aho_corasick::AhoCorasick;
use std::io::{self, Read};

const THREAT_PATTERNS: &[&str] = &[
    "eval(", "eval (", "exec(", "exec (",
    "subprocess.", "os.system(", "os.system (",
    "__import__", "getattr(__builtins__", "compile(",
    "globals(", "locals(", "open(", "input(",
    "pickle.", "marshal.", "ctypes.",
    "../", "rm -rf", "DELETE FROM", "DROP TABLE",
];

fn main() -> std::process::ExitCode {
    let mut content = String::new();
    if io::stdin().read_to_string(&mut content).is_err() {
        return std::process::ExitCode::FAILURE;
    }
    
    let detector = match AhoCorasick::new(THREAT_PATTERNS) {
        Ok(d) => d,
        Err(_) => return std::process::ExitCode::FAILURE,
    };
    
    let is_safe = !detector.is_match(&content);
    std::process::ExitCode::from(if is_safe { 0 } else { 1 })
}
```

=== File: rust_scripts\phimmuno_engine\release.yml (39 lines) ===

```yaml
name: Release

on:
  push:
    tags: ['v*']

jobs:
  build:
    strategy:
      matrix:
        target: [x86_64-pc-windows-msvc]
    runs-on: windows-latest

    steps:
    - uses: actions/checkout@v4
    - uses: actions-rust-lang/setup-rust-toolchain@v1
      with:
        target: ${{ matrix.target }}
        toolchain: stable
    - run: cargo build --release --target ${{ matrix.target }}
    - uses: actions/upload-artifact@v4
      with:
        name: phimmuno-engine-windows
        path: target/${{ matrix.target }}/release/phimmuno-engine.exe

  create-release:
    needs: build
    runs-on: windows-latest
    permissions:
      contents: write
    steps:
    - uses: actions/download-artifact@v4
      with:
        path: artifacts
    - uses: softprops/action-gh-release@v1
      with:
        files: artifacts/phimmuno-engine-windows/phimmuno-engine.exe
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

=== File: rust_scripts\phirust_transpiler\Cargo.toml (16 lines) ===

```toml
[package]
name = "phirust-transpiler"
version = "0.3.1"
edition = "2024"

[dependencies]
clap = { version = "4.5.45", features = ["derive"] }
serde_json = "1.0"
ahash = { version = "0.8", features = ["serde"] }
aho-corasick = "1.1.3"
regex = "1.11.1"

[profile.release]
lto = true
strip = true
opt-level = 3

```

=== File: rust_scripts\phirust_transpiler\main.rs (160 lines) ‼️ ===

```rust
// Copyright 2025 Baleine Jay
// Licensed under the PhiCode Non-Commercial License (https://banes-lab.com/licensing)
// Commercial use requires a paid license. See link for details.
mod threat_detector;
use threat_detector::ThreatDetector;
use clap::Parser;
use std::io::{self, Read, Write};
use ahash::{AHashMap, AHashSet};
use regex::{Regex, Captures};
use serde_json;

pub struct SymbolTranspiler {
    mappings: AHashMap<String, String>,
    pattern: Option<Regex>,
    symbol_bytes: Option<AHashSet<u8>>,
}

impl SymbolTranspiler {
    pub fn new() -> Self {
        Self {
            mappings: AHashMap::new(),
            pattern: None,
            symbol_bytes: None,
        }
    }

    pub fn configure(&mut self, mappings: AHashMap<String, String>) -> Result<(), String> {
        self.mappings = mappings;
        if self.mappings.is_empty() {
            self.pattern = None;
            self.symbol_bytes = None;
            return Ok(());
        }

        let mut bytes = AHashSet::new();
        for symbol in self.mappings.keys() {
            for byte in symbol.bytes() {
                if byte > 127 {
                    bytes.insert(byte);
                }
            }
        }
        self.symbol_bytes = Some(bytes);

        let mut symbols: Vec<_> = self.mappings.keys().cloned().collect();
        symbols.sort_by_key(|s| std::cmp::Reverse(s.len()));

        let escaped_symbols: Vec<String> = symbols.iter()
            .map(|s| {
                if s.chars().all(|c| c.is_alphanumeric() || c == '_') {
                    format!(r"\b{}\b", regex::escape(s))
                } else {
                    regex::escape(s)
                }
            })
            .collect();

        let pattern_str = format!("({})", escaped_symbols.join("|"));
        self.pattern = Some(
            Regex::new(&pattern_str)
                .map_err(|e| format!("Regex compilation failed: {}", e))?
        );
        Ok(())
    }

    fn contains_symbols(&self, source: &str) -> bool {
        match &self.symbol_bytes {
            Some(bytes) => {
                let source_bytes = source.as_bytes();
                for chunk in source_bytes.chunks(64) {
                    for &byte in chunk {
                        if byte > 127 && bytes.contains(&byte) {
                            return true;
                        }
                    }
                }
                false
            },
            None => false,
        }
    }

    pub fn transpile(&mut self, source: &str, threat_detector: &ThreatDetector, bypass_security: bool) -> Result<String, String> {
        if !self.contains_symbols(source) {
            return Ok(source.to_string());
        }

        let pattern = match &self.pattern {
            Some(p) => p,
            None => return Ok(source.to_string()),
        };

        let mut blocked = false;
        let result = pattern.replace_all(source, |caps: &Captures| {
            let matched = &caps[1];

            if let Some(python_replacement) = self.mappings.get(matched) {
                if !bypass_security && threat_detector.is_dangerous(python_replacement) {
                    blocked = true;
                    return "SECURITY_BLOCKED".to_string();
                }
                python_replacement.clone()
            } else {
                matched.to_string()
            }
        });

        if blocked {
            return Err("Security: Dangerous pattern detected during transpilation".to_string());
        }

        Ok(result.to_string())
    }
}

#[derive(Parser)]
#[command(name = "phicode-transpiler")]
#[command(about = "Fast symbolic transpiler for PhiCode")]
struct Cli {
    #[arg(short, long, help = "JSON mapping of symbols to replacements")]
    symbols: String,
    #[arg(long, help = "Show performance benchmarks")]
    benchmark: bool,
    #[arg(long, help = "Bypass threat detection")]
    bypass: bool,
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let cli = Cli::parse();
    let mappings: AHashMap<String, String> = serde_json::from_str(&cli.symbols)?;

    let threat_detector = ThreatDetector::new()?;

    let mut transpiler = SymbolTranspiler::new();
    transpiler.configure(mappings)?;
    let mut source = String::new();
    io::stdin().read_to_string(&mut source)?;

    let result = transpiler.transpile(&source, &threat_detector, cli.bypass)?;

    if cli.benchmark {
        let start = std::time::Instant::now();
        let _ = transpiler.transpile(&source, &threat_detector, cli.bypass)?;
        let duration = start.elapsed();
        let chars_per_sec = if duration.as_secs_f64() > 0.0 {
            source.len() as f64 / duration.as_secs_f64()
        } else {
            f64::INFINITY
        };
        eprintln!("Transpiled {} chars in {:?}", source.len(), duration);
        eprintln!("Speed: {:.0} chars/sec", chars_per_sec);
    }

    if cli.bypass {
        eprintln!("⚠️  Security bypass enabled - threats not blocked");
    }

    io::stdout().write_all(result.as_bytes())?;
    Ok(())
}
```

=== File: rust_scripts\phirust_transpiler\release.yml (39 lines) ===

```yaml
name: Release

on:
  push:
    tags: ['v*']

jobs:
  build:
    strategy:
      matrix:
        target: [x86_64-pc-windows-msvc]
    runs-on: windows-latest
    
    steps:
    - uses: actions/checkout@v4
    - uses: actions-rust-lang/setup-rust-toolchain@v1
      with:
        target: ${{ matrix.target }}
        toolchain: stable
    - run: cargo build --release --target ${{ matrix.target }}
    - uses: actions/upload-artifact@v4
      with:
        name: phirust-transpiler-windows
        path: target/${{ matrix.target }}/release/phirust-transpiler.exe

  create-release:
    needs: build
    runs-on: windows-latest
    permissions:
      contents: write
    steps:
    - uses: actions/download-artifact@v4
      with:
        path: artifacts
    - uses: softprops/action-gh-release@v1
      with:
        files: artifacts/phirust-transpiler-windows/phirust-transpiler.exe
      env:
        GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

=== File: rust_scripts\phirust_transpiler\threat_detector.rs (30 lines) ===

```rust
// Copyright 2025 Baleine Jay
// Licensed under the PhiCode Non-Commercial License (https://banes-lab.com/licensing)
// Commercial use requires a paid license. See link for details.
use aho_corasick::AhoCorasick;

pub struct ThreatDetector {
    detector: AhoCorasick,
}

impl ThreatDetector {
    pub fn new() -> Result<Self, String> {
        let threats = [
            // Current patterns (all good)
            "eval(", "eval (", "exec(", "exec (", "compile(", "compile (",
            "getattr(__builtins__", "getattr(__builtins__,", "globals(", "globals (",
            "locals(", "locals (", "os.system(", "os.system (", "subprocess.",
            "__import__", "vars(", "vars (", "dir(", "dir (", "open(", "open (",
            "input(", "raw_input(",
        ];

        Ok(Self {
            detector: AhoCorasick::new(threats)
                .map_err(|e| format!("Threat detector: {}", e))?
        })
    }

    pub fn is_dangerous(&self, python_code: &str) -> bool {
        self.detector.is_match(python_code)
    }
}
```

=== File: pyproject.toml (43 lines) ===

```toml
[build-system]
requires = ["setuptools>=61.0"]
build-backend = "setuptools.build_meta"

[project]
name = "phicode"
version = "2.6.0"
description = "(φ) Phicode Runtime Engine — Optimized for stability under load (CPython/PyPy Supported)"
readme = "README.md"
license = {file = "LICENSE"}
authors = [
    { name="Jay Baleine", email="jay@banes-lab.com" }
]
requires-python = ">=3.8"
dependencies = [
    "xxhash>=3.0.0",
    "regex>=2025.7.34"
]

[project.optional-dependencies]
utility = ["psutil>=5.8.0"]
rust = []

[project.scripts]
phicode = "phicode_engine.engine:main"
phi = "phicode_engine.engine:main"
phicode-api = "phicode_engine.api.cli:main"
aphi = "phicode_engine.api.cli:main"

[tool.setuptools]
package-dir = {"" = "src"}

[tool.setuptools.packages.find]
where = ["src"]
include = ["phicode_engine*"]

[tool.setuptools.package-data]
"phicode_engine.api" = ["*.py"]
"phicode_engine.rust" = ["*.py"]
"phicode_engine.security" = ["*.py"]
"phicode_engine.installers" = ["*.py"]
"phicode_engine.benchsuite" = ["*.φ"]
"phicode_engine.benchsuite.simulation" = ["*.φ"]
```

=== File: LICENSE (44 lines) ===

```text
Phicode License
------------------------------------------------------------------------------------------
Copyright 2025 Baleine Jay

https://banes-lab.com | https://github.com/Varietyz/phicode-runtime

------------------------------------------------------------------------------------------
NON-COMMERCIAL LICENSE (Default)
This software is available under a non-commercial license based on the MIT License.
------------------------------------------------------------------------------------------

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, **subject to the following commercial restriction:**

COMMERCIAL USE RESTRICTION:
Any use of the Software for commercial purposes, including but not limited to use in
commercial software, paid services, internal use by for-profit organizations, hosting
as a service (SaaS), or distribution for revenue, is expressly prohibited without
a separate commercial license.

To obtain a commercial license, visit: https://banes-lab.com/licensing
or contact: jay.bane@outlook.com.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

------------------------------------------------------------------------------------------
COMMERCIAL LICENSE
For commercial use, a paid license is required. Commercial licenses grant:
- Rights for commercial use, distribution, and hosting
- Rights to create derivative works for commercial purposes
- Optional technical support and maintenance

For details or enterprise licensing, contact: jay.bane@outlook.com.
------------------------------------------------------------------------------------------

```
