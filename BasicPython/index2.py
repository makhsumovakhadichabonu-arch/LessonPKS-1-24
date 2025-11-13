# Задача: Система управление колледжем
# Ты пишешь программу, которая помагает колледжу управлять студентами, предметами и оценками.
# Сист. Вычислять средний балл каждого студента.
    # 5. Показывать топ студентов группы.
    # 6. ема должна уметь: 
    # 1. Регистрировать студентов (имя, группа, возраст).
    # 2. Добавлять предметы (название, преподаветель )
    # 3. Назначать оценки студентам по предметам.
    # 4Проверять кто подлежит отчисление (если средний балл < 50)

students = {}
subjects = {}

def add_student():
    name = input("Имя студента: ")
    group = input("Группа: ")
    age = int(input("Возраст: "))
    students[name] = {"группа": group, "возраст": age, "оценки": {}}
    print(f"Студент {name} зарегистрирован.\n")

def add_subject():
    name = input("Название предмета: ")
    teacher = input("Преподаватель: ")
    subjects[name] = teacher
    print(f"Предмет '{name}' добавлен (преподаватель: {teacher}).\n")

def add_mark():
    student_name = input("Введите имя студента: ")
    if student_name not in students:
        print("Такого студента нет!\n")
        return
    subject_name = input("Введите предмет: ")
    if subject_name not in subjects:
        print("Такого предмета нет!\n")
        return
    mark = int(input("Введите оценку (0-100): "))
    students[student_name]["оценки"][subject_name] = mark
    print(f"Оценка добавлена.\n")

def show_student_info():
    for name, info in students.items():
        print(f"Студент: {name}, Группа: {info['группа']}, Возраст: {info['возраст']}")
        for subject, mark in info["оценки"].items():
            print(f"  {subject}: {mark}")
        print()

def calculate_average():
    for name, info in students.items():
        marks = list(info["оценки"].values())
        if marks:
            avg = sum(marks)/len(marks)
            print(f"Средний балл студента {name}: {avg:.2f}")
        else:
            print(f"Студент {name} еще не имеет оценок.")

def show_top_students():
    group_name = input("Введите группу для топ студентов: ")
    group_students = {name: info for name, info in students.items() if info["группа"] == group_name}
    averages = []
    for name, info in group_students.items():
        marks = list(info["оценки"].values())
        if marks:
            avg = sum(marks)/len(marks)
            averages.append((name, avg))
    averages.sort(key=lambda x: x[1], reverse=True)
    print(f"Топ студентов группы {group_name}:")
    for name, avg in averages[:3]:
        print(f"{name} - {avg:.2f}")

def expel_students():
    for name, info in list(students.items()):
        marks = list(info["оценки"].values())
        if marks:
            avg = sum(marks)/len(marks)
            if avg < 50:
                print(f"Студент {name} подлежит отчислению (средний балл: {avg:.2f})")
while True:
    print("""
1. Регистрировать студентов
2. Добавлять предметы
3. Назначать оценки студентам
4. Вычислять средний балл каждого студента
5. Показывать топ студентов группы
6. Проверять кто подлежит отчисление
7. Выход
""")
    choice = input("Выберите пункт меню: ")
    if choice == '1':
        add_student()
    elif choice == '2':
        add_subject()
    elif choice == '3':
        add_mark()
    elif choice == '4':
        calculate_average()
    elif choice == '5':
        show_top_students()
    elif choice == '6':
        expel_students()
    elif choice == '7':
        break
    else:
        print("Выберите от 1 до 7.")