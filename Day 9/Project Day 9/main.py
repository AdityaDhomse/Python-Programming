logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''


def add_bidder():
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))
    auction_dictionary[name] = bid
    
def highest_bidder(dict):
    highest_bidder = ""
    highest_bid = 0
    
    for bidder in dict:
        bid_amount = dict[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            highest_bidder = bidder
        
    print(f"The winner is {highest_bidder} with a bid of ${highest_bidder}")
        

print(logo)
print("Welcome to the secret auction program.")
auction_dictionary = {}

add_bidder()

toContinue = True

while toContinue:
    choice = input("Are there any other bidders? Type 'yes' or 'no' : ")
    if choice == "yes":
        add_bidder()
    else:
        toContinue = False
        highest_bidder(auction_dictionary)

print(auction_dictionary)