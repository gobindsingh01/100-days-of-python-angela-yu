#Day 2
print("Welcome to the tip calculator!")
total_bill=float(input("What was the total bill? $ "))
tip=int(input("How much tip would you like to give? 10, 12, or 15? "))
people=int(input("How many people to split the bill? "))
final=(total_bill + (total_bill*tip/100))/people
final=round(final,2)
print(f"Each person should pay: ${final:.2f}")