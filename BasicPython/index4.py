    
#    задача: "Учет заказов ресторана"
#   Условие: Напиши программу, которая:
# 1. Добавляет заказ (блюдо, количество, цена)
# 2. Показывает все заказы
# 3. Ишет заказы по название блюда
# 4. Подсчитывает  общую выручку
# 5. Завершает работу по выбору пользователя
# Все данные сохраняются в файле orders.txt.
import os
if not os.path.exists('orders.txt'):
    open('orders.txt', 'w', encoding='utf-8').close()

while True:
    print(""" 
1. Добавляет заказ (блюдо, количество, цена)
2. Показывает все заказы
3. Ищет заказы по названию блюда
4. Подсчитывает общую выручку
5. Завершает работу
""")

    choice = input("Выберите действие: ")

    if choice == '1':
        dish = input("Какое блюдо: ")
        quantity = int(input("Сколько: "))
        price = int(input("Какая цена: ")) 
        total = quantity * price
        with open('orders.txt', 'a', encoding="utf-8") as file:
            file.write(f"{dish},{quantity},{price},{total}\n")
        print("Заказ добавлен!")

    elif choice == '2':
        with open('orders.txt', 'r', encoding='utf-8') as file:
            content = file.read()
            if content.strip() == "":
                print("Заказов пока нет.")
            else:
                print("Все заказы:\n", content)

    elif choice == '3':
        search = input("Введите название блюда: ")
        found = False
        with open('orders.txt', 'r', encoding='utf-8') as file:
            for line in file:
                if search.lower() in line.lower():
                    print("Найдено:", line.strip())
                    found = True
        if not found:
            print("Нет такого блюда")

    elif choice == '4':
        total_income = 0
        with open('orders.txt', 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 4:
                    total_income += float(parts[3])
        print(f"Общая выручка: {total_income} сом")

    elif choice == '5':
        print("Программа завершена.")
        break

    else:
        print("Неверный выбор, попробуйте снова.")
