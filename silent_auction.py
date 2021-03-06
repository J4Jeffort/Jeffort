bids = {}
finished = False
def find_winner(bidding_record):
	highest_bid = 0
	winner = ""
	#{bidding_record ="Angela": 123, "James": 321}
	for bidder in bidding_record:
		bid_amount = bidding_record[bidder]
		if bid_amount > highest_bid:
			highest_bid = bid_amount
			winner = bidder
	print(f"The winner is {winner} with a bid of ${highest_bid}")


while	not finished:
	name = input("What is your name? ")
	price = int(input("What is your bid? $"))
	bids[name] = price
	repeat = input("Are there more people that would wish to bid? 'Yes or No'.\n ").lower()
	if repeat == "no":
		finished = True
		find_winner(bids)
	elif repeat == "yes":
