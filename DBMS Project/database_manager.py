from database import create_connection
import sqlite3 

DB_NAME = "DBMS.db"

def create_connection():
    return sqlite3.connect(DB_NAME)

# ---------- CRUD FUNCTIONS ---------- #

# Insert data
def insert_Student(name, email, address, courses_id, section_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Student (name, email, address, courses_id, section_id) VALUES (?, ?, ?, ?, ?)", 
                   (name, email, address, courses_id, section_id))
    conn.commit()
    print("Information inserted Sucessfully:")
    conn.close()

def insert_Lecturer(name, email, highest_designation, courses_id, student_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Lecturer (name, email, highest_designation, courses_id, student_id) VALUES (?, ?, ?, ?, ?)", 
                   (name, email, highest_designation, courses_id, student_id))
    conn.commit()
    print("Information inserted Sucessfully:")
    conn.close()

def insert_Courses(type, courses_subjects, lecturer_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Courses (type, courses_subjects, lecturer_id) VALUES (?, ?, ?)", 
                   (type, courses_subjects, lecturer_id))
    conn.commit()
    print("Information inserted Sucessfully:")
    conn.close()

def insert_Section(courses_id, student_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Section (courses_id, student_id) VALUES (?, ?)", 
                   (courses_id, student_id))
    conn.commit()
    print("Information inserted Sucessfully:")
    conn.close()

# View records
def view_table(table_name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    conn.close()
    return rows

# Update records
def update_record(table, column, new_value, record_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(f"UPDATE {table} SET {column}=? WHERE id=?", (new_value, record_id))
    conn.commit()
    conn.close()

# Delete records
def delete_record(table, record_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM {table} WHERE id=?", (record_id,))
    conn.commit()
    conn.close()

