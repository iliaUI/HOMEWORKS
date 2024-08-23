balance = input("whats your balance")

user_input = input("Write here when you want to eat: ")


if user_input == "i want to eat":

    amount = balance * 0.80
    print("You left" + str(amount))
else:
    print("You didn't say you want to eat.")