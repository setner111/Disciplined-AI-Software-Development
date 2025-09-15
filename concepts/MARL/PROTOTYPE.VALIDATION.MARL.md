<img src="https://banes-lab.com/assets/images/banes_lab/700px_Main_Animated.gif" width="70" />

## 📂 The Project - Current Tree Structure
```
📂 prototype
├─ 🏠 main.py (19 lines)
├─ 📄 requirements.txt (2 lines)
├─ 📂 core
│   ├─ 🐍 __init__.py (0 lines)
│   ├─ 🐍 command_handler.py (54 lines)
│   └─ ⚙️ config.py (75 lines)
├─ 📂 dashboard
│   ├─ 🏠 main.js (0 lines)
│   ├─ 📦 package.json (16 lines)
│   └─ 📂 renderer
│       ├─ 📇 index.html (0 lines)
│       └─ 🎨 styles.css (0 lines)
├─ 📂 data
│   ├─ 🐍 __init__.py (0 lines)
│   ├─ 📊 database.py (82 lines)
│   ├─ 📊 database_service.py (32 lines)
│   └─ 🐍 results_processor.py (33 lines)
├─ 📂 results
│   ├─ ⚡ benchmark_results.json (100 lines)
│   └─ ✅ validation_results.db (0 lines)
├─ 📂 testing
│   ├─ 🐍 __init__.py (0 lines)
│   └─ 🧪 test_case_generator.py (61 lines)
└─ 📂 validation
    ├─ 🐍 __init__.py (0 lines)
    ├─ 🐍 claude_client.py (138 lines)
    ├─ 🐍 constraint_checker.py (125 lines)
    ├─ ✅ validation_orchestrator.py (89 lines)
    └─ ⚙️ validation_service.py (41 lines)
```

## 📄 Project File Contents


=== File: prototype\main.py (19 lines) ===

```python
#!/usr/bin/env python3

import sys
from core.command_handler import CommandHandler

def main():
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python main.py validate <file_path>")
        print("  python main.py benchmark")
        print("  python main.py stats")
        print("  echo 'code' | python main.py validate -")
        return
    
    handler = CommandHandler()
    handler.execute(sys.argv[1:])

if __name__ == "__main__":
    main()
```

=== File: prototype\requirements.txt (2 lines) ===

```text
anthropic
python-dotenv
```

=== File: prototype\core\command_handler.py (54 lines) ===

```python
import json
import sys
from typing import List
from validation.validation_service import ValidationService
from data.database_service import DatabaseService

class CommandHandler:
    def __init__(self):
        self.validation_service = ValidationService()
        self.database_service = DatabaseService()
    
    def execute(self, args: List[str]):
        if not args:
            return
        
        command = args[0]
        
        if command == "validate":
            self._handle_validate_command(args[1:])
        elif command == "benchmark":
            self._handle_benchmark_command()
        elif command == "stats":
            self._handle_stats_command()
        else:
            print(f"Unknown command: {command}")
            print("Available commands: validate, benchmark, stats")
    
    def _handle_validate_command(self, args: List[str]):
        if not args:
            print("Error: validate command requires file path or '-' for stdin")
            return
        
        file_path = args[0]
        if file_path == "-":
            code_input = sys.stdin.read()
            result = self.validation_service.validate_code_input(code_input)
        else:
            result = self.validation_service.validate_file(file_path)
        
        print(json.dumps(result, indent=2))
    
    def _handle_benchmark_command(self):
        print("Running validation benchmark suite...")
        result = self.validation_service.run_benchmark_suite()
        
        print("\nBenchmark Summary:")
        print(f"Total cases: {result['summary']['total_cases']}")
        print(f"Compliant cases: {result['summary']['compliant_cases']}")
        print(f"Compliance rate: {result['summary']['compliance_rate']:.1%}")
        print(f"Average score: {result['summary']['average_score']:.3f}")
        print(f"Processing time: {result['summary']['total_processing_time']:.2f}s")
    
    def _handle_stats_command(self):
        self.database_service.show_statistics()
```

=== File: prototype\core\config.py (75 lines) ===

