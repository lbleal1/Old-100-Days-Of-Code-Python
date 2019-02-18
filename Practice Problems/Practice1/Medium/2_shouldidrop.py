#Should I drop?

#Problem
# You’re in danger of staining your ​singko-free record because of ES 
# 26; to avoid that, you consider dropping the course. To prove that 
# you have what it takes to get a 3.0 at least in this programming 
# course, you decide to cook up a program which will tell you 
# whether  or not you should be adding another DRP to your poor 
# transcript.

# This particular ES 26 course has its grade breakdown scheme as 
# follows:
# Pre-final grade: 70%
#		a. Long exams (3): 30% each
#		b. Attendance: 10%
# Final exam: 30%

# You have already taken three long exams; assume that you will be
# maintaining your perfect attendance until the end of the semester. 
# To pass the course (i.e., get a 3.0), your final grade must be at 
# least 60%. Assume that there are no bonus points and/or extra credit to save you.

# Input
# Three numbers (0 to 100) indicating your grade (percentage-wise) 
# for the first three long exams

# Output
# A message indicating whether or not you should drop the course
# considering the possibility of a passing mark (i.e., will I get at 
# least 60% if I perfect all remaining exams?)


LE1 = int(input("LE 1: "))
LE2 = int(input("LE 2: "))
LE3 = int(input("LE 3: "))


result = (LE1*0.3 + LE2*0.3 + LE3*0.3 + 10)*.7 + 30

if result < 60:
	out = "Advised to drop."
else:
	out = "Can still pass."

print(out)




