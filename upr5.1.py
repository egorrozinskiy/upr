from random import *
inp = open("inp.txt","w")
s = ""
for i in range (1000000):
    s += str(randint(0,100)) + " "
inp.write(s)
inp.close()  