"""def product(a):
    return a*2
    

x = map(product, (2, 4, 3, 6))

for i in x:
    print(i)
"""


# another example

def func(a, b):
    return a + b

x = map(func, (1, 3, 5, 2), (3, 5, 5, 3))

for i in x:
    print(i)