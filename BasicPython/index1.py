# Задача: Система управление колледжем
# Ты пишешь программу, которая помагает колледжу управлять студентами, предметами и оценками.
# Система должна уметь: 
# 1. Регистрировать студентов (имя, группа, возраст).
# 2. Добавлять предметы (название, преподаветель )
# 3. Назначать оценки студентам по предметам.
# 4. Вычислять средний балл каждого студента.
# 5. Показывать топ студентов группы.
# 6. Проверять кто подлежит отчисление (если средний балл < 50)

def add_students(students):
    name = input("Введите имя студента: ").title().strip()
    group = input("Введите группу: ").upper()
    try:
      age = int(input("Введите возраст: "))
    except ValueError:
        print("Вводите только числа")
        return
    if name in students:
        print("такой уже существует")
        return
    students[name] = {"группа": group, "возраст": age, "оценки": {}}
    print(f"Студент {name} успешно зарегистрирован.")


def add_subject(subjects):
    name = input("Введите название предмета: ")
    teacher = input("Введите имя преподавателя: ")
    if name in subjects:
        print("Такой предмет уже есть")
        return
    subjects[name] = teacher
    print(f" Предмет '{name}' добавлен (преподаватель: {teacher}).")


def add_mark(students, subjects):
    name = input("Введите имя студента: ").title().strip()
    if name not in students:
        print("такого студента нет")
        return
    subject = input("Выбрыть предмет: ").title().strip()
    if subject not in students:
        print("Нет такого предмета")
        return
    try:
        mark = int(input("Введите оценку (0-100): "))
    except ValueError:
        print("Ошибка! введите только число")
        return
    if mark < 0 or mark > 100:
        print("Оценка должна быть от 0 до 100")
        return
    students[name]["оценки"][subjects] = mark
    print(f"{name} получил {mark} по предмету")

def calculate_average(marks):
    if not marks:
        return 0
    return sum(marks.values()) / len(marks)


def show_student_info(students):
    name = input("Введите имя студента: ")
    if name not in students:
        print(" Студент не найден.\n")
        return

    info = students[name]
    avg = calculate_average(info["оценки"])
    print(f"\n Имя: {name}")
    print(f"Группа: {info['группа']}")
    print(f"Возраст: {info['возраст']}")
    print("Оценки:")
    for subject, mark in info["оценки"].items():
        print(f"  {subject}: {mark}")
    print(f"Средний балл: {avg:.2f}\n")


def show_top_students(students):
    group = input("Введите название группы: ")
    group_students = {n: calculate_average(s["оценки"]) for n, s in students.items() if s["группа"] == group}

    if not group_students:
        print(" В этой группе нет студентов.\n")
        return

    sorted_students = sorted(group_students.items(), key=lambda x: x[1], reverse=True)
    print(f"\nТоп студентов группы {group}:")
    for name, avg in sorted_students:
        print(f"{name}: {avg:.2f}")
    print()


def expel_students(students):
    print("\n Студенты, подлежащие отчислению (средний балл < 50):")
    expelled = False
    for name, info in students.items():
        avg = calculate_average(info["оценки"])
        if avg < 50:
            print(f"{name} — {avg:.2f}")
            expelled = True
    if not expelled:
        print(" Таких студентов нет.\n")


students = {}
subjects = {}

while True:
    print("""
1. Регистрировать студентов
2. Добавлять предметы
3. Назначать оценки студентам
4. Показать информацию о студенте
5. Показать топ студентов группы
6. Проверить на отчисление
0.  Проверять кто подлежит отчисление (если средний балл < 50)
""")

    choice = input("Выберите пункт меню: ")

    if choice == '1':
        add_students(students)
    elif choice == '2':
        add_subject(subjects)
    elif choice == '3':
        add_mark(students, subjects)
    elif choice == '4':
        show_student_info(students)
    elif choice == '5':
        show_top_students(students)
    elif choice == '6':
        expel_students(students)
    elif choice == '0':
        print(" Выход из программы. До свидания!")
        break
    else:
        print("Ошибка! Выберите пункт из меню")
