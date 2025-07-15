# Local variables
d = 3

def sum(a, b):
    result = 0 
    global d
    d = 6

    result = a + b + d
    print(f"Sum is :{result}")



# rresult is local variable and "a" and "b" are golabal variables.



# we can change the variable of golabal variavle inside function using keyword global 

a = 5
b = 4
sum(a, b)

print(f"The value of d is : {d}")