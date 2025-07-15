try:
    n = 0
    num = 1/0
except ZeroDivisionError:
    print("You can't divide a number by zero")
except ValueError:
    print("Please enter the correct number")
else:
    print(num)
finally:
    print("Execution completed")
