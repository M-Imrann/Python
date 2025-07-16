'''class Parent:
    age = 15

    def Age(cls):
        print("The age is :", cls.age)


Parent.Age = classmethod(Parent.Age)

Parent.Age()

'''
'''from datetime import date

class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def BirthYear(cls, name, birthYear):
        return cls(name, date.today().year - birthYear)

    def show(self):
        print(self.name + "'s age is: " + str(self.age))

person = Parent('Ali', 24)
person.show()

'''

# Static method

class Sum:
    @staticmethod
    def Add(x,y):
        return x+y
    
s = Sum.Add(2,3)
print(s)