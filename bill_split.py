
print ("**Bill & Tip Splitter** ")

while True:
    bill_input = input("Enter the bill amount(TND): ")
    bill = float(bill_input)
    
    tip_input = input("Enter tip percentage (e.g., 15 for 15%): ")
    tip_percent = float(tip_input)
    
    people_input = input("How many people are splitting? ")
    people = int(people_input)
    
    tip_amount = bill * (tip_percent / 100)
    total_bill = bill + tip_amount
    
    per_person = total_bill / people
    
    print("\n------")
    print("RESULT:")
    print("Bill amount: " + str(round(bill, 2)))
    print("Tip amount:  " + str(round(tip_amount, 2)))
    print("Total price: " + str(round(total_bill, 2)))
    print("________________________________________________")
    print("Each person should pay: TND" + str(round(per_person, 2)))
    print("-------------------------\n")
    
    again = input("Do you want to split another bill? (y/n): ")
    if again != "y" and again != "yes":
        print("Thanks for using my program! Bye!")
        break