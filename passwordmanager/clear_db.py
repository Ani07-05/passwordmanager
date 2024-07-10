import sqlite3

def clear_db(db_path):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Enable writable schema
    cursor.execute("PRAGMA writable_schema = 1;")
    # Delete all tables, indexes, and triggers
    cursor.execute("DELETE FROM sqlite_master WHERE type IN ('table', 'index', 'trigger');")
    # Disable writable schema
    cursor.execute("PRAGMA writable_schema = 0;")
    
    # Commit the transaction
    conn.commit()
    
    # Run VACUUM outside of the transaction
    cursor.execute("VACUUM;")

    conn.close()

if __name__ == "__main__":
    db_path = "database.db"  # Replace with the path to your database file
    clear_db(db_path)
