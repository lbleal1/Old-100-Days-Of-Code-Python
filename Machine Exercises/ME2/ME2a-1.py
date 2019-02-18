#easier than average
summ = 0
count = 0
while True:
	n = float(input("Input a positive number:"))  		
	if n < 0:
		break
	summ += n 
	count +=1

print(summ/count)
