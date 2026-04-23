import art

print(art.logo)

def highest_bid(bidding_dictionary):
    winner = ""
    highest_amount = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_amount:
            highest_amount = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_amount}")


bid_info = {}

continue_bidding = True
while continue_bidding:
    name = input("What is your name?\n")
    bid = int(input("What is your bid?: $\n"))

    bid_info[name] = bid

    should_continue = input(
        "Does somebody else want to bid? Reply with 'yes' or 'no'\n"
    ).strip().lower()

    if should_continue == 'no':
        continue_bidding = False
        highest_bid(bid_info)

    elif should_continue == 'yes':
        print("\n" * 15)