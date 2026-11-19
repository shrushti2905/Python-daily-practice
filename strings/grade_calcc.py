# Calculate a student's grade based on their percentage.

marks = [75, 80, 65, 90, 85]

average = sum(marks) / len(marks)

if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 40:
    grade = "D"
else:
    grade = "Fail"

print("Average:", average)
print("Grade:", grade)