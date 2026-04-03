# Today i got to learn about data type
print("String data aka text, string data gets treated as text")
print(type("string"))
print(11)
print(type(11))
print(3.14)
print(type(3.14))
print(True) #my bad
print(type(True))
# So it was pretty interesting, now let me look up what else i learned today
# Let's try subscripting
print("Number"[0] + " \nIt will print N because that is the first letter, and in python it starts with 0")
# now that's better
# let's convert some data types
print(type(int("11")))
# now this is actually a string converted to integer
print(type(str(11)))
# and here just converted an integer to string
# Another thing i learned about today was Mathematical operators such as * / + -
print((5 * 5), (25 // 5), (10 + 10), (20 - 10))
# if we make use of // then decimal points aren't included
# The operator ** is used for power or exponents
print(4 ** 4)
# Let's try rounding
division_example = 7 / 3
print(round(division_example, 2)) # we want the value rounded off by 2 digits after decimal. Ok this will do c:
# Another important thing i learned today was that in a single expression two different data types cannot be expressed
# Unless conversion or some other method is used, so let's try
print("Letters in your name: " + str(len(input("What is your name?"))))
# Without conversion, it would have given me an error
# Let's move on to BMI calculator for now