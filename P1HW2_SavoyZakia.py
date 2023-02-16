#This program calculates and displays travel expenses
# 2/16/2023
# CTI-110 P1HW2 - Travel Expense
# Zakia Savoy

print("This program calculates and displays travel expenses")
print()
budget = float(input("Enter Budget: "))
print()
destination = input("Enter your travel destination: ")
print()
gas = float(input("How much do you think you will spend on gas? "))
print()
accomodation = float(input("Approximately, how much will you need for accomodation/hotel? "))
print()
food = float(input("Last, how much do you need for food? "))
print()
print("------------Travel Expenses------------")
print("Location: ", destination)
print("Inital Budget: ", budget)
print()
print("Fuel: ", gas)
print("Accomodation: ", accomodation)
print("Food: ", food)
print()
balance = budget - gas - accomodation - food
print("Remaining Balance: ", balance)
