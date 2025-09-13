import sqlite3

def create_connection():
    conn = sqlite3.connect("DBMS.db")
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")  # Enable foreign keys
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()

    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Student (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                address TEXT NOT NULL,
                courses_id INTEGER,
                section_id INTEGER,
                FOREIGN KEY(courses_id) REFERENCES Courses(id),
                FOREIGN KEY(section_id) REFERENCES Section(id)
            )                       
        ''')
        print("Create Student table Successfully")
    except sqlite3.Error as e:
        print(f"Student table creation failed: {e}")

    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Lecturer (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                highest_designation TEXT NOT NULL,
                courses_id INTEGER,
                Student_id INTEGER,
                FOREIGN KEY(courses_id) REFERENCES Courses(id),
                FOREIGN KEY(Student_id) REFERENCES Student(id)
            )                       
        ''')
        print("Create Lecturer table Successfully")
    except sqlite3.Error as e:
        print(f"Lecturer table creation failed: {e}")

    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Courses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                type TEXT NOT NULL UNIQUE,
                courses_subjects TEXT NOT NULL,
                lecturer_id INTEGER,
                FOREIGN KEY(lecturer_id) REFERENCES Lecturer(id)
            )                       
        ''')
        print("Create Courses table Successfully")
    except sqlite3.Error as e:
        print(f"Courses table creation failed: {e}")    

    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Section (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                courses_id INTEGER,
                student_id INTEGER,
                FOREIGN KEY(courses_id) REFERENCES Courses(id),
                FOREIGN KEY(student_id) REFERENCES Student(id)
            )                       
        ''')
        print("Create Section table Successfully")
    except sqlite3.Error as e:
        print(f"Section table creation failed: {e}")

    conn.commit()
    conn.close()
    print("All Tables created successfully")

def print_table():
    conn = create_connection()
    cursor = conn.cursor()
    tables = ["Student", "Lecturer", "Courses", "Section"]
    for table in tables:
        try:
            cursor.execute(f"SELECT * FROM {table}")
            rows = cursor.fetchall()
            print(f"\nContents of {table} table:")
            for row in rows:
                print(row)
        except sqlite3.Error as e:
            print(f"Failed to retrieve data from {table} table: {e}")
    conn.close()

# Make sure to call create_table() when script runs
if __name__ == "__main__":
    create_table()
    print_table()
