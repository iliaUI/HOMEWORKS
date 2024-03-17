# შექმენით პროგრამა, რომელიც სთხოვს მომხმარებელს შეიყვანოს რიცხვი და შემდეგ ითვლის ამ რიცხვიდან 1-მდე.
user_input = input("Enter a number: ")

number = int(user_input)

if number <= 0:
    print("Please enter a number greater than 0.")
else:
    for i in range(number, 0, -1):
        print(i)