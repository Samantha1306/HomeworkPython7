# Функция для добавления данных в справочники

def add_data1(data, sep=','):
    with open('Phonebook1.csv', 'a+', encoding="utf_8") as file:
        file.write(sep.join(data))
        file.write(f"\n")
    print('Данные добавлены.')


def add_data2(data, sep=' '):
    with open('Phonebook2.csv', 'a+', encoding="utf_8") as file:
        for i in data:
            file.write(f"{i}\n")
        file.write(f"\n")
    print('Данные добавлены.')
