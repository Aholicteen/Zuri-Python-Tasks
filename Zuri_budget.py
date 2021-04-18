# Budget app
# Create budget category
# Deposit into budget category
# Withdraw from budget category
# Check category balance
# transfer balance amount between budget category
database = {}


class Budget:
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    def deposit(self, funds):
        funds += self
        return funds

    def withdraw(self, amount, funds):
        funds -= amount
        return funds

    def balance(self):
        for category, funds in self.items():
            # print("-BUDGET BALANCE-")
            # print(f'* {category} -- ₦{funds}')
            # return category, funds
            print('*', category, '--  ₦', funds)

    def transfer(self, fromBudget, amount, toBudget):
        fromFunds = self[fromBudget]
        toFunds = self[toBudget]

        self[fromBudget] = int(fromFunds) - amount
        self[toBudget] = int(toFunds) + amount


class InputException(Exception):
    pass


def init():
    print("Welcome to the Zuri Budgeting app!")
    mainMenu()


def mainMenu():
    try:
        option = int(input("What would you like to do? \n 1. Create a budget \n "
                           "2. Deposit funds into budget \n 3. Withdraw funds from budget \n "
                           "4. Check budget balance \n 5. Transfer funds between budgets \n 6. Exit \n"))
        if option == 1:
            newBudgetCat()
        elif option == 2:
            deposit()
        elif option == 3:
            withdraw()
        elif option == 4:
            balance()
        elif option == 5:
            transfer()
        elif option == 6:
            print("Thank you for using this app! Have a lovely day!")
            exit()
        else:
            print("Please select from the options available.")
            mainMenu()
    except Exception as _:
        print("Invalid Input")
        mainMenu()


def newBudgetCat():
    print("\n---CREATING A NEW BUDGET CATEGORY---")

    budgetName = input("Enter a budget name: ")

    try:
        budgetFunds = int(input("Enter budget funds: ₦"))
        if budgetFunds <= 0:
            print("Please enter a number greater than 0")
            newBudgetCat()
    except Exception as _:
        print("Input is invalid")
        newBudgetCat()

    database[budgetName] = budgetFunds
    print(f"{budgetName} budget has been set up with ₦{budgetFunds}")
    print('\n')
    mainMenu()


def deposit():
    print("\n---DEPOSIT FUNDS INTO BUDGET CATEGORY---\n")
    print("-CREATED BUDGET CATEGORIES-")
    for budgetName, budgetFunds in database.items():
        print(f"* {budgetName}")

    selectBudget = input("\nPlease type in the name of the budget you wish to deposit into: ")
    if selectBudget in database:
        try:
            depositAmount = int(input("How much would you like to deposit?: ₦"))
        except Exception as _:
            print("Invalid input")
            deposit()
        currentBalance = int(database[selectBudget])
        newBalance = Budget.deposit(depositAmount, currentBalance)
        database[selectBudget] = newBalance
        print(f'\nThe {selectBudget} budget has been credited with ₦{depositAmount}\n'
              f'{selectBudget} Budget funds is now ₦{newBalance} \n')
        mainMenu()
    else:
        print('')
        option = int(input(
            f'The {selectBudget} budget does not exist!\n Enter (1) To retry \n Enter (2) To create a new budget '
            f'\n Enter (3) To go back to the main menu\n'))
        if option == 1:
            deposit()
        elif option == 2:
            newBudgetCat()
        elif option == 3:
            mainMenu()
        else:
            print('Invalid option selected \n')
            deposit()


def withdraw():
    print("\n---WITHDRAW FUNDS FROM BUDGET CATEGORY---\n")
    print("-CREATED BUDGET CATEGORIES AND FUNDS ALLOCATED-")
    for budgetName, budgetFunds in database.items():
        print(f"* {budgetName} -- ₦{budgetFunds}")

    selectBudget = input("\nPlease type in the name of the budget you wish to withdraw from: ")
    if selectBudget in database:
        try:
            withdrawAmount = int(input("How much would you like to withdraw?: ₦"))
        except Exception as _:
            print("Invalid Input")
            withdraw()
        if withdrawAmount < database[selectBudget]:
            currentBalance = int(database[selectBudget])
            newBalance = Budget.withdraw(selectBudget, withdrawAmount, currentBalance)
            database[selectBudget] = newBalance
            print(f"\n₦{withdrawAmount} has been debited from the {selectBudget} budget.\n"
                  f"{selectBudget} budget amount remaining is ₦{newBalance}\n")
            mainMenu()
        else:
            selectInput = int(input(
                f'\nThe {selectBudget} budget has insufficient funds. \nYour current balance is {database[selectBudget]}'
                f'\n\nEnter (1) To retry \nEnter (2) to deposit funds into the current budget\n'))
            if selectInput == 1:
                withdraw()
            elif selectInput == 2:
                depositAmount = int(input("How much would you like to deposit?: ₦"))
                currentBalance = int(database[selectBudget])
                newBalance = Budget.deposit(depositAmount, currentBalance)
                database[selectBudget] = newBalance
                print('')
                print(f"The {selectBudget} budget has been credited with ₦{newBalance}\n")
                withdraw()
            else:
                print('Invalid option\n')
                withdraw()
    else:
        print('')
        option = int(input(
            f'The {selectBudget} budget does not exist!\n Enter (1) To retry \n Enter (2) To create a new budget '
            f'\n Enter (3) To go back to the main menu\n'))
        if option == 1:
            deposit()
        elif option == 2:
            newBudgetCat()
        elif option == 3:
            mainMenu()
        else:
            print('Invalid option selected \n')
            withdraw()


def balance():
    print("---CHECK YOUR BUDGET BALANCE---\n")
    print("Your budget balance is: ")
    Budget.balance(database)
    print('\n')
    mainMenu()


def transfer():
    print("\n---TRANSFER FUNDS BETWEEN BUDGET CATEGORIES---\n")
    print("-CREATED BUDGET CATEGORIES AND FUNDS ALLOCATED-")
    for budgetName, budgetFunds in database.items():
        print(f"* {budgetName} -- ₦{budgetFunds}")

    print("**** Transfer Operations ****")
    fromBudget = input("Enter the budget category you are transferring from: ")
    if fromBudget in database:
        try:
            fromAmount = int(input("Enter the amount you want to transfer: ₦"))
        except Exception as _:
            print("Invalid Input")
            transfer()
        if fromAmount < database[fromBudget]:
            toBudget = input("What budget category are you transferring to?: ")
            if toBudget in database:
                Budget.transfer(database, fromBudget, fromAmount, toBudget)
                print("")
                print(f"You have transferred ₦{fromAmount} from the {fromBudget} budget to the {toBudget} budget ")
                for category, funds in database.items():
                    print('*', category, '--  ₦', funds)
                    print('')
                mainMenu()
            else:
                print(f'\nThe {fromBudget} Budget does not exist, please choose from the budget options below\n')
                transfer()
        else:
            print(f'The {fromBudget} budget has insufficient funds. Current balance is ₦{database[fromBudget]}\n')
            transfer()
    else:
        print(f'The {fromBudget} budget does not exist\n')
        transfer()


init()
