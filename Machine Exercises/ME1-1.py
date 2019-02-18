a = int(input("Enter birth year of first person:"))
b = int(input("Enter birth year of second person:"))

age1 = 2016 - a
age2 = 2016 - b
print("Age of first person: ", age1)
print("Age of second person: ", age2)


if age1 <= 12 and age2 <=12:
	message = "aral muna bago landi"
elif (age1 <= 12 or age2 <= 12) and (age1 > 12 or age2 > 12):
	message = "wtf u pedo"
elif ((age1/2 + 7) <= age2) and ((age2/2 + 7) <= age1):
	message = "Approve!"
else:
	message = "I'm judging you"

print(message)


