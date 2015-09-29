input = open('float_data.txt' , 'r')
A = input.readlines()
for i in range(len(A)):
    A[i] = float(A[i])
sredn = sum(A)/len(A)
smq = 0
for i in range(len(A)
    smq += A[i] ** 2
srednkvr = (smq/len(A) - sredn**2)**0.5
print(srednkvr)