count = 0
maxcount = 0
lastorg = ""
for i in range(1,6):
	org = input("Year " + str(i) + " winner: ")
	if count == 0 or org == lastorg:
		count +=1
		lastorg = org
	elif lastorg != org:
		count = 0
	if maxcount < count:
		maxcount = count

print(maxcount)
