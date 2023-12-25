print("Welcome to blind auction")
more_bidders = 'y'
bidders = {}

while more_bidders == 'y':
    bidder = input("Enter bidder name and bid amount : ").split()
    bidders[bidder[0]] = int(bidder[1])
    more_bidders = input("More bidders ?? 'y' or 'n'").lower()


print(bidders)
max_bid = 0

for bid in bidders:
    if bidders[bid] > max_bid :
        max_bid = bidders[bid]
        max_bidder = bid

print(f"The highest bidder is {max_bidder} whose has a bid of Rs.{max_bid}")