```python
import os
from dataclasses import dataclass
from typing import List

try:
    from dotenv import load_dotenv
    dotenv_path = os.path.join(os.getcwd(), '.env')
    load_result = load_dotenv(dotenv_path)
    print(f"Loading .env from: {dotenv_path}")
    print(f"Load result: {load_result}")
    
    if os.path.exists(dotenv_path):
        with open(dotenv_path, 'r') as f:
            content = f.read()
            print(f".env content preview: {content[:100]}...")
    else:
        print(".env file not found at expected path")
        
except ImportError:
    print("python-dotenv not installed - using system environment only")

@dataclass
class ValidationConfig:
    anthropic_api_key: str
    model: str = "claude-sonnet-4-20250514"
    max_tokens: int = 1024
    max_retries: int = 3
    timeout: int = 30
    
    file_line_limit: int = 150
    web_file_line_limit: int = 250
    
    forbidden_patterns: List[str] = None
    required_patterns: List[str] = None
    
    sqlite_path: str = "results/validation_results.db"
    benchmark_output: str = "results/benchmark_results.json"
    
    def __post_init__(self):
        if self.forbidden_patterns is None:
            self.forbidden_patterns = [
                "eval(",
                "exec(",
                "subprocess.call",
                "os.system",
                "__import__",
                "importlib"
            ]
        
        if self.required_patterns is None:
            self.required_patterns = [
                "def ",
                "class "
            ]
        
        os.makedirs("results", exist_ok=True)

def load_config() -> ValidationConfig:
    api_key = os.getenv("ANTHROPIC_API_KEY")
    model = os.getenv("CLAUDE_MODEL", "claude-sonnet-4-20250514")
    
    print(f"API Key found: {bool(api_key)}")
    if api_key:
        print(f"Key starts with: {api_key[:10]}...")
    
    if not api_key:
        print("⚠️ ANTHROPIC_API_KEY not found - using mock validation mode")
        api_key = "mock_key"
    
    return ValidationConfig(
        anthropic_api_key=api_key,
        model=model
    )

config = load_config()
```

=== File: prototype\core\__init__.py (0 lines) ===

```python

```

=== File: prototype\dashboard\main.js (0 lines) ===

```javascript

```

=== File: prototype\dashboard\package.json (16 lines) ===

```json
{
  "name": "validation-dashboard",
  "version": "1.0.0",
  "description": "Code validation metrics visualization dashboard",
  "main": "main.js",
  "scripts": {
    "start": "electron .",
    "dev": "electron . --dev"
  },
  "dependencies": {
    "electron": "^38.1.0",
    "sqlite3": "^5.1.7"
  },
  "author": "R&D Validation Team",
  "license": "MIT"
}
```

=== File: prototype\dashboard\renderer\index.html (0 lines) ===

```html

```

=== File: prototype\dashboard\renderer\styles.css (0 lines) ===

```css

```

=== File: prototype\data\database.py (82 lines) ===

```python
import sqlite3
import json
from typing import Dict, List, Any
from datetime import datetime
from core.config import config

class ValidationDatabase:
    def __init__(self, db_path: str = None):
        self.db_path = db_path or config.sqlite_path
        self.init_database()
    
    def init_database(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.executescript("""
                CREATE TABLE IF NOT EXISTS validations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    code_hash TEXT NOT NULL,
                    file_name TEXT,
                    line_count INTEGER,
                    violations TEXT,
                    success_score REAL,
                    processing_time REAL,
                    timestamp INTEGER,
                    prompt_used TEXT,
                    model_response TEXT
                );
                
                CREATE TABLE IF NOT EXISTS performance_baselines (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    metric_name TEXT NOT NULL,
                    baseline_value REAL,
                    current_value REAL,
                    measurement_date INTEGER
                );
                
                CREATE TABLE IF NOT EXISTS violation_patterns (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    violation_type TEXT NOT NULL,
                    pattern_text TEXT,
                    frequency INTEGER DEFAULT 1,
                    success_rate REAL
                );
            """)
    
    def store_validation(self, code: str, violations: List[str], 
                        processing_time: float, success_score: float,
                        file_name: str = None, prompt: str = None, 
                        response: str = None) -> int:
        code_hash = str(hash(code))
        line_count = len(code.split('\n'))
        violations_json = json.dumps(violations)
        timestamp = int(datetime.now().timestamp())
        
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute("""
                INSERT INTO validations 
                (code_hash, file_name, line_count, violations, success_score, 
                 processing_time, timestamp, prompt_used, model_response)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (code_hash, file_name, line_count, violations_json, 
                  success_score, processing_time, timestamp, prompt, response))
            return cursor.lastrowid
    
    def get_violation_patterns(self) -> List[Dict[str, Any]]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute("""
                SELECT violation_type, pattern_text, frequency, success_rate
                FROM violation_patterns
                ORDER BY frequency DESC
            """)
            return [{"type": row[0], "pattern": row[1], 
                    "frequency": row[2], "success_rate": row[3]} 
                   for row in cursor.fetchall()]
    
    def update_baseline(self, metric_name: str, value: float):
        timestamp = int(datetime.now().timestamp())
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                INSERT INTO performance_baselines 
                (metric_name, current_value, measurement_date)
                VALUES (?, ?, ?)
            """, (metric_name, value, timestamp))
```

