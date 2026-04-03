user_input = input("What is your name?\n")
length = len(user_input)
life_energy = 3.14 * length
print("Your life energy is:" + str(round(life_energy, 3)))
print(f"Your life energy is: {round(life_energy, 0)}")
# Fahrenheit to celsius calculator
print("Welcome to Fahrenheit to Celsius temperature calculator")
tmp_f = float(input("What is the temperature in Fahrenheit?"))
tmp_c = (tmp_f - 32) * 5 / 9
print("temperature in celsius is:" + str(round(tmp_c, 2)) +"°C")
#Interest calculator
print("Welcome to interest calculator!")
amount = float(input("Enter the amount: \n$"))
interest_percent = float(input("Enter the interest percent: \n"))
interest_amount = (amount * interest_percent) / 100
print("Your interest amount is:" + str(round(interest_amount, 2)))
# Bill split
print("Welcome to checkout")
bill = float(input("What was your bill amount?"))
people = int(input("How many people to split the bill?"))
amount_per_person = bill / people
print("Each person should pay $" + str(round(amount_per_person, 2)))
# Subscripting
print("Welcome to random mini game")
number = int(input("Enter a 6 digit whole number: "))
number_as_text = str(number)
print("first digit: " + number_as_text[0])
print("last digit: " + number_as_text[-1])
