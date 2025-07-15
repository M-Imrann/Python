a = lambda x, y: x + y

print(a(3, 4))


# passing a function 
def sum(fun):
    print(fun)
    return lambda a: a * fun


num = sum(2)
print(num(3))