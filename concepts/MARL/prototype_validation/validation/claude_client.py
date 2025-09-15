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