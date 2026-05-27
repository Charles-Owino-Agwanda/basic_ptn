class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email
        self.password = password

    @property
    def email(self):
        print("Email Accessed")
        return self._email

    @email.setter
    def email(self, new_email):
        if "@" in new_email:
            self.email = new_email


user1 = User("Charles", "charlesowino180@gmail.com", "123")
user1.email = "This is not an email"
print(user1.email)
