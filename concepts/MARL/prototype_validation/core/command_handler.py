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