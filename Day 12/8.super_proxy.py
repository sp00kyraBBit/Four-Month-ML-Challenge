class User:
    def __init__(self, username):
        self.username = username
        self.is_active = True

class Admin(User):
    def __init__(self, username, role):
        super().__init__(username)
        self.role = role
