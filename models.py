import json
from datetime import datetime


def create_add_note() -> None:
    """ Пользователь вводит заголовок и тело заметки с консоли,
    создаем словарь заметок, с полями id, title, body и date/time
    """
    notes = get_notes()
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    id_note = str(len(notes) + 1)
    date_creation = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    notes[id_note] = {
        "id": id_note,
        "title": title,
        "body": body,
        "date": date_creation
    }
    save_notes(notes)
    print(f"Заметка с id {id_note} добавлена")


def get_notes() -> dict:
    """Получаем словарь заметок из файла notes.json"""
    try:
        with open("notes.json", "r") as file:
            notes = json.load(file)
            return notes
    except FileNotFoundError:
        notes = {}
    return notes


def save_notes(notes):
    """Сохраняем словарь заметок в файл notes.json"""
    with open("notes.json", "w") as file:
        json.dump(notes, file, indent=2)
