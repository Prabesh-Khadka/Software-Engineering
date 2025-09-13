import time
from database import create_connection, create_table

class Student:
    def __init__(self):
        self.connection = create_connection()

    def get_students(self, id=None):
        with self.connection as conn:
            cursor = conn.cursor()
            if id is None:
                cursor.execute("SELECT * FROM Student")
            else:
                cursor.execute("SELECT * FROM Student WHERE id=?", (id,))
            result = cursor.fetchall()
        return result

class Lecturer:
    def __init__(self):
        self.connection = create_connection()

    def get_lecturers(self, id=None):
        with self.connection as conn:
            cursor = conn.cursor()
            if id is None:
                cursor.execute("SELECT * FROM Lecturer")
            else:
                cursor.execute("SELECT * FROM Lecturer WHERE id=?", (id,))
            result = cursor.fetchall()
        return result

def main():
    create_table()  # Ensure tables are created before querying
    student = Student()
    lecturer = Lecturer()

    start_time = time.perf_counter()
    students = student.get_students()  # call on instance, not class
    end_time = time.perf_counter()
    print(f"Student Query Execution Time: {end_time - start_time:8f} seconds")
    print(f"Number of students retrieved: {len(students)}")

    start_time = time.perf_counter()
    lecturers = lecturer.get_lecturers()  # call on instance, not class
    end_time = time.perf_counter()
    print(f"Lecturer Query Execution Time: {end_time - start_time:.8f} seconds")
    print(f"Number of lecturers retrieved: {len(lecturers)}")

if __name__ == "__main__":
    main()
