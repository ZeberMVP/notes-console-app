import users.user as model
import notes.actions


class Actions:
    def register(self):
        print("\nWe are going to the register you in the system...")

        name = input("What's your name?\n")
        surname = input("What's your surname?\n")
        email = input("Introduce your email\n")
        password = input("Create a password\n")

        user = model.User(name, surname, email, password)
        registry = user.register()

        if registry[0] >= 1:
            print(f"\n{registry[1].name} has been registered with {registry[1].email}")

        else:
            print("\nYou haven't been registered correctly")

    def login(self):
        print("\nIdentify yourself in the system...")

        try:
            email = input("Introduce your email\n")
            password = input("Introduce your password\n")

            user = model.User("", "", email, password)
            login = user.identify()

            if email == login[3]:
                print(
                    f"Welcome {login[1]}, you registered in the system on {login[5]} "
                )
                self.nextActions(login)
        except Exception as e:
            # print(type(e))
            # print(type(e).__name__)
            print(f"Wrong login. Try again")

    def nextActions(self, user):
        print(
            """
            Available actions:
            - Create note (create)
            - Display your notes (display)
            - Delete note (delete)
            - Exit (exit)
            """
        )

        action = input("What do you want to do?\n")
        do = notes.actions.Actions()

        if action == "create":
            do.create(user)
            self.nextActions(user)

        elif action == "display":
            do.display(user)
            self.nextActions(user)

        elif action == "delete":
            do.deleteNote(user)
            self.nextActions(user)

        elif action == "exit":
            print(f"See you soon, {user[1]}!")
            exit()
