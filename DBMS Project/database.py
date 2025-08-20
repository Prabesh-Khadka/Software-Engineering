import sqlite3

def create_connection():
    conn = sqlite3.connect("project.db")
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
        print("Create Student table Sucessfully")
    except sqlite3.Error as e:
        print(f"Student table creation failed:{e}")

    try:
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS Lecturer (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            highest_designation TEXT NOT NULL,
            courses_id INTEGER,
            FOREIGN KEY(courses_id) REFERENCES Courses(id)
            )                       
        ''')
    except sqlite3.Error as e:
        print(f"Lecturer table creation failed:{e}")

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
    except sqlite3.Error as e:
        print(f"Courses table creation failed:{e}")    

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
    except sqlite3.Error as e:
        print(f"Section table creation failed:{e}")

    conn.commit()
    conn.close()
    print("All Table created Sucessfully")