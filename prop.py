class Person:
    def __init__(self, age):
        self.age = age

    def add(self):
        return self.age + 20
    
    @property
    def age(self):
        print("Getting Info/Values..")
        return self._age
    
    @age.setter
    def age(self, a):
        if a >= 40:
            raise ValueError("Age is greater than 40")
        self._age = a

person = Person(17)

print(person.age)

print(person.add())

try:
    age = Person(45)
except ValueError as e:
    print(e)


