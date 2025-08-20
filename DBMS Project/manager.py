from database import create_table
from database_manager import insert_Student, insert_Lecturer, insert_Courses, insert_Section, view_table, update_record, delete_record

def manager():
    while True:
        print("\n--- DATABASE MANAGER ---")
        print("1. Insert Student")
        print("2. Insert Lecturer")
        print("3. Insert Course")
        print("4. Insert Section")
        print("5. View Table")
        print("6. Update Record")
        print("7. Delete Record")
        print("8. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter Student Name: ")
            email = input("Enter Student Email: ")
            address = input("Enter Address: ")
            course_id = input("Enter Course ID: ")
            section_id = input("Enter Section ID: ")
            insert_Student(name, email, address, course_id, section_id)
            print("Student inserted successfully!")

        elif choice == "2":
            name = input("Enter Lecturer Name: ")
            email = input("Enter Lecturer Email: ")
            designation = input("Enter Designation: ")
            course_id = input("Enter Course ID: ")
            insert_Lecturer(name, email, designation, course_id)
            print("Lecturer inserted successfully!")

        elif choice == "3":
            ctype = input("Enter Course Type: ")
            subjects = input("Enter Course Subjects: ")
            lecturer_id = input("Enter Lecturer ID: ")
            insert_Courses(ctype, subjects, lecturer_id)
            print("Course inserted successfully!")

        elif choice == "4":
            course_id = input("Enter Course ID: ")
            student_id = input("Enter Student ID: ")
            insert_Section(course_id, student_id)
            print("Section inserted successfully!")

        elif choice == "5":
            table = input("Enter table name (Student/Lecturer/Courses/Section): ")
            rows = view_table(table)
            for row in rows:
                print(row)

        elif choice == "6":
            table = input("Enter table name: ")
            column = input("Enter column name to update: ")
            new_value = input("Enter new value: ")
            record_id = input("Enter record ID: ")
            update_record(table, column, new_value, record_id)
            print("Record updated successfully!")

        elif choice == "7":
            table = input("Enter table name: ")
            record_id = input("Enter record ID: ")
            delete_record(table, record_id)
            print("Record deleted successfully!")

        elif choice == "8":
            print("Exiting Manager...")
            break

        else:
            print("Invalid choice! Try again.")

# Run the manager
if __name__ == "__main__":
    manager()
