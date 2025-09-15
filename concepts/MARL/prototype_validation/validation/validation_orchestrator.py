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