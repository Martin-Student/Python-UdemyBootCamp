
bids = {}

participant = True

def find_highest_bidder(bidding_record):
    highest_bid = 0
    # bidding_record = {"Name": 123, "Name2": 321}
    for bidder in bidding_record:
        bid_ammount = bidding_record[bidder]
        if bid_ammount > highest_bid:
            highest_bid = bid_ammount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while participant == True:
    name = input("What's your name? ")
    price = int(input("What's your bid? $"))
    bids[name] = price
    want = input("Are there any other bidders? YES/NO").lower()
    if want == "yes":
        participant = True
    else:
        find_highest_bidder(bids)
        participant = False



