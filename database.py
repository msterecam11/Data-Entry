import sqlite3 
def create_table():
    conn = sqlite3.connect('courses.db')
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Courses (
            id TEXT PRIMARY KEY,
            name TEXT,
            duration TEXT,
            format TEXT,
            language TEXT,
            price INTEGER)''')
    conn.commit()
    conn.close()

def insert_course(id, name, duration, format, language, price):
    conn = sqlite3.connect('Courses.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO Courses (id, name, duration, format, language, price ) VALUES (?, ?, ?, ?, ?, ?)',
                   (id, name, duration, format, language, price))
    conn.commit()
    conn.close()

def search_course(query):
    conn = sqlite3.connect('Courses.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Courses WHERE id = ?', (query,))
    row =  cursor.fetchone()
    conn.close()
    return row
def fetch_all_ids():
     conn = sqlite3.connect('Courses.db')
     cursor = conn.cursor()
     cursor.execute('SELECT id FROM Courses')
     ids = cursor.fetchall()
     conn.close()
     return [i[0] for i in ids]

def id_exists(id):
    conn = sqlite3.connect('Courses.db')
    cursor =  conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM Courses WHERE id = ?', (id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] > 0

create_table()