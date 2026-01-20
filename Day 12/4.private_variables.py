class User:
    def __init__(self,name,password):
        self.name = name
        self.__password = password

user = User("Shahriar","1234")
print(user.__password)