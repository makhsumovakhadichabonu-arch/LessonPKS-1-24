#новая тема
#lambda-анонимные функции - функции без имени
#встроенные функции map(), filter()
#импорты


def numMul(x, y):
    return x*y

print(numMul(5,8))

#lambda аргументы выражение
sq = lambda x,y: x*y
print(sq(4,7))
########
orders = ['Кофе','Чай', 'Молоко', 'Капучино', ' Коктейль']
# 1. Отфильтровать заказы длинне 4 символов 
# filter(условие, то к чему это устовие)
long_orders = list(filter(lambda order: len(order)>4, orders))
print(long_orders )
# 2. Заказы, начинающиеся на букву "К" показывать 
k_orders = list(filter(lambda order: order.upper(), orders))
print(k_orders)

# 1. Вывести только те блюда, где цена выше 150 сом 
# 2. Найти самое дорогое блюдо
# 3. отсортировать блюда по цене (от дешевых к дорогим)
# 4. Проверить, есть ли хоть одно бдюдо, где категории -"десерт"

orders = [
    {"название": "Кофе", "цена": 120, "категория": "напиток"},
    {"название": "Чай", "цена": 80, "категория": "напиток"},
    {"название": "Пирог", "цена": 150, "категория": "десерт"},
    {"название": "Салат", "цена":200, "категория": "основное"}
]
exp = list(filter(lambda x:x["цена"]>150, orders))
print(exp)
for i in exp:
    print(i)
2#
max_item= max(orders, key=lambda x:x['цена'])
print(max_item)
#3
sorted_orders = sorted(orders, key=lambda x: x["цена"])
print(sorted_orders)
#4
desert = any(map(lambda x:x['категория'].lower() == 'десерт', orders))
print(desert)
# sum() - суммируют числа
# map() - применяет функцию к каждому элементу
# filter() - оставляет только те элементы, где функция True
# sorted() - сортирует список по заданному правилу
# max() min() - максимальное и минимальное
# any() - проверяет есть ли хоть одно True или все True 
# zip() - Обьединяет списки в пары
# enumerate()-


products = [
    {"название": "Футболка", "цена": 800, "размер": "M", "категория": "мужская"},
    {"название": "Платье", "цена": 1500, "размер": "L", "категория": "женская"},
    {"название": "Куртка", "цена": 3500, "размер": "XL", "категория": "мужская"},
    {"название": "Шорты", "цена": 1200, "размер": "S", "категория": "детская"},
    {"название": "Джинсы", "цена": 2200, "размер": "L", "категория": "мужская"},
]

while True:
    print("""
1. Показать все товары
2. Добавить новый товар
3. Найти товары по категории
4. Найти самый дорогой товар
5. Отфильтровать товары дешевле заданной цены
6. Поднять цену всем товарам на 5%
7. Выйти из программы
""")

    choice = input("Выберите действие (1–7): ")

    if choice == "1":
        print(" Список всех товаров:")
        for item in products:
            print(item)

    elif choice == "2":
        name = input("Введите название товара: ")
        price = float(input("Введите цену: "))
        size = input("Введите размер: ")
        category = input("Введите категорию: ")
        products.append({"название": name, "цена": price, "размер": size, "категория": category})
        print("Товар добавлен!")

    elif choice == "3":
        cat = input("Введите категорию (мужская/женская/детская): ").lower()
        found = [p for p in products if p["категория"].lower() == cat]
        if found:
            print("Товары в категории", cat)
            for f in found:
                print(f)
        else:
            print(" Товары не найдены!")

    elif choice == "4":
        expensive = max(products, key=lambda x: x["цена"])
        print("Самый дорогой товар:", expensive)

    elif choice == "5":
        limit = float(input("Введите максимальную цену: "))
        filtered = list(filter(lambda x: x["цена"] < limit, products))
        if filtered:
            print(" Товары дешевле", limit, "сом:")
            for f in filtered:
                print(f)
        else:
            print("Таких товаров нет!")
 
    elif choice == "6":
        for p in products:
            p["цена"] *= 1.05  # увеличить на 5%
        print(" Цены всех товаров увеличены на 5%!")

    elif choice == "7":
        print(" Выход из программы.")
        break

    else:
        print(" Ошибка: введите число от 1 до 7.")
