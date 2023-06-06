from models import get_notes
from datetime import datetime


def display_note(id_note) -> None:
    """Отобразить параметры заметки по идентификатору"""
    notes = get_notes()
    if id_note in notes:
        note = notes[id_note]
        print(f"Идентификатор: {id_note}")
        print(f"Заголовок: {note['title']}")
        print(f"Текст: {note['body']}")
        print(f"Дата создания: {note['date']}")
        print()
    else:
        print(f"Заметка с идентификатором {id_note} не найдена")


def display_all_notes() -> None:
    """Отобразить все заметки"""
    print("*" * 25)
    notes = get_notes()
    if not notes:
        print("Заметок не найдено")
    else:
        for id_note, note in notes.items():
            print(f"Идентификатор: {id_note}")
            print(f"Заголовок: {note['title']}")
            print(f"Текст: {note['body']}")
            print(f"Дата создания: {note['date']}")
            print()


def select_note_by_date():
    """Отбираем заметки по дате"""
    print("*" * 25)
    notes = get_notes()
    while True:
        date_input = input("Введите дату в формате 'd.m.YYYY' (день.месяц.год): ")
        try:
            datetime.strptime(date_input, '%d.%m.%Y')
        except ValueError:
            print("Неверный формат даты, введите в формате 'd.m.YYYY' (день.месяц.год): ")
            continue
        found_notes = [id_note for id_note, note in notes.items() if note['date'].startswith(date_input)]
        if not found_notes:
            print(f"Заметок c датой {date_input} не найдено")
        else:
            print(f"Заметки с датой {date_input} найдены: ")
            for id_note in found_notes:
                display_note(id_note)
        choice = input("Продолжить поиск по дате? (y/n)\n>> ")
        while choice not in ["y", "n"]:
            choice = input("Неверный ввод, продолжить поиск по дате? (y/n)\n>> ")
        if choice.lower().strip() == 'n':
            print()
            break

def select_note_by_title():
    """Отбираем заметки по заголовку"""
    print("*" * 25)
    notes = get_notes()
    while True:
        title_input = input("Введите заголовок заметки: ")
        found_notes = [id_note for id_note, note in notes.items() if title_input.lower() == note['title'].lower()]
        if not found_notes:
            print(f"Заметки с заголовком {title_input} не найдено")
        else:
            print(f"Заметки с заголовком {title_input} найдены: ")
            for id_note in found_notes:
                display_note(id_note)
        choice = input("Продолжить поиск по заголовку? (y/n)\n>> ")
        if choice.lower().strip() == 'n':
            print()
            break