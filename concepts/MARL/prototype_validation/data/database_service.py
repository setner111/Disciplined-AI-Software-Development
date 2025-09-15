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