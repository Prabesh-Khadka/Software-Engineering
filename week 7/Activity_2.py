import time
from database import create_connection, create_table
from Singletondb import SingletonConnection



# ------------------------------
class StudentWithoutSingleton:
    def __init__(self):
        self.connection = create_connection()

    def get_students(self):
        with self.connection as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Student")
            return cursor.fetchall()


class LecturerWithoutSingleton:
    def __init__(self):
        self.connection = create_connection()

    def get_lecturers(self):
        with self.connection as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Lecturer")
            return cursor.fetchall()


# ------------------------------
class StudentWithSingleton:
    def __init__(self):
        self.connection = SingletonConnection().get_connection()

    def get_students(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Student")
        return cursor.fetchall()


class LecturerWithSingleton:
    def __init__(self):
        self.connection = SingletonConnection().get_connection()

    def get_lecturers(self):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Lecturer")
        return cursor.fetchall()


# ------------------------------

def main():
    create_table()  # ensure tables exist

    print("\n--- Without Singleton Pattern ---")
    s1 = StudentWithoutSingleton()
    l1 = LecturerWithoutSingleton()

    start = time.perf_counter()
    students_wo = s1.get_students()
    end = time.perf_counter()
    print(f"Student (no singleton) time: {end - start:.6f}s | Records: {len(students_wo)}")

    start = time.perf_counter()
    lecturers_wo = l1.get_lecturers()
    end = time.perf_counter()
    print(f"Lecturer (no singleton) time: {end - start:.6f}s | Records: {len(lecturers_wo)}")

    print("\n--- With Singleton Pattern ---")
    s2 = StudentWithSingleton()
    l2 = LecturerWithSingleton()

    start = time.perf_counter()
    students_sg = s2.get_students()
    end = time.perf_counter()
    print(f"Student (singleton) time: {end - start:.6f}s | Records: {len(students_sg)}")

    start = time.perf_counter()
    lecturers_sg = l2.get_lecturers()
    end = time.perf_counter()
    print(f"Lecturer (singleton) time: {end - start:.6f}s | Records: {len(lecturers_sg)}")

    print("\n✅ Comparison Complete")


if __name__ == "__main__":
    main()
