import sqlite3

def create_connection():
    conn = sqlite3.connect('requests.db')
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS help_requests (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            customer_name TEXT,
            question TEXT,
            status TEXT,
            answer TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Call create_table() once when starting
create_table()

def clear_help_requests():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM help_requests')
    conn.commit()
    conn.close()
