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