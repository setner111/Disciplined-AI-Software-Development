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