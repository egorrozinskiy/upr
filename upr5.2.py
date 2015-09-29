from random import *
output = open('float_data.txt', 'w')
for i in (1000000):
    print(randint(0, 100)//100, file=output)
