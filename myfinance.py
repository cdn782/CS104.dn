import math  # Importing math library

def main(): # the main list
    transactions = []
    runningTotal = 0
    while True:
        choice = printMenu()
        if choice == '1':
            CalculateNetPay()
        elif choice == '2':
            runningTotal = trackExpenses(transactions, runningTotal)
        elif choice == '3':
            calculateDiscretionaryIncome(transactions, runningTotal)
        elif choice == '4':
            print("\nThanks for using My Finance!")
            break
        else:
            print("Please enter a valid number choice #1 - 4")

def printMenu(): # presenting the menu
    print("\n1 - Calculate net pay")
    print("2 - Enter revenue or expense")
    print("3 - Show discretionary income")
    print("4 - Exit")
    choice = input("\nChoice: ")
    return choice

def CalculateNetPay(): #solving the netpay
    hourWage = float(input("What is your hourly wage? "))
    hoursWorked = float(input("How many hours did you work? "))
    # Formula for net pay calculation
    gross = hourWage * hoursWorked
    fedTax = gross * 0.1
    stateTax = gross * 0.05
    socSec = gross * 0.062
    netpay = gross - (fedTax + stateTax + socSec)
    print(f"Gross Pay: ${gross:.2f} ({hoursWorked} hours @ ${hourWage:.2f}/hr)")
    print(f"Federal Tax: ${fedTax:.2f}")
    print(f"State Tax: ${stateTax:.2f}")
    print(f"Social Security: ${socSec:.2f}")
    print(f"Net pay: ${netpay:.2f}\n")
    return netpay

def trackExpenses(transactions, total): #solving and returing of expenses
    while True:
        name = input("Enter transaction name: ")
        amount = float(input("Enter amount (use negative sign for expense): "))
        transactions.append(amount)
        total += amount
        answer = input("Input another? (Y/N): ")
        if answer.upper() != 'Y':
            return total

def calculateDiscretionaryIncome(transactions, total): #gathering and disclosing outputs 
    totalRev = 0
    expenses = 0
    for n in transactions:
        if n > 0:
            totalRev += n
        else:
            expenses += n
    print(f"Revenue: ${totalRev:.2f}")
    print(f"EXpenses: ${expenses:.2f}")
    print(f"Discretionary: ${total:.2f}")


main()
