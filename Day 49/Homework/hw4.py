def get_bid():
    bid_input = input("Enter a bid (or type 'done' to end): ")
    if bid_input.lower() == 'done':
        return None
    try:
        return float(bid_input)
    except ValueError:
        print("Invalid input. Please enter a numeric value or 'done'.")
        return get_bid()  

def auction():
    max_bid = 1600
    highest_bid = 0

    print("Auction started. Place your bids.")

    while True:
        bid = get_bid()
        if bid is None:
            break
        if bid <= max_bid:
            if bid > highest_bid:
                highest_bid = bid
            print(f"Current highest bid: {highest_bid}")
        else:
            print(f"Bid exceeds the maximum limit of {max_bid}. Please enter a lower bid.")

    if highest_bid > 0:
        print(f"Sold: {highest_bid}")
    else:
        print("No valid bids were made.")

auction()
