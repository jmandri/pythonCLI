import json
import unittest

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

class TestGuestbook(unittest.TestCase):
    def setUp(self):
        try:
            with open("guestbook.txt", "r") as f:
                self.guestbook = json.loads(f.read())
        except FileNotFoundError:
            self.guestbook = []

    def test_add_note(self):
        add_note(self.guestbook, "This is my note")
        self.assertEqual(self.guestbook[-1], "This is my note")

    def test_edit_note(self):
        add_note(self.guestbook, "This is my note")
        edit_note(self.guestbook, -1, "Change the note")
        self.assertEqual(self.guestbook[-1], "Change the note")

    def test_delete_note(self):
        add_note(self.guestbook, "This is my note")
        delete_note(self.guestbook, -1)
        self.assertEqual(len(self.guestbook), 0)

if __name__ == "__main__":
    unittest.main()