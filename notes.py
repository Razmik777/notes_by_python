import json
import datetime


def load_notes():
    try:
        with open('notes.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_notes(notes):
    with open("notes.json", "w") as file:
        json.dump(notes, file, indent=4)


def add_note():
    title = input("Введите заголовок заметки: ")
    body = input("Введите тело заметки: ")
    timestamp = datetime.datetime.now().isoformat()

    note = {
        id: len(notes) + 1,
        "title": title,
        "body": body,
        "timestamp": timestamp
    }
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно добавлена")
