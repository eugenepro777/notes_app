import time
from models import create_add_note, update_note, delete_note
from views import display_all_notes, select_note_by_date, select_note_by_title


def app_menu():
    while True:
        print("***Выберите пункт меню:")
        print("1. Показать все заметки")
        print("2. Выбрать заметки по дате")
        print("3. Выбрать заметки по заголовку")
        print("4. Добавить заметку")
        print("5. Отредактировать заметку")
        print("6. Удалить заметку")
        print("0. Выход")
        print("-" * 30)

        choice = input(">> ")

        match choice:
            case "1":
                # os.system('cls' if os.name == 'nt' else 'clear')
                print("\n" * 100)
                display_all_notes()
                time.sleep(3)
            case "2":
                select_note_by_date()
            case "3":
                select_note_by_title()
            case "4":
                create_add_note()
            case "5":
                update_note()
            case "6":
                delete_note()
            case "0":
                print(">> Вы вышли из программы")
                break
            case _:
                print("Такого пункта нет. Повторите ввод.\n")
                time.sleep(1)


app_menu()

