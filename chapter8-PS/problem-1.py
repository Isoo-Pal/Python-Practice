def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>c:
        return b
    else:
        return c
    

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))
res = greatest(a,b,c)
print(f"Greatest number is : {res}")