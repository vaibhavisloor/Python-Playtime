
print('''
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
''')    

import os

def clear_terminal():
    os.system('cls')

print("Welcome to blind auction !")
another_participant = "yes"

bid_dict = {}

while another_participant == "yes":

    bidder_name = input("Enter your name : ")
    bid_amount = int(input("Enter the amount you want to bid : "))
    bid_dict[bidder_name] = bid_amount

    another_participant = input("Are there any more participants ?  ")
    clear_terminal()


max_bid = 0

for bidder in bid_dict:
    if bid_dict[bidder] > max_bid:
        max_bid = bid_dict[bidder]
        max_bidder_name = bidder

print(f"{max_bidder_name} has placed the highest bid worth {max_bid}")





