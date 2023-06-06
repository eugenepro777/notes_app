import json
import time
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
    print()


def get_notes() -> dict:
    """Получаем словарь заметок из файла notes.json"""
    try:
        with open("notes.json", "r") as file:
            notes = json.load(file)
            return notes
    except FileNotFoundError:
        notes = {}
    return notes


def save_notes(notes) -> None:
    """Сохраняем словарь заметок в файл notes.json"""
    with open("notes.json", "w") as file:
        json.dump(notes, file, indent=2)


def update_note() -> None:
    """Изменяет указанную заметку в словаре заметок и сохраняет обновленный словарь в файл"""
    while True:
        search_by = input("Введите идентификатор или заголовок заметки: ")
        notes = get_notes()
        matching_notes = {k: v for k, v in notes.items() if search_by in [k, v["title"]]}
        if not matching_notes:
            print(f"Заметка с параметром '{search_by}' не найдена")
            choice = input("Введите 'y', чтобы попробовать еще раз или 'n' для возврата в меню:\n>> ")
            if choice == 'n':
                return
            continue

        if len(matching_notes) > 1:
            print(f"Найдено несколько заметок с параметром '{search_by}':")
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
            choice = input("Введите 'y', чтобы попробовать еще раз или 'n' для возврата в меню:\n>> ")
            if choice == 'n':
                print()
                return
            continue

        title = input("Введите новый заголовок заметки: ")
        if title == note["title"]:
            print("Заголовок заметки не изменился")
            choice = input("Введите 'y', чтобы ввести другой заголовок или 'n' для возврата в меню:\n>> ")
            if choice == 'n':
                print()
                return
            continue
        body = input("Введите новый текст заметки: ")
        note["title"] = title
        note["body"] = body
        note["date"] = datetime.now().strftime("%d.%m.%Y %H:%M:%S")

        save_notes(notes)
        print(f"Заметка с параметром {id_or_title_note} обновлена")
        choice = input("Введите 'y', чтобы продолжить или 'n' для возврата в меню:\n>> ")
        if choice == 'n':
            print()
            return


def delete_note() -> None:
    """Удаляет заметку по идентификатору или заголовку заметки"""
    while True:
        delete_by = input("Удалить по идентификатору или по заголовку? Введите 'id' или 'title': ")
        notes = get_notes()
        if delete_by == "id":
            id_note = input("Введите идентификатор заметки для удаления: ")
            if id_note in notes:
                del notes[id_note]
                save_notes(notes)
                print(f"Заметка с идентификатором {id_note} удалена\n")
            else:
                print(f"Заметка с идентификатором {id_note} не найдена")
        elif delete_by == "title":
            title = input("Введите заголовок заметки для удаления: ")
            found_notes = []
            for note in notes.values():
                if note["title"] == title:
                    found_notes.append(note)
            if found_notes:
                print(f"Найдены заметки с заголовком {title}: ")
                for note in found_notes:
                    print(f"Идентификатор: {note['id']}")
                    print(f"Заголовок: {note['title']}")
                    print(f"Текст заметки: {note['body']}")
                    print(f"Дата создания: {note['date']}")
                print("*" * 30)
                id_note = input("Введите идентификатор заметки для удаления: ")
                if id_note in notes:
                    del notes[id_note]
                    save_notes(notes)
                    print(f"Заметка с идентификатором {id_note} и именем {title} удалена\n")
                    time.sleep(1)
                else:
                    print(f"Заметка с идентификатором {id_note} не найдена")
            else:
                print(f"Заметка с именем {title} не найдена")
        else:
            print("Неизвестный параметр удаления. Введите 'id' или 'title'")
        choice = input("Продолжить удаление? Введите 'y' или 'n'\n>> ")
        if choice.lower().strip() == 'n':
            print()
            break
