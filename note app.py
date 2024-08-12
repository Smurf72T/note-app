import os.path

"""Функция для создания заметки в новом файле"""
def build_note(note_text, note_name):
    f = open(f'{note_name}.txt', 'w', encoding="utf-8")
    f.write(note_text)
    f.close()
    print(f'Заметка {note_name} создана')

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
    if os.path.isfile(f'{note_name}.txt'):
        f = open(f'{note_name}.txt', 'r')
        f.close()
        print(f)
    else:
        print(f'Заметка {note_name} не найдена')

"""Функция которая редактирует заметку"""
def edit_note():
    note_name = input("Введите название заметки: ")
    if os.path.isfile(f'{note_name}.txt'):
        f = open(f'{note_name}.txt', '+')
        print(f)
        note_text = input("Введите текст заметки: ")
        f.write(note_text)
        f.close()
    else:
        print(f'Заметка {note_name} не найдена')

"""Функция, которая удаляет заметку"""
def delete_note():
    note_name = input("Введите название заметки: ")
    if os.path.isfile(f'{note_name}.txt'):
        os.remove(f'{note_name}.txt')
    else:
        print(f'Заметка {note_name} не найдена')