=== File: prototype\data\database_service.py (32 lines) ===

```python
import sqlite3
from data.database import ValidationDatabase

class DatabaseService:
    def __init__(self):
        self.db = ValidationDatabase()
    
    def show_statistics(self):
        print("Validation Database Statistics:")
        print("-" * 40)
        
        conn = sqlite3.connect(self.db.db_path)
        
        cursor = conn.execute("SELECT COUNT(*) FROM validations")
        total_validations = cursor.fetchone()[0]
        print(f"Total validations: {total_validations}")
        
        cursor = conn.execute("SELECT AVG(success_score) FROM validations")
        avg_score = cursor.fetchone()[0] or 0
        print(f"Average success score: {avg_score:.3f}")
        
        cursor = conn.execute("SELECT AVG(processing_time) FROM validations")
        avg_time = cursor.fetchone()[0] or 0
        print(f"Average processing time: {avg_time:.3f}s")
        
        patterns = self.db.get_violation_patterns()
        if patterns:
            print("\nTop violation patterns:")
            for pattern in patterns[:5]:
                print(f"  {pattern['type']}: {pattern['frequency']} occurrences")
        
        conn.close()
```

=== File: prototype\data\results_processor.py (33 lines) ===

```python
import json
from typing import Dict, List, Any
from core.config import config

class ResultsProcessor:
    def __init__(self, db):
        self.db = db
    
    def generate_summary(self, results: List[Dict], total_time: float) -> Dict[str, Any]:
        total_cases = len(results)
        compliant_cases = sum(1 for r in results if r["compliant"])
        avg_score = sum(r["combined_score"] for r in results) / total_cases if total_cases > 0 else 0
        avg_processing_time = sum(r["processing_time"] for r in results) / total_cases if total_cases > 0 else 0
        
        return {
            "total_cases": total_cases,
            "compliant_cases": compliant_cases,
            "compliance_rate": compliant_cases / total_cases if total_cases > 0 else 0,
            "average_score": avg_score,
            "average_processing_time": avg_processing_time,
            "total_processing_time": total_time,
            "throughput": total_cases / total_time if total_time > 0 else 0
        }
    
    def save_results(self, results: Dict[str, Any]):
        with open(config.benchmark_output, 'w') as f:
            json.dump(results, f, indent=2)
        print(f"Results saved to {config.benchmark_output}")
    
    def update_baselines(self, summary: Dict[str, Any]):
        for metric, value in summary.items():
            if isinstance(value, (int, float)):
                self.db.update_baseline(metric, float(value))
```

=== File: prototype\data\__init__.py (0 lines) ===

```python

```

=== File: prototype\results\benchmark_results.json (100 lines) ===

