ages = [13, 67, 35, 87, 23, 27, 2, 15]

def func(n):
    if n > 18:
        return True
    else:
        return False
    
adults = filter(func, ages)

for i in adults:
    print(i)
