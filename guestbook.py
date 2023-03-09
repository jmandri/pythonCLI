import sys
import os


def add_new_entry(entry):
    with open("guestbook.txt", "a") as f:
        f.write(entry + "\n")


def list_entries():
    with open("guestbook.txt", "r") as f:
        entries = f.readlines()
        for i, entry in enumerate(reversed(entries)):
            print(f"{i + 1}. {entry.strip()}")


def edit_entry(num, new_entry):
    with open("guestbook.txt", "r+") as f:
        entries = f.readlines()
        entry_to_edit = entries[-num].strip()
        f.seek(0)
        for entry in entries:
            if entry.strip() == entry_to_edit:
                f.write(new_entry + "\n")
            else:
                f.write(entry)
        f.truncate()


def delete_entry(num):
    with open("guestbook.txt", "r+") as f:
        entries = f.readlines()
        entry_to_delete = entries[-num].strip()
        f.seek(0)
        for entry in entries:
            if entry.strip() != entry_to_delete:
                f.write(entry)
        f.truncate()


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: guestbook.py [new|list|edit|delete] [args]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "new":
        if len(sys.argv) < 3:
            print("Usage: guestbook.py new [entry]")
            sys.exit(1)
        entry = " ".join(sys.argv[2:])
        add_new_entry(entry)
        print("Entry added successfully!")
    elif command == "list":
        list_entries()
    elif command == "edit":
        if len(sys.argv) < 4:
            print("Usage: guestbook.py edit [num] [new_entry]")
            sys.exit(1)
        num = int(sys.argv[2])
        new_entry = " ".join(sys.argv[3:])
        edit_entry(num, new_entry)
        print(f"Entry #{num} edited successfully!")
    elif command == "delete":
        if len(sys.argv) < 3:
            print("Usage: guestbook.py delete [num]")
            sys.exit(1)
        num = int(sys.argv[2])
        delete_entry(num)
        print(f"Entry #{num} deleted successfully!")
    else:
        print("Invalid command")
        sys.exit(1)
