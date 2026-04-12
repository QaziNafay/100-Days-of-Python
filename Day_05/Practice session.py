student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

even_scores = []

for score in student_scores:
    if score % 2 == 0:
        even_scores.append(score)

print(even_scores)

odd_scores = []
for score in student_scores:
    if score % 2 != 0:
        odd_scores.append(score)
print(odd_scores)

pass_marks = []
for score in student_scores:
    if score >= 100:
        pass_marks.append(score)

print(pass_marks)

# just assuming list i have is now temperature values lol

temperature = ""
for temp in student_scores:
    print(f"{temp} C")