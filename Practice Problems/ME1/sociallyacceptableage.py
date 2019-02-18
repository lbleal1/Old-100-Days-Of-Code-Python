#Socially Acceptable Age

#Problem
# For those unfamiliar with the “half-your-age-plus-seven” 
# relationship rule, your partner should be ​at least half your age 
# plus seven for the relationship to be considered socially acceptable.

# Ideally, kids should not be pursuing serious relationships; 
# relationships involving children are socially unacceptable.

#Notes 
# Assume the current year is ​2016 ​ and everyone has had his/her birthday
# The rule should be applied to ​both ​partners in order to say that the relationship is socially acceptable
# A child is a person whose age is twelve (12) or under
# An adult is a person whose age is thirteen (13) or above
#  Disclaimer: this rule is not entirely accurate

#Input
# Two numbers (your birth year and your partner’s birth year)

#Output
# The ages of the people involved
# A message for the following cases (make your own messages):
#		Both children ( ​aral muna bago landi)
#		Child and adult ( ​wtf u pedo)
#		Both adults, ages within bounds ( ​Approve!)
#		Both adults, ages outside bounds ( ​I’m judging you)

currentYear = int(input("Enter current year: "))
print()
birthYear1 = int(input("Enter birth year of first person: "))
birthYear2 = int(input("Enter birth year of second person: "))
print()
age1 = currentYear - birthYear1
age2 = currentYear - birthYear2

print("Age of first person:", age1)
print("Age of second person:", age2)
print()

if age1 <= 12 and age2 <= 12:
	result = "Study first."
elif (age1 <= 12 and age2 > 12) or (age1 > 12 and age2 <= 12):
	result = "No child and adult relationship allowed!"
elif age1 > 12 and age2 > 12:
	if age1 > age2:
		older = age1
		younger = age2;
	else:
		older = age2
		younger = age1
	rule = older//2 + 7
	if younger >= rule:
		result = "Approve!"
	else:
		result = "I'm judging you."

print(result)

