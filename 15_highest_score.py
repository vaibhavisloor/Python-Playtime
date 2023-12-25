# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

max_val = student_scores[0]
#Write your code below this row 👇
for score in student_scores:
  if score > max_val:
    max_val = score

print(max_val)
