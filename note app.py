import re
import os
import os.path
import sys
from lib2to3.pygram import pattern_symbols
from multiprocessing.connection import answer_challenge

"""Функция для создания заметки в новом файле"""


def build_note(note_text, note_name):
    try:
        try:
            file = open(f'{note_name}.txt', 'r+', encoding="utf-8")
            print('Такой файл существует')
        except IOError:
            file = open(f'{note_name}.txt', 'w+', encoding="utf-8")
            print('Файл создан')
        file.write(note_text)
        print(f'Заметка {note_name} создана.')
    except:
        print('Что-то пошло не так. Повторите попытку.')


"""Функция, которая запрашивает название и текст заметки у пользователя, после чего создает заметку"""
def create_note():
    try:
        note_name = input("Введите название заметки: ")
        forbidden_symbols = '\\|/*<>?:' # набор символов запрещенных в windows
        pattern = "[{0}]".format(forbidden_symbols)
        if re.search(pattern, note_name):
            print(
                'Вы ввели недопустимые символы в названии файла. Переименуйте заметку.'
            )
        # Запросите текст заметки и создайте заметку
        else:
            print('Название заметки создано.')
            note_text = input('Введите текст заметки: ')
            build_note(note_text, note_name)
    except:
        print('Что-то пошло не так. Повторите попытку.')

"""Функция, которая выводит заметку по запросу пользователя"""

def read_note():
    try:
        note_name_read = input("Введите название заметки, которую нужно открыть: ")
        path = f'{note_name_read}.txt'
        if os.path.isfile(path):
            with open(f'{note_name_read}.txt', 'r', encoding="utf-8") as file:
                lines = file.read()
            print('Текст заметки: ', lines)
        else:
            print("Такой заметки не существует. Проверьте правильность имени.")
    except:
        print('Что-то пошло не так. Повторите попытку.')


"""Функция которая редактирует заметку"""

def edit_note():
    try:
        note_name_edit = input(
            "Введите название заметки для редактирования: "
        )
        path = f'{note_name_edit}.txt'
        if os.path.isfile(path):
            print('Заметка существует, можете отредактировать.')
            note_text_new = open(f'{note_name_edit}.txt', 'w+', encoding="utf-8")
            note_text_edit_new = input('Введите новый текст заметки: ')
            note_text_new.write(note_text_edit_new)
            print(f'Заметка {note_name_edit} обновлена.')
        else:
            print(f'Заметка {note_name_edit} не найдена')
    except:
        print('Что-то пошло не так. Повторите попытку.')


"""Функция, которая удаляет заметку"""
def delete_note():
    try:
        note_name_delete = input('Введите название заметки для удаления: ')
        path = f'{note_name_delete}.txt'
        if os.path.isfile(path):
            os.remove(f'{note_name_delete}.txt')
            print(f'Заметка {note_name_delete} удалена')
        else:
            print(f'Заметка {note_name_delete} не найдена')
    except:
        print('Что-то пошло не так. Повторите попытку.')


"""Функция, которая выводит все заметки пользователя"""
def display_notes():
    try:
        notes = [note for note in os.listdir() if note.endswith(".txt")]
        sorted_notes = sorted(notes, key=len, reverse=True)
        print(
            'Список заметок от короткой к длинной: \n',
            sorted_notes,
        )
    except:
        print('Что-то пошло не так. Повторите попытку.')

"""Функция, которая добавляет сортировку для заметок"""
def display_sorted_notes():
    try:
        notes = [note for note in os.listdir() if note.endswith('.txt')]
        sorted_list = sorted(notes, key=len)
        print(
            '\nСписок заметок от короткой к длинной: \n',
            sorted_list,
        )
    except:
        print('Что-то пошло не так. Повторите попытку.')


"""Функция, которая управляет работой приложения"""
def main_note():
    while True:
        action = input(
            "Выберите пункт меню: "
            "\n"
            """               1. Создание заметки
               2. Просмотр заметки
               3. Редактирование заметки
               4. Удаление заметки
               5. Вывод всех заметок от короткой к длинной
               6. Вывод всех заметок от длинной к короткой
               7. Выход из приложения"""
            "\n"
        ).lower()
        # Проверка ввода пользователя.
        allowed_symbols ='1234567'
        pattern1 = "[{0}]".format(allowed_symbols)
        if re.search(pattern1, action):
            print('Вы выбрали верный пункт', action)
            if action == '1':
                create_note()
            if action == '2':
                read_note()
            if action == '3':
                edit_note()
            if action =='4':
                delete_note()
            if action == '5':
                display_notes()
            if action == '6':
                display_sorted_notes()
            if action == '7':
                break
        else:
            print(
                'Такого пункта меню не существует. Пожалуйста введите цифры от 1 до 7'
            )

        print('Чтобы продолжить работать с заметками, нажмите y/n')
        answer = input().lower()
        if answer != 'y':
            break

main_note()

print(sys.hash_info)