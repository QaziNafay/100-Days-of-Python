# 100 Days of Python

This repository serves as my practice ground for learning python

## System Info
* **Language:** Python 3.13
* **Environment:** Strictly isolated virtual environment (`.venv`)
* **Tracking:** Monolithic repository structure with daily atomic commits.

## Logs
* **Day 0:** Environment Configuration & Initial Execution ("Hello World")

# Day 1: Python Basics

##  Core Functions Learned
* **`print()`**: I learned about the `print()` function today and how it displays an output in the IDE.
* **`\n` (Escape Character)**: Simultaneously, I learned about the `\n` escape character, which helps with line breaks.
* **`input()`**: The `input()` function serves as a prompt to capture data from the user.
* **`len()`**: The `len()` function can then be used to count characters in a given string.

##  Key Concepts
* **String Concatenation**: String concatenation allows you to merge two or more string values with the `+` symbol, such as `"Wonder" + "Woman"`; however, it does not add a space automatically.
* **Variables**: Variables can be defined as names assigned to data; however, within the syntax of Python, they must follow certain rules: spaces must not be used, and a variable name should not begin with a number.

##  Daily Project
* **Brand Name Generator**: A Brand Name Generator was created from the basics of Python I learned today.

# Day 2: Data Types



## String
Can be defined as text data, however, it can also include numeric values and even emojis.

## Floats
Numerical data with decimals like 3.14.

## Booleans
Can have two values: True or False, it could be useful in conditional data types.

## Subscripting
Subscripting – returns a letter from string value, [0] counts as first letter


## Type Function
Type() function can return the type of data in output, also referred to as type checking.


## Type Conversion / Type Casting
Type conversion / type casting refers to converting a type of data into another, i.e. numerical string data to integer.


## Mathematical Operations in Python
+ operator is used for addition i.e. print(11 + 22)  
- operator used for subtraction i.e. print(22 - 11)  
* operator is used for multiplication i.e. print(11 * 11), while the operator ** is used for ^ or power i.e. print(4 ** 4)  
/ operator is used for division i.e. print(22 / 11),  

However, it may return a float value, a default Python behavior, sometimes referred to as “implicit type casting”. To overcome this, // can be used instead i.e. print(22 // 11), however, this second may not be ideal as it also removes values recurring after decimals.

## PEMDAS
PEMDAS should be used (Parenthesis, exponents, multiplication/division, addition/subtraction) while doing mathematical operations, and should be kept in mind as Python will prioritize all and produce unexpected results if PEMDAS is not being used, as Python executes from left to right.

## Round Function
round() function can round the value obtained via operator / to nearest whole number, while with round( , n digits) the number of digits after decimal can be specified.


## Assignment Operators
Assignment operators are used to change values of variables by performing an operation and storing the result back in the same variable using assignment operators such as +=, -=, *=, /=.



## F String
F string allows multiple data types to be present within a single expression.

# Day 3: Conditional logic

## If-else
if-else statements inside python can help create a flow of how a set of given should be executed

## Flattened if-else statements
Often use case for exclusive option, if one option is no executed then the other will be executed

## Nested if-else statements
Nested flow allows multiple other if-else statements to exit inside a flow, whether often each option is checked against some criteria

## elif
just as if-else, elif which stands for else-if, can be used between if and else statements

## indentation
Inside IDE, indents help you see flow of nested or flattened of conditional logic, they provide visual cues which are very important 

# # Day 4: Randomization in Python and lists

## Randomization
in Python is works by importing 'random' into python, random.randint(a, b) can generate random between numbers, while random.choice can be used for lists containing string data such as names

## Lists
In Python allow to create a set of data such as 'name of fruits', indexing inside the list or offset begins with 0, certain functions like append() add the items to the end of the list

## Nested lists
Allows multiple lists to exist to inside to single larger one

# Day 5: Loops

## Loops  
Loops allow repetitive execution of a block of code without rewriting it multiple times, making iteration efficient and structured.

## For and in function  
The `for` loop works with `in` to iterate through elements in a sequence such as lists or strings, executing code for each item.

## Range()  
The `range()` function generates a sequence of numbers within a given limit, commonly used with loops to control iteration count..

# Day 6: Functions

## Def
'Def' in python allows to define a function

# While
'While' function can be used to generate loops, and can be used alongside defined functions ('def') and even conditional logic can be used alongside it.

# Day 7: Hangman Game

## Exercise
The game brings back everything back together that was learned in previous 6 days, however it can be improved further.