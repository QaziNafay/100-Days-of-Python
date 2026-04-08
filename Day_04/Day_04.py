# i just learned about random in python, i am going to create a heads and tails program
import random

random_no_range = random.randint(1, 2)

user_choice = input("heads or tails?\n").lower()


if random_no_range == 1 and user_choice == "heads":
    print("As the coin is flung mid air in seemingly perpetual motion, it whirls and falls down:\n Heads")
    print("you win")

elif random_no_range == 2 and user_choice == "heads":
    print("The chaotic swerving in a deterministic system begins and ends with:\n Tails")
    print("you lose")

elif random_no_range == 2 and user_choice == "tails":
    print("You see the coin fall as if your life depends on it, in front of your eyes it settles on the ground:\n Tails")
    print("You win")

elif random_no_range == 1 and user_choice == "tails":
    print("If the rule you followed, brought you to this, of what use was the rule? The truth is revealed:\n Tails")
    print("You lose")

else:
    print("Well, probably some particle from cosmic radiation interacted with my circuits and flipped a very sensitive bit which resulted in an unholy (Pythagorean reference c:) output:\nDraw")

# This programs hints at interplay of chaos and order in nature and universe as a whole, for more look up the video titled "The relationship between chaos, fractal and physics" on YT