# Arbitrary Arguments
def sum(*args):
    sum = 0
    for i in args:
        sum += i
    print (sum)

sum(1,2,3)
sum(2,3,5,4)
sum(1,3,4,6,3,4)

# Arbitrary keyword arguments

def info(**kwargs):
    for key, value in kwargs.items():
        print("{} is {}" .format(key, value))


info(name = "Imran", dob = 1, gender = "Male", Pos = "Python")
info(name = "Ali", dob = 2, gender = "Male", Pos = "MERN", loc = "Lahore")