# Задание: СИСТЕМА УПРАВЛЕНИЕ КУХНЕЙ РЕСТОРАНА
# 1. Добавлять блюда в меню (name, цена, сложность приготовления от 1 до 5).
# 3. Регистрировать поваров (имя, уповень мастерства от 1 до 5).
# 3. Создавать заказы (гость заказывает блюда из меню).
# 4. Определять, может ли повар приготовить заказ (если его мастерство>  сложности блюда).
# 5. Считать общую сумму заказа и показывать итог.
menu = {
    "Паста": {"цена": 400, "сложность": 3},
    "Стейк": {"цена": 900, "сложность": 5},
}

chefs = {
    "Айбек": {"уровень": 4},
    "Марина": {"уровень": 5}
}

orders = []

while True:
    print("\nВыберите действие:")
    print("1. Добавить блюдо в меню")
    print("2. Зарегистрировать повара")
    print("3. Создать заказ")
    print("4. Проверить, может ли повар приготовить заказ")
    print("5. Рассчитать сумму заказа и показать итог")
    print("6. Выйти")
    
    choice = input("Ваш выбор: ")
    
    if choice == '1':
        name = input("Введите название блюда: ")
        price = int(input("Введите цену блюда: "))
        difficulty = int(input("Введите сложность (1-5): "))
        menu[name] = {"цена": price, "сложность": difficulty}
        print(f"Блюдо {name} добавлено в меню!")
    
    elif choice == '2':
        chef_name = input("Введите имя повара: ")
        level = int(input("Введите уровень мастерства (1-5): "))
        chefs[chef_name] = {"уровень": level}
        print(f"Повар {chef_name} зарегистрирован!")
    
    elif choice == '3':
        guest = input("Введите имя гостя: ")
        print("Доступные блюда в меню:")
        for dish in menu:
            print(f"- {dish}")
        dishes = input("Введите блюда через запятую: ").split(",")
        dishes = [d.strip().capitalize() for d in dishes]  # убираем пробелы и делаем с заглавной буквы
        chef = input("Назначьте повара: ")
        orders.append({"гость": guest, "блюда": dishes, "повар": chef})
        print(f"Заказ от {guest} добавлен!")
    
    elif choice == '4':
        order_index = int(input(f"Введите номер заказа (0-{len(orders)-1}): "))
        order = orders[order_index]
        chef_name = order["повар"]
        can_cook = True
        for dish in order["блюда"]:
            if dish not in menu:
                print(f" Блюдо {dish} нет в меню!")
                can_cook = False
            elif chefs[chef_name]["уровень"] < menu[dish]["сложность"]:
                print(f" Повар {chef_name} не может приготовить {dish}")
                can_cook = False
        if can_cook:
            print(f" Повар {chef_name} может приготовить весь заказ для {order['гость']}")
    
    elif choice == '5':
        order_index = int(input(f"Введите номер заказа (0-{len(orders)-1}): "))
        order = orders[order_index]
        total = 0
        for dish in order["блюда"]:
            if dish in menu:
                total += menu[dish]["цена"]
        print(f"Итоговая сумма заказа для {order['гость']}: {total} сом")
    
    elif choice == '6':
        print("Выход из программы")
        break
    
    else:
        print("Некорректный выбор, попробуйте снова")
