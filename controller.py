# Функции для вызова меню, добавления данных

from add_data import add_data1, add_data2
from export_data import export_data1, export_data2
from print_data import print_data1, print_data2

# Обращение к пользователю, что умеет делать справочник


def greet():
    print('Добрый день! Вы зашли в телефонный справочик.\n\
    С помощью него вы можете просматривать контакты, добавлять контакты в двух форматах, найти контакт в любом из спарвочников.\n\
    Данные в Телефонном справочнике 1 хранятся построчно. Даныне в Телефонном справочнике 2 хранятся в одной строке с разделителем "запятая".\n\
    Для того, чтобы выбрать необходимое действие, введите нужную цифру из меню.')

# Добавление данных в справочники


def input_data():
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    phone_number = input("Введите телефон: ")
    note = input("Введите описание: ")
    return [last_name, first_name, phone_number, note]

# Вывод меню для выбора действия


def menu():
    print("Меню:\n\
    1 - Просмотр записей из обоих телефонных справочников\n\
    2 - Добавить запись в Телефонный справочник 1;\n\
    3 - Добавить запись в Телефонный справочник 2")
    ch = input("Введите цифру: ")
    if ch == '1':
        data1 = export_data1()
        print_data1(data1)
        data2 = export_data2()
        print_data2(data2)
    elif ch == '2':
        add_data1(input_data())
    elif ch == '3':
        add_data2(input_data())
