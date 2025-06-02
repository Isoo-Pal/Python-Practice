from datetime import date
name = input("Enter you name:")
today = date.today()

letter = f'''
Dear {name},
You are selected!
{today}
'''
print(letter)

