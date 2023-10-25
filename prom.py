import json
import os
from datetime import datetime

FILE_PATH = "notes.json"
def load_():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as file:
            try:
                notes_ = json.load(file)
            except json.JSONDecodeError:
                notes_ = []
    else:
        notes_ = []
    return notes_


def save_(notes):
    with open(FILE_PATH, 'w') as file:
        json.dump(notes, file, indent=4)


def add_():
    title = input("Введите заголовок заметки: ")
    content = input("Введите содержание заметки: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    note = {
        "id": len(notes) + 1,
        "title": title,
        "content": content,
        "timestamp": timestamp
    }
    notes.append(note)
    save_(notes)
    print("Заметка добавлена успешно.")


def edit_():
    note_id = int(input("Введите ID заметки для редактирования: "))
    for note in notes:
        if note["id"] == note_id:
            note["title"] = input("Введите новый заголовок заметки: ")
            note["content"] = input("Введите новое содержание заметки: ")
            note["time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_(notes)
            print("Заметка успешно отредактирована.")
            return
    print("Заметка с указанным ID не найдена.")


def delete_():
    note_id = int(input("Введите ID заметки для удаления: "))
    for note in notes:
        if note["id"] == note_id:
            notes.remove(note)
            save_(notes)
            print("Заметка успешно удалена.")
            return
    print("Заметка с указанным ID не найдена.")


def display_():
    for note in notes:
        print(f'ID: {note["id"]}, '
              f'Заголовок: {note["title"]}, '
              f'Содержание: {note["content"]}, '
              f'Дата/Время: {note["timestamp"]}')


notes = load_()

while True:
    print("\nВыберите действие:")
    print("1. Добавить заметку")
    print("2. Редактировать заметку")
    print("3. Удалить заметку")
    print("4. Вывести все заметки")
    print("5. Выйти")
    choice = input("Введите номер действия: ")

    if choice == "1":
        add_()
    elif choice == "2":
        edit_()
    elif choice == "3":
        delete_()
    elif choice == "4":
        display_()
    elif choice == "5":
        break
    else:
        print("попробуйте снова.")