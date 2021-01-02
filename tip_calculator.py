greeting =("Welcome to the tip calculator! Ya Cheap bastard")
print (greeting)

bill = float(input("What was the total bill? Be honest! $"))
percentage = int(input("What percentage tip would you like to give? 15, 20, or 25? "))
split = int(input("How many people will be splitting the bill? "))
tip = float(1 + percentage / 100)

total = int(bill / split * tip)
final = "{:.2f}".format(total)
print = input(f"Each person should pay ${final}")