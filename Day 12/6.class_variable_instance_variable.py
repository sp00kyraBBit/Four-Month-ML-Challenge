class Person:
    species = "Human"   

    def __init__(self, name):
        self.name = name   


person1 = Person("Shahriar")
person2 = Person("Kabir")

print(person1.name)
print(person2.name)
print(person1.species)
print(person2.species)

person1.species = "Animal"
print(person1.species)
print(person2.species)

person3 = Person("Munna")
print(person3.species)