```json
{
  "timestamp": "2025-09-14T16:17:53.318246",
  "test_cases": 3,
  "results": [
    {
      "name": "compliant_module",
      "validation_id": 25,
      "constraint_checker": {
        "violations": [],
        "warnings": [],
        "success_score": 1.0,
        "compliant": true,
        "line_count": 9,
        "file_name": "compliant_module"
      },
      "claude_validation": {
        "violations": [
          "Violation of DRY principle: input validation logic duplicated between process_data() and validate_input()",
          "Violation of SoC principle: process_data() handles both validation and processing concerns"
        ],
        "success_score": 0.7,
        "processing_time": 4.3183372020721436,
        "raw_response": "```json\n{\n  \"violations\": [\n    \"Violation of DRY principle: input validation logic duplicated between process_data() and validate_input()\",\n    \"Violation of SoC principle: process_data() handles both validation and processing concerns\"\n  ],\n  \"compliant\": false,\n  \"score\": 0.7\n}\n```",
        "prompt_used": "Analyze this code against systematic constraints:\n\nCONSTRAINTS:\n- File must be \u2264150 lines\n- No forbidden security patterns\n- Must follow DRY/KISS/SoC principles\n\nCODE:\n```python\ndef process_data(input_data):\n    if not input_data:\n        return None\n    \n    cleaned_data = [item.strip() for item in input_data if item.strip()]\n    return sorted(cleaned_data)\n\ndef validate_input(data):\n    return data is not None and len(data) > 0\n```\n\nRespond with JSON format:\n{\n  \"violations\": [\"list of specific violations found\"],\n  \"compliant\": true/false,\n  \"score\": 0.0-1.0\n}"
      },
      "processing_time": 4.323861837387085,
      "combined_score": 0.7,
      "compliant": false
    },
    {
      "name": "line_limit_violation",
      "validation_id": 26,
      "constraint_checker": {
        "violations": [
          "File exceeds 150 line limit: 160 lines"
        ],
        "warnings": [],
        "success_score": 0.0,
        "compliant": false,
        "line_count": 160,
        "file_name": "line_limit_violation"
      },
      "claude_validation": {
        "violations": [
          "File exceeds 150 lines (160 lines total)",
          "Violates DRY principle - repetitive comment pattern 'Line X' repeated 160 times",
          "Violates KISS principle - unnecessarily complex structure for what appears to be placeholder content"
        ],
        "success_score": 0.2,
        "processing_time": 8.019530534744263,
        "raw_response": "```json\n{\n  \"violations\": [\"File exceeds 150 lines (160 lines total)\", \"Violates DRY principle - repetitive comment pattern 'Line X' repeated 160 times\", \"Violates KISS principle - unnecessarily complex structure for what appears to be placeholder content\"],\n  \"compliant\": false,\n  \"score\": 0.2\n}\n```",
        "prompt_used": "Analyze this code against systematic constraints:\n\nCONSTRAINTS:\n- File must be \u2264150 lines\n- No forbidden security patterns\n- Must follow DRY/KISS/SoC principles\n\nCODE:\n```python\n# Line 0\n# Line 1\n# Line 2\n# Line 3\n# Line 4\n# Line 5\n# Line 6\n# Line 7\n# Line 8\n# Line 9\n# Line 10\n# Line 11\n# Line 12\n# Line 13\n# Line 14\n# Line 15\n# Line 16\n# Line 17\n# Line 18\n# Line 19\n# Line 20\n# Line 21\n# Line 22\n# Line 23\n# Line 24\n# Line 25\n# Line 26\n# Line 27\n# Line 28\n# Line 29\n# Line 30\n# Line 31\n# Line 32\n# Line 33\n# Line 34\n# Line 35\n# Line 36\n# Line 37\n# Line 38\n# Line 39\n# Line 40\n# Line 41\n# Line 42\n# Line 43\n# Line 44\n# Line 45\n# Line 46\n# Line 47\n# Line 48\n# Line 49\n# Line 50\n# Line 51\n# Line 52\n# Line 53\n# Line 54\n# Line 55\n# Line 56\n# Line 57\n# Line 58\n# Line 59\n# Line 60\n# Line 61\n# Line 62\n# Line 63\n# Line 64\n# Line 65\n# Line 66\n# Line 67\n# Line 68\n# Line 69\n# Line 70\n# Line 71\n# Line 72\n# Line 73\n# Line 74\n# Line 75\n# Line 76\n# Line 77\n# Line 78\n# Line 79\n# Line 80\n# Line 81\n# Line 82\n# Line 83\n# Line 84\n# Line 85\n# Line 86\n# Line 87\n# Line 88\n# Line 89\n# Line 90\n# Line 91\n# Line 92\n# Line 93\n# Line 94\n# Line 95\n# Line 96\n# Line 97\n# Line 98\n# Line 99\n# Line 100\n# Line 101\n# Line 102\n# Line 103\n# Line 104\n# Line 105\n# Line 106\n# Line 107\n# Line 108\n# Line 109\n# Line 110\n# Line 111\n# Line 112\n# Line 113\n# Line 114\n# Line 115\n# Line 116\n# Line 117\n# Line 118\n# Line 119\n# Line 120\n# Line 121\n# Line 122\n# Line 123\n# Line 124\n# Line 125\n# Line 126\n# Line 127\n# Line 128\n# Line 129\n# Line 130\n# Line 131\n# Line 132\n# Line 133\n# Line 134\n# Line 135\n# Line 136\n# Line 137\n# Line 138\n# Line 139\n# Line 140\n# Line 141\n# Line 142\n# Line 143\n# Line 144\n# Line 145\n# Line 146\n# Line 147\n# Line 148\n# Line 149\n# Line 150\n# Line 151\n# Line 152\n# Line 153\n# Line 154\n# Line 155\n# Line 156\n# Line 157\n# Line 158\n# Line 159\n```\n\nRespond with JSON format:\n{\n  \"violations\": [\"list of specific violations found\"],\n  \"compliant\": true/false,\n  \"score\": 0.0-1.0\n}"
      },
      "processing_time": 8.022051095962524,
      "combined_score": 0.0,
      "compliant": false
    },
    {
      "name": "security_violation",
      "validation_id": 27,
      "constraint_checker": {
        "violations": [
          "Forbidden security pattern: eval(",
          "Forbidden security pattern: os.system"
        ],
        "warnings": [],
        "success_score": 0.0,
        "compliant": false,
        "line_count": 5,
        "file_name": "security_violation"
      },
      "claude_validation": {
        "violations": [
          "Uses eval() which allows arbitrary code execution - major security vulnerability",
          "Uses os.system() with user input without sanitization - command injection vulnerability",
          "f-string with unsanitized user input passed to system command creates shell injection risk",
          "No input validation or sanitization implemented",
          "Function enables remote code execution through eval()",
          "Missing error handling for potential eval() exceptions"
        ],
        "success_score": 0.0,
        "processing_time": 5.350508451461792,
        "raw_response": "```json\n{\n  \"violations\": [\n    \"Uses eval() which allows arbitrary code execution - major security vulnerability\",\n    \"Uses os.system() with user input without sanitization - command injection vulnerability\",\n    \"f-string with unsanitized user input passed to system command creates shell injection risk\",\n    \"No input validation or sanitization implemented\",\n    \"Function enables remote code execution through eval()\",\n    \"Missing error handling for potential eval() exceptions\"\n  ],\n  \"compliant\": false,\n  \"score\": 0.0\n}\n```",
        "prompt_used": "Analyze this code against systematic constraints:\n\nCONSTRAINTS:\n- File must be \u2264150 lines\n- No forbidden security patterns\n- Must follow DRY/KISS/SoC principles\n\nCODE:\n```python\nimport os\ndef risky_function(user_input):\n    result = eval(user_input)\n    os.system(f\"echo {result}\")\n    return result\n```\n\nRespond with JSON format:\n{\n  \"violations\": [\"list of specific violations found\"],\n  \"compliant\": true/false,\n  \"score\": 0.0-1.0\n}"
      },
      "processing_time": 5.353517770767212,
      "combined_score": 0.0,
      "compliant": false
    }
  ],
  "summary": {
    "total_cases": 3,
    "compliant_cases": 0,
    "compliance_rate": 0.0,
    "average_score": 0.2333333333333333,
    "average_processing_time": 5.899810234705607,
    "total_processing_time": 17.724966764450073,
    "throughput": 0.1692527856253544
  }
}
```

=== File: prototype\results\validation_results.db (0 lines) ===

```text
[Could not read file: 'utf-8' codec can't decode byte 0xbd in position 111: invalid start byte]
```

=== File: prototype\testing\test_case_generator.py (61 lines) ===

```python
from typing import List, Dict

class TestCaseGenerator:
    def __init__(self):
        pass
    
    def create_test_cases(self) -> List[Dict[str, str]]:
        return [
            {
                "name": "compliant_module",
                "code": """def process_data(input_data):
    if not input_data:
        return None
    
    cleaned_data = [item.strip() for item in input_data if item.strip()]
    return sorted(cleaned_data)

def validate_input(data):
    return data is not None and len(data) > 0""",
                "is_web_component": False
            },
            {
                "name": "line_limit_violation",
                "code": "\n".join([f"# Line {i}" for i in range(160)]),
                "is_web_component": False
            },
            {
                "name": "security_violation", 
                "code": """import os
def risky_function(user_input):
    result = eval(user_input)
    os.system(f"echo {result}")
    return result""",
                "is_web_component": False
            }
        ]
    
    def create_web_test_cases(self) -> List[Dict[str, str]]:
        return [
            {
                "name": "compliant_react_component",
                "code": """import React from 'react';

function DataDisplay({ items }) {
    if (!items || items.length === 0) {
        return <div>No data available</div>;
    }
    
    return (
        <ul>
            {items.map((item, index) => (
                <li key={index}>{item}</li>
            ))}
        </ul>
    );
}

export default DataDisplay;""",
                "is_web_component": True
            }
        ]
```

=== File: prototype\testing\__init__.py (0 lines) ===

```python

```

=== File: prototype\validation\claude_client.py (138 lines) ===

```python
import time
from typing import List, Dict, Any
from core.config import config

class ClaudeClient:
    def __init__(self):
        if config.anthropic_api_key == "mock_key":
            self.available = False
            print("Running in mock validation mode - no API calls")
        else:
            try:
                import anthropic
                self.client = anthropic.Anthropic(api_key=config.anthropic_api_key)
                self.available = True
                print("Claude API client initialized")
            except ImportError:
                self.available = False
                print("Anthropic library not available - using mock responses")
    
    def validate_code(self, code: str, constraints: List[str]) -> Dict[str, Any]:
        if not self.available:
            return self._mock_validation(code, constraints)
        
        prompt = self._build_validation_prompt(code, constraints)
        
        print("\n--- CLAUDE API CALL ---")
        print(f"Model: {config.model}")
        print(f"Max tokens: {config.max_tokens}")
        print(f"Prompt length: {len(prompt)} chars")
        print(f"Code lines: {len(code.split(chr(10)))}")
        
        start_time = time.time()
        try:
            print("Sending request to Claude API...")
            response = self.client.messages.create(
                model=config.model,
                max_tokens=config.max_tokens,
                messages=[{"role": "user", "content": prompt}]
            )
            processing_time = time.time() - start_time
            
            print(f"Response received in {processing_time:.2f}s")
            print(f"Response length: {len(response.content[0].text)} chars")
            print("\n--- CLAUDE RESPONSE ---")
            print(response.content[0].text)
            print("--- END RESPONSE ---\n")
            
            violations = self._parse_violations(response.content[0].text)
            success_score = self._calculate_success_score(response.content[0].text)
            
            print(f"Parsed violations: {len(violations)}")
            print(f"Success score: {success_score}")
            
            return {
                "violations": violations,
                "success_score": success_score,
                "processing_time": processing_time,
                "raw_response": response.content[0].text,
                "prompt_used": prompt
            }
        except Exception as e:
            processing_time = time.time() - start_time
            print(f"API Error after {processing_time:.2f}s: {str(e)}")
            return {
                "violations": [f"API Error: {str(e)}"],
                "success_score": 0.0,
                "processing_time": processing_time,
                "raw_response": "",
                "prompt_used": prompt
            }
    
    def _build_validation_prompt(self, code: str, constraints: List[str]) -> str:
        constraint_text = "\n".join(f"- {c}" for c in constraints)
        
        return f"""Analyze this code against systematic constraints:

CONSTRAINTS:
{constraint_text}

CODE:
```python
{code}
```

Respond with JSON format:
{{
  "violations": ["list of specific violations found"],
  "compliant": true/false,
  "score": 0.0-1.0
}}"""
    
    def _parse_violations(self, response: str) -> List[str]:
        try:
            import json
            if "```json" in response:
                json_part = response.split("```json")[1].split("```")[0]
            else:
                json_part = response
            
            data = json.loads(json_part.strip())
            return data.get("violations", [])
        except Exception:
            return ["Failed to parse validation response"]
    
    def _calculate_success_score(self, response: str) -> float:
        try:
            import json
            if "```json" in response:
                json_part = response.split("```json")[1].split("```")[0]
            else:
                json_part = response
            
            data = json.loads(json_part.strip())
            return float(data.get("score", 0.0))
        except Exception:
            return 0.0
    
    def _mock_validation(self, code: str, constraints: List[str]) -> Dict[str, Any]:
        violations = []
        line_count = len(code.split('\n'))
        
        if line_count > config.file_line_limit:
            violations.append(f"File exceeds {config.file_line_limit} lines ({line_count})")
        
        for pattern in config.forbidden_patterns:
            if pattern in code:
                violations.append(f"Forbidden pattern found: {pattern}")
        
        success_score = 1.0 - (len(violations) * 0.2)
        success_score = max(0.0, min(1.0, success_score))
        
        return {
            "violations": violations,
            "success_score": success_score,
            "processing_time": 0.1,
            "raw_response": f"Mock validation - {len(violations)} violations found",
            "prompt_used": "Mock prompt"
        }
```

=== File: prototype\validation\constraint_checker.py (125 lines) ===

```python
import re
import ast
from typing import List, Dict, Any
from core.config import config

class ConstraintChecker:
    def __init__(self):
        self.constraints = self._load_constraints()
    
    def _load_constraints(self) -> Dict[str, Any]:
        return {
            "file_line_limit": config.file_line_limit,
            "web_file_line_limit": config.web_file_line_limit,
            "forbidden_patterns": config.forbidden_patterns,
            "required_patterns": config.required_patterns,
            "architectural_rules": [
                "single_responsibility",
                "dry_principle",
                "kiss_principle",
                "separation_of_concerns"
            ]
        }
    
    def validate_code(self, code: str, file_name: str = None, 
                     is_web_component: bool = False) -> Dict[str, Any]:
        violations = []
        warnings = []
        
        violations.extend(self._check_line_count(code, is_web_component))
        violations.extend(self._check_forbidden_patterns(code))
        violations.extend(self._check_syntax_validity(code))
        
        warnings.extend(self._check_code_quality(code))
        warnings.extend(self._check_architectural_compliance(code))
        
        success_score = self._calculate_compliance_score(violations, warnings)
        
        return {
            "violations": violations,
            "warnings": warnings,
            "success_score": success_score,
            "compliant": len(violations) == 0,
            "line_count": len(code.split('\n')),
            "file_name": file_name
        }
    
    def _check_line_count(self, code: str, is_web_component: bool) -> List[str]:
        lines = code.split('\n')
        line_count = len(lines)
        limit = self.constraints["web_file_line_limit"] if is_web_component else self.constraints["file_line_limit"]
        
        if line_count > limit:
            return [f"File exceeds {limit} line limit: {line_count} lines"]
        return []
    
    def _check_forbidden_patterns(self, code: str) -> List[str]:
        violations = []
        for pattern in self.constraints["forbidden_patterns"]:
            if pattern in code:
                violations.append(f"Forbidden security pattern: {pattern}")
        return violations
    
    def _check_syntax_validity(self, code: str) -> List[str]:
        try:
            ast.parse(code)
            return []
        except SyntaxError as e:
            return [f"Syntax error: {str(e)}"]
    
    def _check_code_quality(self, code: str) -> List[str]:
        warnings = []
        
        if len(re.findall(r'def\s+(\w+)', code)) > 10:
            warnings.append("High function count suggests separation of concerns violation")
        
        if len(re.findall(r'class\s+(\w+)', code)) > 3:
            warnings.append("Multiple classes in single file may violate SoC")
        
        if code.count('import ') > 15:
            warnings.append("High import count suggests excessive dependencies")
        
        return warnings
    
    def _check_architectural_compliance(self, code: str) -> List[str]:
        warnings = []
        
        duplicated_code = self._detect_code_duplication(code)
        if duplicated_code:
            warnings.append("Potential DRY violation: duplicated code patterns")
        
        complex_functions = self._detect_complex_functions(code)
        if complex_functions:
            warnings.append("KISS violation: overly complex function implementations")
        
        return warnings
    
    def _detect_code_duplication(self, code: str) -> bool:
        lines = [line.strip() for line in code.split('\n') if line.strip()]
        line_counts = {}
        
        for line in lines:
            if len(line) > 20 and not line.startswith('#'):
                line_counts[line] = line_counts.get(line, 0) + 1
        
        return any(count > 2 for count in line_counts.values())
    
    def _detect_complex_functions(self, code: str) -> bool:
        try:
            tree = ast.parse(code)
            for node in ast.walk(tree):
                if isinstance(node, ast.FunctionDef):
                    if len(node.body) > 20:
                        return True
        except Exception:
            pass
        return False
    
    def _calculate_compliance_score(self, violations: List[str], 
                                  warnings: List[str]) -> float:
        if violations:
            return 0.0
        
        warning_penalty = len(warnings) * 0.1
        score = 1.0 - warning_penalty
        return max(0.0, min(1.0, score))
```

=== File: prototype\validation\validation_orchestrator.py (89 lines) ===

```python
import time
from typing import Dict, List, Any
from datetime import datetime
from data.database import ValidationDatabase
from validation.constraint_checker import ConstraintChecker
from validation.claude_client import ClaudeClient

class ValidationOrchestrator:
    def __init__(self):
        self.db = ValidationDatabase()
        self.constraint_checker = ConstraintChecker()
        self.claude_client = ClaudeClient()
    
    def run_validation_suite(self, test_cases: List[Dict[str, str]]) -> Dict[str, Any]:
        print("Starting validation benchmark suite...")
        
        results = {
            "timestamp": datetime.now().isoformat(),
            "test_cases": len(test_cases),
            "results": [],
            "summary": {}
        }
        
        total_start = time.time()
        
        for i, test_case in enumerate(test_cases):
            print(f"Processing test case {i+1}/{len(test_cases)}: {test_case.get('name', 'unnamed')}")
            result = self.run_single_validation(test_case)
            results["results"].append(result)
        
        total_time = time.time() - total_start
        
        from data.results_processor import ResultsProcessor
        processor = ResultsProcessor(self.db)
        results["summary"] = processor.generate_summary(results["results"], total_time)
        processor.save_results(results)
        processor.update_baselines(results["summary"])
        
        return results
    
    def run_single_validation(self, test_case: Dict[str, str]) -> Dict[str, Any]:
        code = test_case["code"]
        name = test_case.get("name", "unnamed")
        is_web = test_case.get("is_web_component", False)
        
        print(f"\n=== VALIDATING: {name} ===")
        print(f"Code preview: {code[:100]}...")
        print(f"Lines: {len(code.split(chr(10)))}")
        
        start_time = time.time()
        
        print("Running local constraint checker...")
        constraint_result = self.constraint_checker.validate_code(
            code, name, is_web
        )
        print(f"Local violations: {len(constraint_result['violations'])}")
        
        print("Running Claude API validation...")
        claude_result = self.claude_client.validate_code(
            code, 
            ["File must be ≤150 lines", "No forbidden security patterns", 
             "Must follow DRY/KISS/SoC principles"]
        )
        
        processing_time = time.time() - start_time
        combined_score = min(constraint_result["success_score"], claude_result["success_score"])
        
        print(f"Combined score: {combined_score}")
        print(f"Overall compliant: {constraint_result['compliant'] and len(claude_result['violations']) == 0}")
        
        validation_id = self.db.store_validation(
            code=code,
            violations=constraint_result["violations"] + claude_result["violations"],
            processing_time=processing_time,
            success_score=combined_score,
            file_name=name,
            prompt=claude_result.get("prompt_used", ""),
            response=claude_result.get("raw_response", "")
        )
        
        return {
            "name": name,
            "validation_id": validation_id,
            "constraint_checker": constraint_result,
            "claude_validation": claude_result,
            "processing_time": processing_time,
            "combined_score": combined_score,
            "compliant": constraint_result["compliant"] and len(claude_result["violations"]) == 0
        }
```

=== File: prototype\validation\validation_service.py (41 lines) ===

```python
from typing import Dict, Any
from validation.validation_orchestrator import ValidationOrchestrator
from testing.test_case_generator import TestCaseGenerator
from validation.constraint_checker import ConstraintChecker
from validation.claude_client import ClaudeClient

class ValidationService:
    def __init__(self):
        self.orchestrator = ValidationOrchestrator()
        self.generator = TestCaseGenerator()
        self.checker = ConstraintChecker()
        self.claude_client = ClaudeClient()
    
    def validate_file(self, file_path: str) -> Dict[str, Any]:
        try:
            with open(file_path, 'r') as f:
                code = f.read()
            return self._validate_code(code, file_path)
        except FileNotFoundError:
            return {"error": f"File not found: {file_path}"}
    
    def validate_code_input(self, code: str) -> Dict[str, Any]:
        return self._validate_code(code, "stdin_input")
    
    def _validate_code(self, code: str, name: str) -> Dict[str, Any]:
        constraint_result = self.checker.validate_code(code, name)
        claude_result = self.claude_client.validate_code(
            code, 
            ["File must be ≤150 lines", "No forbidden security patterns"]
        )
        
        return {
            "file_name": name,
            "constraint_validation": constraint_result,
            "claude_validation": claude_result,
            "overall_compliant": constraint_result["compliant"] and len(claude_result["violations"]) == 0
        }
    
    def run_benchmark_suite(self) -> Dict[str, Any]:
        test_cases = self.generator.create_test_cases()
        return self.orchestrator.run_validation_suite(test_cases)
```

=== File: prototype\validation\__init__.py (0 lines) ===

```python

```
