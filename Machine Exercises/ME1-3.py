#Love Triangle
yla = input("Does Misaki like Usui? ")
aly = input("Does Usui like Misaki? ")

ylb = input("Does Misaki like Tora? ")
bly = input("Does Tora like Misaki? ")

alb = input("Does Usui like Tora? ")
bla = input("Does Tora like Usui? ")

if yla == ylb == aly == bly == "no":
	result = "yay"
elif yla == aly == "yes" and bly == bla == "no": 
	result = "yay"
elif ylb == bly == "yes" and aly== alb == "no": 
	result = "yay"
elif alb == bla == "yes" and yla == ylb == "no": 
	result = "yay"
else:
	result = "gg FO na"

print(result)
