choice1 = input("Choice 1:")
choice2 = input("Choice 2:")

hateRate1 = float(input(choice1 + "? "))
hateRate2 = float(input(choice2 + "? "))

if hateRate1 <= hateRate2:
	result = "Choose the first choice!"
else:
	result = "Choose the second choice!"

print(result)
