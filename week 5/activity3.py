# Student class
class Student:
    def __init__(self, name, age):
        self.name = name       # public
        self._age = age        # protected
        self.__grade = 'A'     # private

    # Getter for private attribute
    def get_grade(self):
        return self.__grade

    # New method using private attribute
    def is_passing(self):
        # Assume A, B, C are passing
        return self.__grade in ['A', 'B', 'C']


# Course class
class Course:    
    def __init__(self, course_id, course_name, domain):
        self.__course_id = course_id   # private
        self.course_name = course_name # public
        self._domain = domain          # protected
    
    def course_info(self):
        return f"Course ID: {self.__course_id}, Name: {self.course_name}, Domain: {self._domain}"
    
    # Setter for private variable
    def set_course_id(self, new_id):
        self.__course_id = new_id
    
    # Getter for private variable
    def get_course_id(self):
        return self.__course_id


# New class to demonstrate public and protected access for the public and protected attributes
class University:
    def __init__(self, student, course):
        self.student = student
        self.course = course

    def show_student_course(self):
        print(f"Student Name (public): {self.student.name}")       # public → accessible
        print(f"Student Age (protected): {self.student._age}")    # protected → accessible but discouraged
        print(f"Course Name (public): {self.course.course_name}") # public → accessible
        print(f"Course Domain (protected): {self.course._domain}") # protected → accessible but discouraged


# Using the classes
s = Student('Ali', 20)
c1 = Course("C101", "Python Programming", "Computer Science")

# Accessing public and private methods/attributes
print(c1.course_name)      # Public -- accessible
print(c1.get_course_id())  # Private -- safe access
c1.set_course_id("C202")   # Update private
print(c1.get_course_id())

print(s.name)         # public
print(s._age)         # protected -- discouraged
print(s.get_grade())  # private -- correct way
print(s.is_passing()) # new method using private

# Using University class to access public/protected attributes
uni = University(s, c1)
uni.show_student_course()
