#Problem
#Your love life has been nonexistent for so long, so you want 
#to play Cupid and feel secondhand sparks by making a program that 
#evaluates the situation between two of your close friends involving 
#love (or infatuation/attraction?).

#Input
#If friend A likes friend B or not and if friend B likes friend A or not: yes/y or no/n

#Output
#A positive message if there are mutual feelings
#A negative message if there are unrequited feelings
#A neutral message if there are no feelings involved

name1 = input("Enter a person name: ")
name2 = input("Enter a person name: ")

ask1 = input("Does " + name1 + " like " + name2 + "? ")
ask2 = input("Does " + name2 + " like " + name1 + "? ")

if (ask1 == "yes" or ask1 == "y") and  (ask2 == "yes" or ask2 == "y"):
	result = "Mutual!"
elif ((ask1 == "yes" or ask1 == "y") and (ask2 == "no" or ask2 == "n")) or ((ask1 == "no" or ask1 == "n") and  (ask2 == "yes" or ask2 == "y")) : 
	result = "Unrequited..."
else:
	result = "Friends."

print(result)
