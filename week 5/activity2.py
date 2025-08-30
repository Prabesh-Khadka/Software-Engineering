class Student:
    def __init__(self, name, age):
        self.name = name       # public
        self._age = age        # protected
        self.__grade = 'A'     # private

    def get_grade(self):
        return self.__grade

class Course:    
    def course(self, course_id, course_name, Domain):
        self.__course_id = course_id  #private
        self.course_name = course_name #public
        self._Domain = Domain # protected
    
    def course_info(self):
        return self.__course_id
    
    # Setter for private variable
    def set_course_id(self, new_id):
        self.__course_id = new_id

s = Student('Ali', 20)
c1 = Course("C101", "Python Programming", "Computer Science")

print(c1.course_name)      #  Public → accessible
print(c1._domain)          #  Protected → works, but not recommended
print(c1.get_course_id())  #  Safe way to access private

c1.set_course_id("C202")   # Safe way to update private
print(c1.get_course_id())

print(s.name)         # accessible
print(s._age)         # discouraged
print(s.get_grade())  # correct way
