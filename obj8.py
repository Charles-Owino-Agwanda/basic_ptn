class User:
    user_count = 0

    def __init__(self, username, email):
        self.username = username
        self.email = email
        User.user_count += 1

    def display_user(self):
        print(f"Username: {self.username}, Email: {self.email}")


user1 = User("Charles", "agwandacharles@gmailcom")
user2 = User("Kevin", "kevin@gmailcom")
user3 = User("Erick", "Erick@gmailcom")

print(User.user_count)
