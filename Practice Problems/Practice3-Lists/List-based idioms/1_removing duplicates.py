#List-based idioms 1: Removing duplicates

#find occurrence then remove
#keep 1 occurrence


#count occurrence
#if more than one, remove, else stay

A = [1,2,3,4,5,2,3,5,1,7,4]

for i in A:
	if A.count(A[i]) > 1:
		A.remove(A[i]
		
print(A)
