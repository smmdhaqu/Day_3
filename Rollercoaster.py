print("Welcome to the Rollercoaster")
height = int(input("Enter your recent height in cm: "))
bill = 0
if height != 120:
    print ("You are allowed to ride the Rollercoaster!")
    age = int(input("enter your age: "))
    if age <12:
        bill = 5
        print("You have to pay $5")
    elif age <= 18:
        bill = 7
        print("You have to pay $7")
    else:
        bill = 12
        print("You have to pay $12.")
    want_photo = input("Do you want to take photos? Yes or No! ")
    if want_photo == "Yes":
        bill += 3
        print(f"Your total Bill is ${bill}")
else:
    print("You are not allowed to ride now!" )