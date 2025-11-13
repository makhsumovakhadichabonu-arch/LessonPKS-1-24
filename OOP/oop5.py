# создайте программу для комп клуба, которая будет спрашивать играл ли этот человек наше игру, если "нет" не играл, тогда регистрируется, он создает себе логин и пароль, и этот логин и пароль мы записываем к себе в список, а если он скажет, что у нас играл, мы проверить свой список клиентов, если он там есть, скажем "Добро пожаловать в бойцовский клуб", а если нет в списке, отправялем его на регистрацию.
# Дальше после входа, он может пополнить свой баланс или проверить сколько у него на балансе денег.
# У нашего комп клуба есть тарифы, и может выбрать из этих тарифов, если хватает денег, если хватает денег и он выбирает, то с его баланса снимается эта сумма
tarif = {
    '3 часа': 150,
    '5 часа': 220,
    '7 часа': 330
}

clients = {
    "Agent007": {'password':'qwerty','balance':300}
}

while True:
    played = input("Вы уже играли в нашу игру? (да/нет): ").lower()

    if played == "нет":
        print("Тогда давайте зарегистрируем вас.")
        login = input("Введите логин: ")
        while login in clients:
            print("Такой логин уже существует. Попробуйте другой.")
            login = input("Введите логин: ")
        password = input("Введите пароль: ")
        clients[login] = {'password': password, 'balance': 0}
        print(f"Регистрация успешна! Ваш логин: {login}")
        current_user = login
        break

    elif played == "да":
        login = input("Введите ваш логин: ")
        if login in clients:
            password = input("Введите пароль: ")
            if clients[login]['password'] == password:
                print("Добро пожаловать в бойцовский клуб!")
                current_user = login
                break
            else:
                print("Неверный пароль. Попробуйте снова.")
        else:
            print("Такого пользователя нет. Нужно зарегистрироваться.")
    else:
        print("Ответьте 'да' или 'нет'.")

while True:
    print("\nВаш баланс:", clients[current_user]['balance'], "сом")
    action = input("Что вы хотите сделать?\n1 - Пополнить баланс\n2 - Проверить тарифы и выбрать\n3 - Выйти\nВыбор: ")

    if action == "1":
        amount = int(input("Сколько сом хотите пополнить?: "))
        clients[current_user]['balance'] += amount
        print("Баланс успешно пополнен!")

    elif action == "2":
        print("Доступные тарифы:")
        for t, price in tarif.items():
            print(f"{t} - {price} сом")
        choice = input("Выберите тариф: ")
        if choice in tarif:
            if clients[current_user]['balance'] >= tarif[choice]:
                clients[current_user]['balance'] -= tarif[choice]
                print(f"Тариф {choice} успешно куплен! Остаток баланса: {clients[current_user]['balance']} сом")
            else:
                print("Недостаточно денег на балансе.")
        else:
            print("Такого тарифа нет.")

    elif action == "3":
        print("Выход. До свидания!")
        break

    else:
        print("Неверный выбор.")
