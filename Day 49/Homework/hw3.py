weight_input = float(input("Enter your weight:"))

if weight_input < 18.5:
    print("You are underweight")
elif 18.5 <= weight_input < 25:
    print("You have normal weight")
elif 25 <= weight_input < 30:
    print("You are overweight")
else:
    print("Obesity")