#CTI 110
#P3HW2-Salary
#Zakia Savoy
#3/23/2023
#

name = input("Enter employee's name:")
hours = float(input("Enter number of hours worked:"))
payrate = float(input("Enter employee's pay rate:"))
ovthrs = 0.0
ovtpay = 0.0

if hours > 40:
    regpay = payrate * 40
    ovthrs = hours - 40
    ovtpay = payrate * ovthrs * 1.5
    grosspay = ovtpay + regpay
else:
    regpay = hours * payrate
    grosspay = hours * payrate
    
var1 = hours
var2 = payrate
var3 = ovthrs
var4 = ovtpay
var5 = regpay
var6 = grosspay

print("-"*30)
print("Employee name:", name)
print()
print("Hours Worked   Pay Rate   OverTime   OverTime Pay   RegHour Pay   Gross Pay")
print("-"*80)
print(f'{var1:<15}{var2:<11}{var3:<11}{var4:<15.2f}${var5:<13.2f}${var6:<12.2f}')

