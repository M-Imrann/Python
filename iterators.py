'''list = ["apple", "banana", "cherry"]


iterator = iter(list)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator)) 

# We can also use a for loop to iterate through the list
for item in list:
    print(item)



'''

# Create custom iterators
class Product:

    def __init__(self, max):
        self.max = max

    
    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            pro = self.n * self.n
            self.n += 1
            return pro
        else:
            raise StopIteration
        
pro = Product(4)
i = iter(pro)
print(next(i))
print(next(i))
print(next(i))
print(next(i)) 
print(next(i)) 
print(next(i)) 
