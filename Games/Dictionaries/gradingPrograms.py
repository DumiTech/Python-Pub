student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}
print(student_scores)

for key in student_scores:
    value = student_scores[key] #value
    if value >= 91 and value <= 100:
        student_grades[key] = "Outstanding"
    elif (value >= 81 and value <= 90):
        student_grades[key] = "Exceeds Expectations"
    elif (value >= 71 and value <= 80):
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

print(student_grades)