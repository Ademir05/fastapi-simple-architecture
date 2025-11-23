import sqlite3 
from pathlib import Path

def create_database():
    base_dir = Path(__file__).resolve().parent

    schema_path = base_dir / "docs/database/schema.sql"
    db_path = base_dir / "database.db"
    print(db_path)
    if db_path.exists():
        print("Database file already exists.")
        return
        
    ddl_sql = ""
    with open(schema_path, "r") as f:
        ddl_sql = f.read()

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.executescript(ddl_sql)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
