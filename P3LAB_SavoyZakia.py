is_leap_year = False
   
input_year = int(input())

''' Type your code here. '''
if (input_year % 4) == 0:            # inputYear is divisible by 4
    if (input_year % 100) == 0:       # inputyear is divisible by 100
        if (input_year % 400) == 0:   # inputyear is divisible by 400
            is_leap_year = True
        else:
            is_leap_year = False
    else:
        is_leap_year = True
else:
    is_leap_year = False
    
if is_leap_year:
    print(f'{input_year} - leap year')
else:
    print(f'{input_year} - not a leap year')