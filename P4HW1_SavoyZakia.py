#CTI-110
#P4HW1 - Score List
#Zakia Savoy
#4/5/2023
#

def main():

    grade = 0
    total = 0
    grade_list = []

    num=int(input("How many scores do you want to enter: "))

    for i in range(0, num):
        grade = float(input("Enter score #" + str(i + 1)+ ": "))
        while grade < 0 or grade >100:
            print()
            print("INVALID Score entered!!!!")
            print("Score should be between 0 and 100")
            grade = float(input("Enter score #" + str(i + 1)+ " again: "))
        grade_list.append(grade)
    lowest = min(grade_list)
    grade_list.remove(lowest)
    print()
    print()
    print('-'*14 + "Results" + '-'*11)
    print("Lowest Score   :", format(lowest,',.1f'))
    print("Modified List  :", grade_list)
    average = sum(grade_list)/ (num - 1)
    print("Scorces Average:", format(average,',.2f'))
    if average > 90:
        grade = 'A'
    elif average >= 80:
            grade = 'B'
    elif average >= 70:
            grade = 'C'
    elif average >= 60:
            grade = 'D'
    else:
        grade = "F"
    print("Grade          :",grade)
    print('-'*35)


main()
