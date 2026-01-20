class User:
    def __init__(self,name):
        self.name = name

    def __repr__(self):
        return (f"User: {self.name}")
    
    def __str__(self):
        return (f"User: {self.name}")

user = User("Shahriar")
print(user)