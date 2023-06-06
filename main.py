import time
from models import create_add_note, update_note, delete_note
from views import display_all_notes, select_note_by_date


def app_menu():
    while True:
        print("***Выберите пункт меню:")
        print("1. Показать все заметки")
        print("2. Выбрать заметки по дате")
        print("3. Добавить заметку")
        print("4. Отредактировать заметку")
        print("5. Удалить заметку")
        print("0. Выход")

        choice = input()

        match choice:
            case "1":
                display_all_notes()
            case "2":
                select_note_by_date()
            case "3":
                create_add_note()
            case "4":
                update_note()
            case "5":
                delete_note()
            case "0":
                print(">>Вы вышли из программы")
                break
            case _:
                print("Такого пункта нет. Повторите ввод.")
                time.sleep(2)
                app_menu()


app_menu()

