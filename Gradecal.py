# Input the score

score = float(input("Enter the student's score: "))

# Determine the grade based on the score

if score >= 90  :
    grade = 'A'

elif score >= 80 :
    grade = 'B'

elif score >= 70 :
    grade = 'C'

elif score >= 60 :
    grade = 'D'

else:
    grade = 'F'


print(grade)
