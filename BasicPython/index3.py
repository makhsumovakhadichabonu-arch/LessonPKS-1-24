# новая тема : работа с файлами
# mode - режим
# r - read- чтение
# w - write - писать- создание нового файла, старый очищает
# a - append - добавляеть 
# x - создание нового файла, но если есть такая то вызов ошибка 
# b - binary - используется вместе с rb и wb 
# t - текстовый режим по умолчанию
# open() функция во круг которого все крутится
# File = open("имя_файла", "режим")
# запись файла
# with open('data.txt', 'w', encoding='utf-8') as file:
#     file.write("Урок по теме работе с файлами\n")
#     file.write("Шодияна в шарфе\n")
#     file.write("Абдулвадуд сегодня пришел")
  
# чтение файла
while True:
    print("""
1. Добавляет заметку в файл
2. Показывает все заметки
3. Ищет заметку по слову 
4. Заканчивает работу
""")
    choice = input("Выберите действие: ")

    if choice == '1':
        textUser = input("Что хотите добавить? ")
        with open('bloknot.txt', 'a', encoding='utf-8') as file:
            file.write(f"{textUser}\n")
        print("Заметка добавлена!")

    elif choice == '2':
        try:
            with open('bloknot.txt', 'r', encoding='utf-8') as file:
                content = file.read()
            print("\nВсе заметки:")
            print(content)
        except FileNotFoundError:
            print("Файл пустой или не существует.")

    elif choice == '3':
        search = input("Что ищете? ").lower()
        found = False
        try:
            with open('bloknot.txt', 'r', encoding='utf-8') as file:
                for line in file:
                    if search in line.lower():
                        print("Найдено:", line.strip())
                        found = True
            if not found:
                print("Нет такой заметки.")
        except FileNotFoundError:
            print("Файл пустой или не существует.")

    elif choice == '4':
        print("Выход из программы.")
        break

    else:
        print("Выбирайте от 1 до 4.")
