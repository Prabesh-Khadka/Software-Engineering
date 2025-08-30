# Base class (common attributes)
class Person:
    def __init__(self, name, address, age, person_id):
        self.name = name
        self.address = address
        self.age = age
        self.person_id = person_id

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, ID: {self.person_id}")
        print(f"Address: {self.address}")


# Derived class: Student
class Student(Person):
    def __init__(self, name, address, age, person_id, academic_record):
        super().__init__(name, address, age, person_id)
        self.academic_record = academic_record

    def display_info(self):
        super().display_info()
        print(f"Academic Record: {self.academic_record}")


# Derived class: Academic Staff
class Academic(Person):
    def __init__(self, name, address, age, person_id, tax_code, salary):
        super().__init__(name, address, age, person_id)
        self.tax_code = tax_code
        self.salary = salary

    def display_info(self):
        super().display_info()
        print(f"Tax Code: {self.tax_code}, Salary: {self.salary}")


# Derived class: General Staff
class GeneralStaff(Person):
    def __init__(self, name, address, age, person_id, tax_code, pay_rate):
        super().__init__(name, address, age, person_id)
        self.tax_code = tax_code
        self.pay_rate = pay_rate

    def display_info(self):
        super().display_info()
        print(f"Tax Code: {self.tax_code}, Pay Rate: {self.pay_rate}")


# Example usage
s1 = Student("Siman", "123 Street", 20, "S001", "GPA: 3.8")
a1 = Academic("Dr. Anjan", "456 Avenue", 45, "A123", "TAX789", 85000)
g1 = GeneralStaff("Marley", "789 Road", 35, "G456", "TAX456", 25.5)

s1.display_info()
print()
a1.display_info()
print()
g1.display_info()
