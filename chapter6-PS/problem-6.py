marks = int(input("Enter your marks: "))

if marks>=90 and marks<=100:
    print("Excellent.")
elif marks>=80 and marks<90:
    print("A grade.")
elif marks>=70 and marks<80:
    print("B grade.")
elif marks>=60 and marks<70:
    print("C grade.")
elif marks>=50 and marks<60:
    print("D grade.")
else:
    print("Failed.")