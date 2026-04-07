# challenge from Angela
# i didn't hear the whole description but i have the got the gist of it

import random #chaos

print("Russian roulette with the bill begins")

friends_at_restaurant = ["Yagami Light", "No Face", "Sakamoto", "Bocchi the Rock", "Dio"]
# let's add a bit of twist
random_bill = random.randint(200, 100000)
assignment_index = random.randint(0,4)
print("The waiter churns the business cards in the bowl, the business that is drawn is belongs to:",friends_at_restaurant[assignment_index], "Your bill is:", str(random_bill))





if assignment_index == 0 and random_bill > 1000:
    print("Yagami light's internal monologue starts, because he knows he cannot change the bill with his notebook")

elif assignment_index == 0 and random_bill < 1000:
    print("Light: I think i can take a loan")

if assignment_index == 1 and random_bill > 1000:
    print("*Devours everyone*")

elif assignment_index == 1 and random_bill < 1000:
    print("Stares at everyone")

if assignment_index == 2 and random_bill > 1000:
    print("*Removes scarf and starts meowing*")

elif assignment_index == 2 and random_bill < 1000:
    print("*Presents tuna for payment*")

if assignment_index == 3 and random_bill > 1000:
    print("Actually, I'm pretty exhausted from all this social interaction, so I'm gonna go.")

elif assignment_index == 3 and random_bill < 1000:
    print("But if I do that, I'll write bitter, social-outcast lyrics")

if assignment_index == 4 and random_bill > 99000:
    print("Za Warudo! Sutando no pawā o zenkai da! * Times stops * but the bill remains the same.")

elif assignment_index == 4 and random_bill < 99000:
    others = friends_at_restaurant.copy()
    others.remove("Dio")
    stare_target = random.choice(others)
    print(f"Kisama wa ima made tabeta pan no mai-suu o oboete iru no ka? *Stares at {stare_target}* You ate. You didn’t count. Now I’m paying??")
    if stare_target == "Yagami Light":
        print("Yagami Light: hahahahah, Sō da... boku ga Kira da. *Pulls out notebook to deter*\n")
    elif stare_target == "No Face":
        print("No Face: Devours Dio")
    elif stare_target == "Sakamoto":
        print("Sakamoto: *Meows and licks paws")
    elif stare_target == "Bocchi the Rock":
        print("Bocchi the Rock: No, I just... the GPS said the trash cans were this way... I thought this was a dark corner where I could be alone forever... P-please don't look at me, I’ll explode...")