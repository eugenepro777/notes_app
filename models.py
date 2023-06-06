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


def update_note() -> None:
    """Изменяет указанную заметку в словаре заметок и сохраняет обновленный словарь в файл"""
    search_parameter = input("Введите идентификатор или заголовок заметки: ")
    notes = get_notes()
    matching_notes = {k: v for k, v in notes.items() if search_parameter in [k, v["title"]]}
    if not matching_notes:
        print(f"Заметка с параметром '{search_parameter}' не найдена")
        return

    if len(matching_notes) > 1:
        print(f"Найдено несколько заметок с параметром '{search_parameter}':")
        for id_note, note in matching_notes.items():
            print(f"Идентификатор: {id_note}")
            print(f"Заголовок: {note['title']}")
            print(f"Текст заметки: {note['body']}")
            print(f"Дата создания: {note['date']}")
            print()
        id_or_title_note = input("Введите идентификатор или заголовок заметки: ")
    else:
        id_or_title_note = next(iter(matching_notes))
    note = notes.get(id_or_title_note) or next((note for note in notes.values() if note['title'] == id_or_title_note), None)

    if not note:
        print(f"Заметка с параметром '{id_or_title_note}' не найдена")
        return

    title = input("Введите новый заголовок заметки: ")
    body = input("Введите новый текст заметки: ")
    note["title"] = title
    note["body"] = body
    note["date"] = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

    save_notes(notes)
    print(f"Заметка с параметром {id_or_title_note} обновлена")