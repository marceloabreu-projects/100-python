print("Welcome to the tip calculator!")
bill = input("What was the total bill? €")
tip = input("What percentage tip would you like to give? 10, 12 or 15 ")
people = input("How many people to split the bill? ")

tip_bill = float(bill) * (float(tip) / 100) + float(bill)  
split_bill = float(tip_bill) / (float(people))
print(f"Each person should pay {split_bill:.2f}€.")