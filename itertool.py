
'''# count
from itertools import count

for i in count(1):
    if i <= 5:
        print(i)
    else:
        break

# if we will not give condition it will be infinite. we can also give this the steps to skip. 
print("Count with steps")
for i in count(2,2):
    if i <= 10:
        print(i)
    else:
        break

# this will start from 2 and skip 2 numbers

'''

# cycle
'''
from itertools import cycle
count = 0
list = ['A', 'B']

for i in cycle(list):
    if count < 5:
        print(i)
        count += 1
    else:
        break'''

# repeat
from itertools import repeat

print(list(repeat(1, 4)))
