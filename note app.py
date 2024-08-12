import os.path

"""Функция для создания заметки в новом файле"""
def build_note(note_text, note_name):
    f = open(note_name, 'w')
    f.write(note_text)
    f.close()

"""Функция, которая запрашивает название и текст заметки у пользователя, после чего создает заметку"""
def create_note():
    note_name = input("Введите название заметки: ")
    note_text = input("Введите текст заметки: ")
    # try:
    build_note(note_text, note_name)
    # except:
    #     print(f'Заметка {note_name} не найдена')

"""Функция, которая выводит заметку по запросу пользователя"""
def read_note():
    note_name = input()
    if os.path.isfile(note_name):
        f = open(note_name, 'r')
        f.close()
        print(f)
    else:
        print(f'Заметка {note_name} не найдена')

"""Функция которая редактирует заметку"""
def edit_note():
    note_name = input("Введите название заметки: ")
    if os.path.isfile(note_name):
        f = open(note_name, '+')
        # f.close()
        print(f)
        note_text = input("Введите текст заметки: ")
        f.write(note_text)
        f.close()
    else:
        print(f'Заметка {note_name} не найдена')

"""Функция, которая удаляет заметку"""
def delete_note():
    note_name = input("Введите название заметки: ")
    if os.path.isfile(note_name):
        os.remove(note_name)
    else:
        print(f'Заметка {note_name} не найдена')