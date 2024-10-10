class Note:
    """Class representing a single note."""
    
    def __init__(self, content):
        self.content = content

    def __str__(self):
        return self.content


class NotePad:
    """Class representing a collection of notes."""
    
    def __init__(self):
        self.notes = []

    def add_note(self, content):
        """Add a new note to the note pad."""
        new_note = Note(content)
        self.notes.append(new_note)
        print("Note added!")

    def view_notes(self):
        """View all notes in the note pad."""
        if not self.notes:
            print("Your note pad is empty.")
        else:
            print("Your Notes:")
            for i, note in enumerate(self.notes, start=1):
                print(f"{i}. {note}")

    def delete_note(self, index):
        """Delete a note from the note pad by its index."""
        if 0 <= index < len(self.notes):
            removed_note = self.notes.pop(index)
            print(f"Deleted note: {removed_note}")
        else:
            print("Invalid note index.")


def main():
    """Main function to run the Note Pad application."""
    notepad = NotePad()

    while True:
        print("\n--- Note Pad Menu ---")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Delete Note")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            content = input("Enter the note content: ")
            notepad.add_note(content)
        elif choice == '2':
            notepad.view_notes()
        elif choice == '3':
            notepad.view_notes()
            if not notepad.notes:
                continue
            try:
                index = int(input("Enter the note number to delete: ")) - 1
                notepad.delete_note(index)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            print("Exiting the Note Pad. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 4.")


if __name__ == "__main__":
    main()
