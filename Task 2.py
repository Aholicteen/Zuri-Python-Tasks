from datetime import date
today = date.today()
print("Today's date is:", today)

name = input("Hello, what is your name? \n")
print("Welcome %s. What would you like to do?" % name)
print("1. Withdrawal")
print("2. Cash Deposit")
print("3. Complaint")

balance = 0
while True:
    option = int(input("Please select an option: \n"))
    if option == 1:
        with_amount = int(input("How much would you like to withdraw?: \n"))
        print("Take your cash", with_amount)
        break
    elif option == 2:
        dep_amount = int(input("How much would you like to deposit?: \n"))
        print("Current balance is:", dep_amount + balance, "Naira")
        break
    elif option == 3:
        complaint = input("What issue will you like to report?: \n")
        print("Thank you for contacting us")
        break
    else:
        print("That option isn't available.")
