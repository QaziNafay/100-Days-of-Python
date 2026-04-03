# Let's make a tip calculator
print("Welcome to the tip calculator")
bill = float(input("How much was your bill? "))
tip = int(input("How much tip would you like to give?5 8 10")) #in percentage
people = int(input("How many people to split the bill? "))
total_bill = bill * (1 + tip / 100)
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"Each person should pay: ${final_amount}")
