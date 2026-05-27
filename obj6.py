class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password

    def get_email(self):
        return self._email

    def set_email(self, new_email):
        self._email = new_email

    def say_hi_to_user(self, user):
        print(
            f"Sending message to {user.username}: Hi {user.username}. it's {self.username}"
        )


user1 = User("Charles", "charlesowino180@gmail.com", "1234")
print(user1.get_email())
user1.set_email("agwandacharlesowino@gmail.com")
print(user1.get_email())
