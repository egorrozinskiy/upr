from random import *
output = open('int_data.txt', 'w')
for i in (1000000):
    print(randint(0, 100), file=output)
