# Today i got to learn about loops in lists
# say this is example of var / list of anime characters

villains = ["Dio", "Griffith", "Nanook", "Yagami Light", "Frieza"]

# now let's suppose we want dio gone in as the command i will give will go through list

vil_var = []

for vil in villains:
    if vil != "Dio":
        vil_var.append(vil)

print(vil_var)

# SPOILER ALERT:
# and that's the end of Dio's fight with Jotaro

# Now let's move on range()

for number in range(1, 101):
    if number % 11 == 0:
        print("Eleven was here")
    else:
        print(number)

# the sum() func

numbers = (4, 23, 62, 62, 1, 2, 63, 7,)
addition = sum(numbers)
print(addition)

