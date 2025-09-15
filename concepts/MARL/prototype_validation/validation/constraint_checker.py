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