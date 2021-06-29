print("Welcome: ")
bill = float(input("Enter Total Bill$"))
tip = float(input("Enter the tip percentage$"))
people = int(input("Total no of people: "))
tipP = tip/100
tipAmt = bill*tipP
total_bill = bill + tipAmt
bill_per_person = round(total_bill/people,2)
finalAt = "{:.2f}".format(bill_per_person)
print(f"Each person would pay ${finalAt}")