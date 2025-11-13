# 1) Вам нужно проверить начало или конец строки на присутствие неких текстовых шаблонов, таких как расширения файлов, схемы URL и т. д.
filename = 'spam.txt'
url = 'http://www.python.org&#39'
#2) Написать функцию "угадай число", использую import random, пользователь должен отгадать число что задает компьтер, компьютер задает число от 1 до 100. Например, компьтер загадал число 10, а человек ввел число 50, то мы должны писать ему "число должно быть ниже" и наоборот, а если угадал то выводим "молодец" и показать сколько попыток он сделал
# 3) Генератор пароля
# Создайте функцию, которая генерирует случайный пароль длиной N символов. Используйте модуль random и буквы/цифры/специальные символы.
# 4)Проверка палиндрома. Напишите функцию, которая проверяет, является ли введённая строка палиндромом (читается одинаково с начала и с конца).


# ЗАДАНИЕ: СИСТЕМА УПРАВЛЕНИЯ КУХНЕЙ РЕСТОРАНА
# 1. Добавлять блюда в меню (name, цена, сложность приготовления от 1 до 5).
# 2. Регистрировать поваров (имя, уровень мастерства от 1 до 5).
# 3. Создавать заказы (гость заказывает блюда из меню).
# 4. Определять, может ли повар приготовить заказ (если его мастерство ≥ сложности блюда).
# 5. Считать общую сумму заказа и показывать итог.
menu = {
"Паста": {"цена": 400, "сложность": 3},
"Стейк": {"цена": 900, "сложность": 5}}
chefs = {
"Айбек": {"уровень": 4},
"Марина": {"уровень": 5}}
orders = [
{"гость": "Канат", "блюда": ["Паста", "Стейк"], "повар": "Марина"}
]
#1
filename = 'spam.txt'
url = 'http://www.python.org'

# Проверяем, чем заканчивается или начинается строка
if filename.endswith('.txt'):
    print("Это текстовый файл (.txt)")

if url.startswith('http://') or url.startswith('https://'):
    print("Это ссылка (URL)")
#2
import random

def guess_number():
    secret = random.randint(1, 100)
    tries = 0

    print("Я загадал число от 1 до 100. Попробуй угадать!")

    while True:
        guess = int(input("Твоё число: "))
        tries += 1

        if guess < secret:
            print(" Число должно быть больше!")
        elif guess > secret:
            print(" Число должно быть ниже!")
        else:
            print(f" Молодец! Ты угадал за {tries} попыток!")
            break

guess_number()
#3
import random
import string

def generate_password(length):
    symbols = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(symbols) for _ in range(length))
    return password

print("Ваш пароль:", generate_password(10))
#4
def is_palindrome(text):
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]

word = input("Введите слово: ")
if is_palindrome(word):
    print(" Это палиндром!")
else:
    print(" Это не палиндром.")
#5
menu = {
    "Паста": {"цена": 400, "сложность": 3},
    "Стейк": {"цена": 900, "сложность": 5}
}

chefs = {
    "Айбек": {"уровень": 4},
    "Марина": {"уровень": 5}
}

orders = []

def add_dish():
    name = input("Введите название блюда: ")
    price = int(input("Введите цену блюда: "))
    level = int(input("Введите сложность приготовления (1–5): "))
    menu[name] = {"цена": price, "сложность": level}
    print(f"Блюдо {name} добавлено!")

def add_chef():
    name = input("Имя повара: ")
    level = int(input("Уровень мастерства (1–5): "))
    chefs[name] = {"уровень": level}
    print(f" Повар {name} зарегистрирован!")

def create_order():
    guest = input("Имя гостя: ")
    dishes = input("Введите блюда через запятую: ").split(",")
    dishes = [d.strip() for d in dishes]

    chef_name = input("Введите имя повара: ")

    if chef_name not in chefs:
        print("Такого повара нет!")
        return

    chef_level = chefs[chef_name]["уровень"]
    total = 0
    can_cook_all = True

    for dish in dishes:
        if dish not in menu:
            print(f" Блюдо '{dish}' отсутствует в меню.")
            can_cook_all = False
            continue

        if chef_level < menu[dish]["сложность"]:
            print(f"{chef_name} не может приготовить '{dish}' (сложность выше уровня).")
            can_cook_all = False

        total += menu[dish]["цена"]

    orders.append({"гость": guest, "блюда": dishes, "повар": chef_name, "итог": total})

    if can_cook_all:
        print(f"Заказ для {guest} готов! Сумма: {total} сом")
    else:
        print(f"Заказ не может быть полностью выполнен ({guest}).")

def show_orders():
    print("\n Все заказы:")
    for order in orders:
        print(f"{order['гость']} → {order['блюда']} (повар: {order['повар']}, сумма: {order['итог']} сом)")


# Меню управления
while True:
    print("\n1. Добавить блюдо\n2. Добавить повара\n3. Создать заказ\n4. Показать заказы\n5. Выход")
    choice = input("Выберите действие: ")

    if choice == "1":
        add_dish()
    elif choice == "2":
        add_chef()
    elif choice == "3":
        create_order()
    elif choice == "4":
        show_orders()
    elif choice == "5":
        print(" Программа завершена.")
        break
    else:
        print("Неверный выбор.")
