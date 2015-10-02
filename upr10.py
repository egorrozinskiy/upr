from random import random

inp = str(input())
x = list(map(int,inp.split(" ")))
y = int(input())
for i in range(y):
    x.insert(len(x)-1-x[len(x)- 1],x[len(x)-1])
    x.reverse()
    x.remove(x[0])
    x.reverse()
print(x)