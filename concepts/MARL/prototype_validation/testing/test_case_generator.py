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