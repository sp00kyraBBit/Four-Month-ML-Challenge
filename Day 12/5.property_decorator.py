from datetime import date

class User:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    @property
    def age(self):
        current_year = date.today().year
        return current_year - self.birth_year
    
user = User("Shahriar",2001)
print(user.age)