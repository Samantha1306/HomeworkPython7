# Функция для вывода данных
def export_data1():
    with open('Phonebook1.csv', 'r', encoding="utf_8") as file:
        data = []
        t = []
        for line in file:
            if ',' in line:
                temp = line.strip().split(',')
                data.append(temp)
    return data


def export_data2():
    with open('Phonebook2.csv', 'r', encoding="utf_8") as file:
        data = []
        t = []
        for line in file:
            if line != '':
                if line != '\n':
                    t.append(line.strip())
                else:
                    data.append(t)
                    t = []
    return data
