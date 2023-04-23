"""
Pyhton and MySQL project:
- Open assistant
- Login or register
- If we choose register, it will create a user in the db
- If we choose login, identifies the user and will ask us
- Create note, show notes, delete them
"""
from users import actions

print("""
Available actions:
    - Register
    - Login
""")

do = actions.Actions()
action = input("What do you want to do?")

if action == "register" or action == "Register":
    do.register()

elif action == "login" or action == "Login":
    do.login()



    