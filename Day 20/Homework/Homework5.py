#5)მომხმარებელს შემოაქვს რიცხვი. შეამოწმეთ არის თუ არა ეს რიცხვი მარტიცი. თუ მარტიცია დაუპრინტეთ "თქვენი რიცხვი მარტივია", სხვა შემთხვევაში დაუპრინტეთ "თქვენი რიცხვი არ არის მარტივი"(მარტივი რიცხვი არის ისეთი ნატურალური რიცხვი რომელსაც გააჩნია მხოლოდ ორი გამოყოფი(1 და თავისი თავი))

num = int(input("enter numbers from 1 to 50:"))

if num // 1 and num // num:
    print("your number is simple") 
else:
    print("your number is not simple")