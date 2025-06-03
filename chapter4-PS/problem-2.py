# code for taking marks of 6 students and show them in sorted manner

marks = []

print("Enter marks: ")
for i in range(0,6):
    m = input()
    marks.append(m)

marks.sort()
print(marks)