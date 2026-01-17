import pickle

class Student:
    def __init__(self,name,age,section):
        self.name = name
        self.age = age
        self.section = section

student1 = Student("Shahriar",24,"A")

with open("read.pkl","wb") as f:
    pickle.dump(student1,f,protocol=pickle.HIGHEST_PROTOCOL)