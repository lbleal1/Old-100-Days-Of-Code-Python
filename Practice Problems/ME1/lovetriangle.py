#Love Triangle

#Problem

# You enjoy thinking about hypothetical situations involving you and 
# your friends. The what-if scenario you are thinking of now is what 
# if there are hidden feelings involved between you and your two 
# close friends

# You plan on whipping up a program to easily find out which 
# scenarios will keep your friendship and sanity intact given all 
# possible cases.


#Assumptions

# For simplicity, we are disallowing ​Friend A and ​Friend B from 
# liking each other (bonus points for handling equality; see below)

#No need to consider narcissistic tendencies (one liking oneself)

#Feelings have to be ​mutual
	#Pairs who like each other will end up together unless a 
	#rivalry exists
	
	#Pairs who do not like each other will not end up together;
	#feelings have to be mutual ( ​wag pilitin kung hindi talaga meant to be)

#No two-timing
		#Be loyal; sharing is shit (all of you liking each other ​
		#will never work out ​)
		
		#Liking both your friends is a valid scenario
			#You like both Friend A and Friend B
			#Friend A likes you as well
			#Friend B does not like you back
			#Since Friend A likes you back, Friend B ​not liking you
			#back does not matter ​ since you will end up with Friend A

#Walang sawi/bitter
		#If you harbor feelings for anyone, 
		#you should end up with someone

#Restrictions
	#Use at most 50 comparison operators (=, !=, <, <=, >, >=)

#Input
	#yes ​ ​if person 1 likes person 2, ​no ​ otherwise
		#Use your own name and two others
	#(in order)
		#Does ​(your name) ​ like ​(friend A’s name) ​?
		# Does ​(your name) ​ like ​(friend B’s name) ​?
		# Does ​(friend A’s name) ​ like ​(your name) ​?
		# Does ​(friend B’s name) ​ like ​(your name) ​?

#Output
	# Any positive message for the case when no friendships will be
	#broken if so, or a negative message if drama will ensue and 
	#broken hearts are inevitable (make your own messages)

you = input("Enter your name: ")
friend1 = input("Enter your friend's name: ")
friend2 = input("Enter another friend's name: ")

ans1 = input("Does " + you  + " like " + friend1 + "? ")
ans2 = input("Does " + you  + " like " + friend2 + "? ")
ans3 = input("Does " + friend1  + " like " + you + "? ")
ans4 = input("Does " + friend2  + " like " + you + "? ")


