import math
num = int(input("Enter the number: "))

if num<2:
    print("Not prime.")
else:
    isPrime = True
    for i in range(2, int(math.sqrt(num))+1):
        if num%i == 0:
            isPrime = False
            break

if isPrime:
    print("Given number is a prime number.")
else:
    print("Given number is not a prime number.")