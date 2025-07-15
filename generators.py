def numbers(num):
    n = 0
    while n <= num:
        yield n
        n += 1

generator  = numbers(5)

for i in generator:
    print(i)

#Product Generator
def product(num):
   for i in num:
       yield i * 2

# Generator Expression
print("Generator Expression")

generator = (i + i for i in range(5))
for i in generator:
    print(i)



# Pipelining Generators
print("Pipelining Generators")
print(sum(product(numbers(4))))