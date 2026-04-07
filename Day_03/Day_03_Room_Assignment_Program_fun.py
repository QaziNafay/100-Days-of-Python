# P.S. It's for fun only
# I have no mouth, and I must scream
# It's a computer terminal at ripper dock in night city

print("This is ripper dock terminal for blood donation, please proceed through instructions on the screen")

age = int(input("What is your age?"))

if age >= 18:
    print("You are eligible for blood donation")
    eligible = True
    if age >= 50:
        print("Please answer a few more questions before proceeding")
    heart_health = input("Do you have any heart condition? Reply with Y for yes or N for no\n").lower()
    if heart_health == "y":
        eligible = False

    haemoglobin_level = float(input("What is your haemoglobin level?\n"))
    if haemoglobin_level <= 13.5:
        eligible = False

    std_screening = input("Are you carrier of any STDs? Reply with Y for yes or N for no\n").lower()
    if std_screening == "y":
        eligible = False  # let's create an else statement

    if eligible:
        blood_type = input("What is your blood type? Reply with Y for O positive and Z for O negative\n").lower()

        donation_method = input(
            "How would you prefer to donate blood\n 1. Apheresis\n 2. Blood letting\n 3. Amputation\n")
        # oops
        if blood_type == "y":
            if donation_method == "1":
                print("You are assigned to room 411")
            elif donation_method == "2":
                print("You are assigned to room 412")
            elif donation_method == "3":
                print("You are assigned to room 413")
            else:
                print("You are awaited in room 420 by Adam Smasher ;)")

        elif blood_type == "z":
            if donation_method == "1":
                print("You are assigned to room 401")
            elif donation_method == "2":
                print("You are assigned to room 402")
            elif donation_method == "3":
                print("You are assigned to room 403")
            else:
                print("You are awaited in room 420 by Adam Smasher ;)")

        else:
            print("Invalid blood type Choom")

    else:
        print("You are not eligible for blood donation Choom")

# it was space related
else:
    print("You are not eligible for blood donation Choom")
    #Ok let's try
    # why didn't show that else message, let's try again
    # i think it will work now
    # phew c:
    # hmm now it's not asking the questions