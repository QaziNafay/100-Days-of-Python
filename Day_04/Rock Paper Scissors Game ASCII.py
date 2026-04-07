# I think this is going to be easy
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

ascii_set = [rock, paper, scissors]

import random

print("Welcome to the Rock Paper Scissors Game!")
user_choice = int(input("Rock, paper, scissors, what do you choose? Reply with 0 for Rock, 1 for paper, and 2 for scissors:\n"))
if user_choice >=0 and user_choice <= 2:
    print(ascii_set[user_choice])

computer_choice = random.randint(0, 2)
print("computer chose:")
print(ascii_set[computer_choice])

if user_choice >= 3 or user_choice <0:
    print("Invalid choice")
if user_choice == 0 and computer_choice == 2:
    print("You win")
if computer_choice == 0 and user_choice == 2:
    print("You lose")
elif computer_choice > user_choice:
    print("You lose")
elif user_choice > computer_choice:
    print("You win")
elif computer_choice == user_choice:
    print("Draw")