# If the bill was 8000, split between 5 people with 12% tip.
# eg. Each person should pay ( 8000 / 5 ) * 1.12 = 1792
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? INR\n"))

# print(type(bill))
tip = int(input("How much percent would you like to give? 10, 12, or 15\n"))
# print(type(tip))
people = int(input("How many people to split the bill\n"))
# print(type(people))
# bill_with_tip = tip / 100 * bill + bill

tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 6)

final_amount = "{:.2f}".format(bill_per_person)
# print(bill_with_tip)
print(f"Each person should pay {final_amount} INR Rupee")