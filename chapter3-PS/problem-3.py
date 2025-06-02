# write a program to detect double white space in a string

text = "This  text   has double  spaces"
text2 = "This has no double space"

if "  " in text:
    print("Double space detected.")
else:
    print("No double space detected")

# Using find or index

position = text.find("  ")
if position != -1:
    print(f"Double space detected at {position}")

# how many extra spaces
count = text.count("  ")
print(f"Double spaces count {count}")