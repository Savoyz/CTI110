#CTI-110
#P4HW2-Salary Calculator
#Zakia Savoy
#4/18/2023
#

def main():
    ovthrs = 0
    ovtpay = 0
    employee_count = 0
    overtime_total = 0
    regularpay_total = 0
    grosspay_total = 0
    name = input("Enter employee's name or " +'Done'+" to terminate: ")
    while name != "Done":
        hours = float(input(f"How many hours did "+ name +" work? "))
        payrate = float(input(f"What is "+ name + "'s pay rate? "))

        if hours > 40:
            regpay = payrate * 40
            ovthrs = hours - 40
            ovtpay = payrate * ovthrs * 1.5
            grosspay = ovtpay + regpay
        else:
            regpay = hours * payrate
            grosspay = hours * payrate
        
        employee_count = employee_count + 1
        overtime_total = overtime_total + ovtpay 
        regularpay_total = regularpay_total + regpay
        grosspay_total = grosspay_total + grosspay 

        var1 = hours
        var2 = payrate
        var3 = ovthrs
        var4 = ovtpay
        var5 = regpay
        var6 = grosspay

        print()
        print("Employee name:", name)
        print()
        print("Hours Worked   Pay Rate   OverTime   OverTime Pay   RegHour Pay   Gross Pay")
        print("-"*80)
        print(f'{var1:<15}{var2:<11.2f}{var3:<11}{var4:<15.2f}${var5:<13.2f}${var6:<12.2f}')
        print()
        print()
        name = input("Enter employee's name or 'Done' to terminate: ")
    print("Total number of employees entered: ", employee_count)
    print("Total amount paid for overtime: $",overtime_total)
    print("Total amount paid for regular hours: $",regularpay_total)
    print("Total amount paid in gross: $",grosspay_total)

main()

