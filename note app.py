"""Функция для создания заметки в новом файле"""
def build_note(note_text, note_name):
    f = open(note_name, 'w')
    f.write(note_text)
    f.close()

"""Функция, которая выводит заметку по запросу пользователя"""
def create_note():
    note_name = input()
    try:
        f = open(note_name, 'r')
        print(f)
    except:
        print(f'Заметка {note_name} не найдена')

"""Функция, которая редактирует заметку"""
def edit_note():
