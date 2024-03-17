# შექმენით პროგრამა რომელიც მომხმარებელს შეეკითხება პაროლს, იქამდე უნდა შეეკითხოს სანამ პაროლი სწორი არ იქნება.

correct_password = '0123456789'

while True:
    user_password = input("Enter the password: ")
    
    if user_password == correct_password:
        print("Correct.")
        break  
    else:
        print("Incorrect. Try again.")
