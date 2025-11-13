class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.is_available = True

    def borrow(self):
        if self.is_available:
            self.is_available:False
            return self.is_available
        
    def return_book(self):
         self.is_available:True
         return self.is_available

    def info(self):
         return f"Название: {self.title}, Автор: {self.author}, Год: {self.year}, Доступность: {self.is_available}"
    
book1 =Book('Война и мир', "Лев Толстой", 1867) # экземпляр
book1.borrow()
message = book1.info
print(message)
book1.return_book()
message = book1.info()
print(message)



# 2) Создай класс Student и класс Course
# класс Student
# name
# group
# метод enroll(course) — записывает студента на курс
# класс Course
# name
# students — список студентов
# метод add_student(student) — добавляет студента в курс
class Student:
    def __init__(self, name,group):
        self.name = name
        self.group = group
        self.courses = []

    def enroll(self,course):
        self.courses.append(course)
        course.add_student(self)  
        print(f"{self.name} записан на курс {course.name}")
class Course:
    def __init__(self, name, ):
        self.name = name
        self.students = []

    def add_student(self,student):
        self.students.append(student)
        print(f"{student.name} добавлен в курс {self.name}")

math_course = Course('Математика')
physics_course = Course('Физика')
student1 = Student('Хадичабону ', "B1")
student2 = Student('Айжамал', "A2")
student1.enroll(math_course)
student2.enroll(physics_course)
print(" Студенты курса Математика\n:")
for s in math_course.students:
    print(s.name)

print(" Студенты курса Физика\n:")
for s in physics_course.students:
    print(s.name)

