#Determine the value of n!! given n
#The double factorial of n is the product of the numbers n, n − 2, n − 4, ... not including 0

#following the alternative definition
n = int(input("Enter n: "))
ans = 1
if n%2 == 0: #if even
	end = n//2
	for k in range(1,end+1):
		ans *= 2*k
else:
	end = (n+1)//2
	for k in range(1,end+1):
		ans *= (2*k-1)

print("Answer:",ans)
