import notes.note as model


class Actions:
    def create(self, user):
        print(f"\nLet's create a new note...")
        title = input("Introduce your note title\n")
        description = input("Introduce your note content\n")

        note = model.Note(user[0], title, description)
        save = note.save()

        if save[0] >= 1:
            print(f"You have saved the note: {note.title}\n")

        else:
            print("The note hasn't been saved\n")

    def display(self, user):
        print(f"These are your notes:\n")

        note = model.Note(user[0])
        notes = note.listNote()

        for note in notes:
            print("\n****************************")
            print(note[2])
            print(note[3])
            print("****************************")

    def deleteNote(self, user):
        print("We are going to delete notes")

        title = input("Introduce the title of the note you want to delete\n")

        note = model.Note(user[0], title)
        delete = note.deleteNote()

        if delete[0] >= 1:
            print(f"We have deleted the note: {note.title}")

        else:
            print("We have not deleted anything. Try again")
