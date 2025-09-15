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