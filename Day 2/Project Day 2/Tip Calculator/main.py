print("Welcome to the Tip Calculator\n")

total_bill = int(input("What was your total bill? $"))

tip = int(input("How much tip would you like to give? 10, 12, 15? "))

new_bill = total_bill + (total_bill * tip/100)

no_of_people = int(input("How many people to split the money? "))

split_per_person = new_bill / no_of_people
round_off = round(split_per_person, 2)

print(f"Each person should pay ${round_off}")