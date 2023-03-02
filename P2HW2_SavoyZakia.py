#CTI-110
#P2HW2 - List
#Zakia Savoy
#3/2/2023
#

grade_list = [ ]
grade = float(input("Enter Grade for Module 1: "))
grade_list.append(grade)
grade = float(input("Enter Grade for Module 2: "))
grade_list.append(grade)
grade = float(input("Enter Grade for Module 3: "))
grade_list.append(grade)
grade = float(input("Enter Grade for Module 4: "))
grade_list.append(grade)
grade = float(input("Enter Grade for Module 5: "))
grade_list.append(grade)
grade = float(input("Enter Grade for Module 6: "))
grade_list.append(grade)

total = sum(grade_list)
length = len(grade_list)
average = format(total / length,".2f")
lowest = min(grade_list)
highest = max(grade_list)

print()
print("-"*12 + "Results" + "-"*12)
print("Lowest Grade:      ",lowest)
print("Highest Grade:     ",highest)
print("Sum of Grades:     ",total)
print("Average:           ",average)
print("-"*38)
