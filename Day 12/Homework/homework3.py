# შექმენით პროგრამა, რომელიც სთხოვს მომხმარებელს შეიყვანოს დადებითი მთელი რიცხვი, შექმნილ ცვლადში რომლის სახელიც არის num, შემდეგ გგამოითვალოს და დაბეჭდოს ყველა რიცხვის ჯამინ 1-დან num-მდე
num = int(input("Enter integer: "))

sum_numbers = 0

if num <= 0:
    print("The number must be higher than 0.")
else:
    for i in range(1, num + 1):
        sum_numbers += i

    print(f"The sum of all numbers from 1 to {num} is {sum_numbers}.")

