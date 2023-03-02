'''1.Create a program that asks the user to enter their age and whether or not they have a driver's license.
If the user is at least 18 years old and has a driver's license, the output should be as follows
You are able to drive : True
If not, then
You are able to drive : False'''

age = int(input('please, enter your ege: '))
is_license = input("do you have driver's license? yes/no: ")

result = age >= 18 and is_license == 'yes'
print('You are able to drive: ', result)


'''2. (Explore some String functions).Create a program that asks the user for a password, and checks if it meets the 
following criteria: at least 8 characters long
If the password meets all of these criteria, print "Password accepted : True", 
otherwise print "Password accepted : False".'''

psw = input('enter your password: ')
result = len(psw) >= 8
print('Password accepted: ', result)

'''3. Write a program that asks the user to enter two integers and checks if they are both even. 
If they are, print "Both numbers are even : True", otherwise print "Both numbers are even : False".
If at least one is even print "At least one number is even : True", else "At least one number is even : False".
Hint : use modulo operator % here
'''
int1 = int(input('enter first integer: '))
int2 = int(input('enter second integer: '))

a = (int1 % 2) == 0
b = (int2 % 2) == 0

if a == b:
    both = a and b
    print('Both numbers are even: ', both)
else:
    one_of = a or b
    print('At least one number is even: ', one_of)


'''4. Write a program that asks the user to enter a year and checks if it is a leap year. 
A leap year is defined as a year that is divisible by 4 but not by 100, or a year that is divisible by 400. 
If the year is a leap year, print "Leap year : True", otherwise print "Leap year : False".'''

year = int(input('please, enter a year: '))

is_leap_year = ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)
print('Leap year: ', is_leap_year)

'''5.Create the program which asks to enter the date (day, month, year). 
If the date is valid print : "Date valid : True" else "Date valid : False" '''

year = int(input('enter a year: '))
month = int(input('enter a month: '))
day = int(input('enter a day: '))

leap_year = ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)
valid_date = False

if year >= 0000 and year <= 9999:
    if month >= 1 and month <= 12:
        if month in [4, 6, 9, 11]:
            if day >= 1 and day <= 30:
                valid_date = True
        elif month in [1, 3, 5, 7, 8, 10, 12]:
            if day >= 1 and day <= 31:
                valid_date = True
        elif leap_year and day >= 1 and day <= 29:
            valid_date = True
        elif day >= 1 and day <= 28:
            valid_date = True

print("Date valid: ", valid_date)

