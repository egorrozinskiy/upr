input = open('int_data.txt', 'r')
A = input.readlines()
for i in range(len(A)):
	A[i] = int(A[i])
k = 0
lx = ln = A[0]
for i in range(len(A)):
	if A[0:i].count(A[i]) == 0:
		print(A[i], A.count(A[i]), 'r', k)
		k += 1
	x = A.count(A[i])	
	if A.count(ln) > x:
		ln = A[i]
	if x > A.count(lx):
		lx = A[i]
print(lx, ln)
print(k)