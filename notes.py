import json
import datetime

def load_notes():
    try:
        with open('notes.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_notes(notes):
    with open('notes.json', 'w') as file:
        json.dump(notes, file, indent=4)

def add_note():
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    timestamp = datetime.datetime.now().isoformat()
    note = {
        'id': len(notes) + 1,
        'title': title,
        'body': body,
        'timestamp': timestamp
    }
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно сохранена")

def list_notes():
    for note in notes:
        print(f"{note['id']}. {note['title']} - {note['timestamp']}")

def filter_notes_by_date(date):
    filtered_notes = [note for note in notes if note['timestamp'].startswith(date)]
    for note in filtered_notes:
        print(f"{note['id']}. {note['title']} - {note['timestamp']}")

def edit_note():
    note_id = int(input("Введите id заметки для редактирования: "))
    for note in notes:
        if note['id'] == note_id:
            new_title = input("Введите новый заголовок заметки: ")
            new_body = input("Введите новый текст заметки: ")
            note['title'] = new_title
            note['body'] = new_body
            save_notes(notes)
            print("Заметка успешно отредактирована")
            return
    print("Заметка с указанным id не найдена")

def delete_note():
    note_id = int(input("Введите ID заметки для удаления: "))
    global notes
    notes = [note for note in notes if note['id'] != note_id]
    for index, note in enumerate(notes):
        note['id'] = index + 1
    save_notes(notes)
    print("Заметка успешно удалена")

notes = load_notes()

while True:
    command = input("Введите команду (add/list/filter/edit/delete/exit): ")

    if command == 'add':
        add_note()
    elif command == 'list':
        list_notes()
    elif command == 'filter':
        date = input("Введите дату для фильтрации (гггг-мм-дд): ")
        filter_notes_by_date(date)
    elif command == 'edit':
        edit_note()
    elif command == 'delete':
        delete_note()
    elif command == 'exit':
        break