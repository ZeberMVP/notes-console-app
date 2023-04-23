import datetime
import hashlib
import users.connection as connection

connect = connection.connect()
database = connect[0]
cursor = connect[1]


class User:
    def __init__(self, name, surname, email, password):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password

    def register(self):
        date = datetime.datetime.now()

        # Cypher password
        cypher = hashlib.sha256()
        cypher.update(self.password.encode("utf8"))

        sql = "INSERT INTO users VALUES(null, %s, %s, %s, %s, %s)"
        user = (
            self.name,
            self.surname,
            self.email,
            cypher.hexdigest(),
            date,
        )

        try:
            cursor.execute(sql, user)
            database.commit()
            result = [cursor.rowcount, self]
        except:
            result = [0, self]

        return result

    def identify(self):
        # Query to check if user exists
        sql = "SELECT * FROM users WHERE email = %s AND password = %s"

        # Cypher password
        cypher = hashlib.sha256()
        cypher.update(self.password.encode("utf8"))

        # Data for query
        user = (self.email, cypher.hexdigest())

        cursor.execute(sql, user)
        result = cursor.fetchone()

        return result
