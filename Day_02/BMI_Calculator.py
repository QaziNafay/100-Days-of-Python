# Ok lets try to make one again
print("Welcome to the BMI Calculator")
height = float(input("What is your height in cm? "))
weight = float(input("What is your weight? "))
weight_type = input("is it KG or lbs?").lower() # i got this bit from GPT
if weight_type == "lbs":
    weight = weight * 0.453592
bmi = weight / (height ** 2)
print(F"Your BMI is ", (round(bmi, 2)))
      # i will probably use f string here
#