#This program calculates and displays travel expenses
# 2/28/2023
# CTI-110 P2HW1- Travel 
# Zakia Savoy
#

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
print("Location:                     ", destination)
print("Inital Budget:                $"  + str (budget) + "")
print("Fuel:                              $" + str (gas) + "")
print("Accomodation:             $" + str (accomodation) + "")
print("Food:                            $" + str (food) + "")
print("------------------------------------------------")
balance = budget - gas - accomodation - food
print("Remaining Balance:    $" + str (balance) + "")
