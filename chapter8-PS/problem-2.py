def celciusToFahrenheit(c):
    f = (9/5)*c+32
    return f

c = float(input("Enter the temparature: "))

print(f"{c} celcius in fahrenheit {celciusToFahrenheit(c)}")