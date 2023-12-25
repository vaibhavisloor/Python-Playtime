# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

total = 0
#Write your code below this row 👇
for height in student_heights:
  total+=height

print(int(total/len(student_heights)))

#You can use the sum() function alternatively




