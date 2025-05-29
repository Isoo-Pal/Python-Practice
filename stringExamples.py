str = "radhika is a world world world of abc and xyz"

print(len(str))

# slicing

print(str[1:3])

print(str[4:5])

print(str[:4])
print(str[-4:-1])

print(str[:-4])

print(str[1:5:2])


# Functions
print(str.endswith('ka'))  #return true or false
print(str.startswith('ra'))  #return true or false
print(str.capitalize())   #capitalize first letter of first word

print(str.upper())  #converts whole string in upper case
print(str.lower())#converts whole string in lower case

print(str.find("dhi"))  #returns index of first letter 
print(str.replace("world", "Cosmos"))   #replace all occurances of the given word

# Escape sequences


print("Escape sequences:\n")
str2 = "Harry is a good teacher\nbut not a bad \tteacher"

print(str2)