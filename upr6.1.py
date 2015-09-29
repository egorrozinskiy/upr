input = open('float_data.txt' , 'r')
A = input.readlines()
for i in range(len(A)):
    A[i] = float(A[i])
sredn = sum(A)/len(A)
print(sredn) 