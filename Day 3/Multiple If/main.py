print("Welcome to the roller coaster")
height = int(input("Enter your height: "))

bill = 0

if height >= 120:
    print("You can ride the roller coaster")
    age = int(input("What is your age? "))
    
    if age < 12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7")
    else: 
        bill = 12
        print("Adult tickets are $12")
        
    want_photos = input("Do you want photos? Y or N --> ")
    if want_photos == "Y": 
        bill += 3
        
    print(f"Your final bill is ${bill}")
    
else:
    print("Sorry, you are too short.")