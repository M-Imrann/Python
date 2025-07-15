def repeat(fun):
    def wrapper():
        print("The sum of two numbers are :")
        sum()
        print("Sum calculated")

@repeat

def sum(a,b):
    print(a+b)