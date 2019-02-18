#UP Grade Converter

grade = float(input("Grade: "))

if 92 <= grade:
	upGrade = 1.0
elif 88 <= grade < 92:
	upGrade = 1.25
elif 84 <= grade < 88:
	upGrade = 1.5
elif 80 <= grade < 84:
	upGrade = 1.75
elif 76 <= grade < 80:
	upGrade = 2.0
elif 72 <= grade < 76:
	upGrade = 2.25
elif 68 <= grade < 72:
	upGrade = 2.5
elif 64 <= grade < 68:
	upGrade = 2.75
elif 60 <= grade < 64:
	upGrade = 3.0
elif 56 <= grade < 60:
	upGrade = 4.0
elif grade < 56:
	upGrade = 5.0

print("Your grade is", upGrade)
