def sumofNumbers(n):
    if n==0:
        return sum
    sum = n+sum
    return sumofNumbers(n-1)

n = int(input("Enter the number: "))

print(f"Sum of {n} natural numbers is: {sumofNumbers(n)}")