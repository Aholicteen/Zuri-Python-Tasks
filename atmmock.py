# Register
# - First name, last name, password, email.
# - Generate account number.

# Login
# - Email and password.

# Bank operations
# - Withdrawal
# - Deposit
# - Complaint
# - Exit

import random
from datetime import date

database = {}

today = date.today()
print("Today's date is:", today)


def init():
    print("Welcome to Zuri Bank")
    while True:
        haveAccount = int(input("Do you have an account with us? \n 1 - Yes. \n 2 - No. \n"))
        if haveAccount == 1:
            login()
            break
        elif haveAccount == 2:
            register()
            break
        else:
            print("You have selected an invalid option")


def login():
    print("---------- Login ----------")

    correctInput = False
    count = 0

    while not correctInput:
        userEmail = input("Please input your email address? \n")
        password = input("Please input your password \n")
        for accountNumber, userDetails in database.items():
            if userEmail == userDetails[2]:
                if password == userDetails[3]:
                    correctInput = True
                    bankOperations(userDetails)
                    break
        else:
            print("Incorrect Email or password!")
            count = count + 1
            if count == 4:
                register()


def register():
    print("---------- Register ----------")

    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("create a password \n")
    accountNumber = accNoGeneration()

    database[accountNumber] = [first_name, last_name, email, password]

    print("You have successfully created an account!")

    login()


def bankOperations(user):
    print("Welcome %s %s," % (user[0], user[1]))

    correctInput = False

    while not correctInput:
        optionSelected = int(input("What would you like to do? \n 1. Withdrawal \n "
                                   "2. Cash Deposit \n 3. Complaint \n 4. Exit \n"))

        if optionSelected == 1:
            correctInput = True
            withdraw()
        elif optionSelected == 2:
            correctInput = True
            deposit()
        elif optionSelected == 3:
            correctInput = True
            complaint()
        elif optionSelected == 4:
            correctInput = True
            exit()
        else:
            print("You have selected an invalid option.")


def accNoGeneration():
    return random.randrange(1111111111, 9999999999)


def withdraw():
    with_amount = int(input("How much would you like to withdraw?: \n"))
    print("Take your cash N", with_amount)
    notFinished()


def deposit():
    balance = 0
    dep_amount = int(input("How much would you like to deposit?: \n"))
    print("Current balance is:", dep_amount + balance, "Naira")
    notFinished()


def complaint():
    input("What issue will you like to report?: \n")
    print("Thank you for contacting us! Your complaint has been received!")
    notFinished()


def notFinished():
    value = int(input("Would you like to do anything else? \n 1. Yes \n 2. No \n"))
    if value == 1:
        login()
    else:
        exit()


# Banking System Main


init()
