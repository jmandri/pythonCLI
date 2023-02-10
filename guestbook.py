import json

def add_note(guestbook, content):
    guestbook.append(content)
    with open("guestbook.txt", "w") as f:
        f.write(json.dumps(guestbook))

def print_entries(guestbook):
    for i, entry in enumerate(guestbook):
        print(f"{i+1}. {entry}")

def edit_note(guestbook, index, content):
    guestbook[index] = content
    with open("guestbook.txt", "w") as f:
        f.write(json.dumps(guestbook))

def delete_note(guestbook, index):
    del guestbook[index]
    with open("guestbook.txt", "w") as f:
        f.write(json.dumps(guestbook))

def export_json(guestbook):
    print(json.dumps(guestbook))

if __name__ == "__main__":
    try:
        with open("guestbook.txt", "r") as f:
            guestbook = json.loads(f.read())
    except FileNotFoundError:
        guestbook = []

    if len(guestbook) == 0:
        print("No entries in guestbook.")

    while True:
        action = input("What would you like to do? (add/print/edit/delete/export/quit) ")
        if action == "add":
            content = input("Enter your note: ")
            add_note(guestbook, content)
        elif action == "print":
            print_entries(guestbook)
        elif action == "edit":
            index = int(input("Enter the index of the entry to edit: ")) - 1
            content = input("Enter the new content: ")
            edit_note(guestbook, index, content)
        elif action == "delete":
            index = int(input("Enter the index of the entry to delete: ")) - 1
            delete_note(guestbook, index)
        elif action == "export":
            export_json(guestbook)
        elif action == "quit":
            break