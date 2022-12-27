# Функции для вывода контактов из справочника

def print_data1(data):
    if len(data) > 0:
        print("Телефонный справочник 1".center(85))
        print("-"*85)
        print("Фамилия".center(20), "Имя".center(20),
              "Телефон".center(15), "Описание".center(30))
        print("-"*85)
        for item in data:
            print(item[0].center(20), item[1].center(20),
                  item[2].center(15), item[3].center(30))
        print("-"*85)
    else:
        print("Телефонный справочник 1 пуст!")

def print_data2(data):
    if len(data) > 0:
        print("Телефонный справочник 2")
        print("-"*22)
        for i in data:
            if i != '':
                for j in i:
                    print(f'|| {j}' + " " * (22 - len(j) - 5) + "||")
            print("-" * 22)
            print("-" * 22)
    else:
        print("Телефонный справочник 2 пуст!")
