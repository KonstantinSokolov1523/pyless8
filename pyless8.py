# на Отлично в одного человека надо сделать консольное приложение Телефонный справочник с внешним хранилищем информации, и чтоб был реализован основной функционал - 
# просмотр, сохранение, импорт, поиск, удаление.

# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести имя или фамилию, и 
# Вы должны реализовать функционал для изменения и удаления данных

# для отлично в группах надо выполнить или ТГ бот или ГУИ (это когда кнопочки и поля ввода как в Виндовс приложениях) или БД

# ГУИ можно сделать просто на EasyGUI или Tkinter
from random import *
import json

phone_book = {}

def save():
    with open("contact.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(phone_book, ensure_ascii=False))
    print("Контакт сохранен")
def load():
    with open("contact.json", "r", encoding="utf-8") as fh:
        phone_book = json.load(fh)
    return phone_book
    
def delete():
    name = input('Введите имя контакта, которого нужно удалить: ')
    phone_book.pop(name)
    return phone_book
def add():
    name = input("Введите имя контакта: ")
    number0 = input("Введите 1й номер: ")
    number1 = input("Введите 2й номер: ")
    bith_day = input("Введите дфту рождения: ")
    mail = input("Введите email: ")
    phone_book[name] = {"phone_numbers": [number0, number1], "birth_day": bith_day, "email": mail}
    print("Контакт добавлен")
    

while True:
    command = input("Введите команду(введите help для вывода списка команд): ")
    if command == "add":
        add()

    elif command == "all":
        print("Контакты: ")
        print(phone_book)
    elif command == "search":
        name = input("Введите имя для поиска: ")
        if name in phone_book:
            print(name, phone_book)
    elif command == "save":
        save()
    elif command == "load":
        phone_book = load()
        print("Загрузка контактов выполнена успешно")
    elif command == "delete":
        delete()
        print("Контакт успешно изменена удалён!")
    elif command == "help":
        print("add -> добавить новый контакт")
        print("search -> поиск контакта по имени")
        print("all -> вывод всех контактов в списке")
        print("save -> сохранить изменения в книге")
        print("load -> загрузить изменения из книги")
    elif command == "exit":
        break
    else:
        print("такой команды нет")

        
   