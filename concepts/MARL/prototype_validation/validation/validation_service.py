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