#Determine the value of n! given n
# n! = n(n-1)(n-2)...(2)(1)

n = int(input("Enter n: "))
result = n
for i in range(1, n):
	result *= n-i
print(result)
