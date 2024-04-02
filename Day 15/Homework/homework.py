score = int(input("Enter your score"))

if 90 < score < 100:
    print("You will be fully funded.")
elif 70 < score < 80:
    print("You will be financed with 1500 GEL.")
elif 40 < score < 70:
    print("You will be financed with 500 GEL.")
elif score < 40:
    print("You will not be funded.")
