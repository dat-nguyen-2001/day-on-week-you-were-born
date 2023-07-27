import datetime 

user_input = input("Enter your date of birth: (for example 21/11/2001) \n")
input_list = user_input.split('/')
day = int(input_list[0])
month = int(input_list[1])
year = input_list[2]
year_first_half = int(year[0:2])
year_last_half = int(year[2:4])

numbers_for_months = [
    1 if int(year_last_half)//4 == 0 else 1,
    4 if int(year_last_half)//4 == 0 else 3,
    4,
    0,
    2,
    5,
    0,
    3,
    6,
    1,
    4,
    6
]

A = year_last_half 
B = A//4
C = numbers_for_months[month - 1]
D = day 
E = 6 if year_first_half == 20 else 0
F = A + B + C + D + E 
G = F%7 

match G:
    case 0:
        print('Saturday')
    case 1: 
        print('Sunday')
    case 2: 
        print('Monday')
    case 3: 
        print('Tuesday')
    case 4:
        print('Wednesday')
    case 5: 
        print('Thursday')
    case 6: 
        print('Friday')