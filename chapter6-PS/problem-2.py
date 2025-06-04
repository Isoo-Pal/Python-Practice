mark1 = int(input("Enter your first subject marks: "))
mark2 = int(input("Enter your second subject marks: "))
mark3 = int(input("Enter your third subject marks: "))
total_marks = mark1+mark2+mark3
per = (total_marks/300) * 100


if per>=40 and mark1>=33 and mark2>=33 and mark3>=33:
    print("Passed.")
else:
    print("Failed")