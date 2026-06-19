import sqlite3

# Connect to database (creates file if not exists)
conn = sqlite3.connect("learning_tutor.db")

# Create cursor
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    course TEXT
)
""")

print("Database created successfully")

# Close connection
conn.commit()
conn.close()
