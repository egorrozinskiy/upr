A=[2,4,5,5,5,4,2,2,4,4,5,8]
k=None
for i in A:
    if k==None:
        k=A.count(i)
    elif A.count(i)>k:
        h=i
print(h)
