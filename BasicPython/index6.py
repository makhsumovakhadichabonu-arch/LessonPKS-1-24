# Задание: СИСТЕМА УПРАВЛЕНИЕ КУХНЕЙ РЕСТОРАНА
# 1. Добавлять блюда в меню (name, цена, сложность приготовления от 1 до 5).
# 3. Регистрировать поваров (имя, уповень мастерства от 1 до 5).
# 3. Создавать заказы (гость заказывает блюда из меню).
# 4. Определять, может ли повар приготовить заказ (если его мастерство>  сложности блюда).
# 5. Считать общую сумму заказа и показывать итог.
menu = {
    "Паста": {"цена": 400, "сложность": 3},
    "Стейк": {"цена": 900, "сложность": 5},}
chefs = {
    "Айбек": {"уровень": 4},
    "Марина": {"уровень": 5}}
orders = [
    {"гость": "Канат", "блюда": ["паста","стейк"], "повар": "Марина"}
]
def add_dish(name, price, difficulty):
        menu[name] = {"цена": price, "сложность": difficulty}
        print(f"Блюдо '{name}' добавлено в меню!")
def add_chef(name, level):
        chefs[name] = {"уровень": level}
        print(f"Повар {name} добавлен с уровнем мастерства {level}." )
def can_cook(chef_name, dish_name):
        chef_level = chefs[chef_name]["уровень"]
        dish_difficulty = menu[dish_name]["сложность"]
        return chef_level >= dish_difficulty
def can_cook(chef_name, dish_name):
        chef_level = chefs[chef_name]["уровень"]
        dish_difficulty = menu[dish_name]["сложность"]
        return chef_level >= dish_difficulty

def make_order(guest, dish_list, chef_name):
    print(f"\nГость: {guest}")
    print(f"Повар: {chef_name}")
    total = 0

    for dish in dish_list:
        dish_cap = dish.capitalize()
        if dish_cap in menu:
            if can_cook(chef_name, dish_cap):
                price = menu[dish_cap]["цена"]
                total += price
                print(f" {dish_cap} — {price} сом (повар может приготовить)")
            else:
                print(f" {dish_cap} — слишком сложно для этого повара!")
        else:
            print(f" {dish_cap} — такого блюда нет в меню!")

    print(f"\n Общая сумма заказа: {total} сом\n")

make_order("Канат", ["паста", "стейк"], "Марина")
make_order("Алия", ["суп", "стейк"], "Айбек")