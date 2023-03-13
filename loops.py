
#1)Write a program that takes a user input (an integer) and determines whether it is positive, negative, or zero.

integer = int(input('enter the integer: '))

if integer < 0:
    print('integer is negative')
elif integer == 0:
    print('integer equals zero')
else:
    print('integer is positive')

#2)Write a program that prints out the numbers from 1 to 100. But for multiples of three, print "Fizz" instead of the
# number and for multiples of five, print "Buzz".
#For numbers that are multiples of both three and five, print "FizzBuzz".

for numb in range(1, 101):
    if numb % 3 == 0 and numb % 5 == 0:
        print('FizzBuzz')
    elif numb % 3 == 0:
        print('Fizz')
    elif numb % 5 == 0:
        print('Buzz')
    else:
        print(numb)

#3)Write a program that takes an integer as input and prints out all the factors of that integer.

integer = int(input('enter the integer: '))

if integer >= 0:
    factorial = 1
    for i in range(1,integer + 1):
        factorial *= i
    print('Factorial is ', factorial)
else:
    print("The value can't be negative")

'''4)Create calculator:
  Ask user to provide 2 numbers and one operation to be performed (*,/,+.- or %). If the operation 
  provided does not match one of these, the program should print 
  "Operation provided isn't valid, please,try again" - in this case, the program should
'''

def calculator():
    num1 = float(input('enter first number: '))
    num2 = float(input('enter second number: '))
    operation = input('enter one operation to be performed (*,/,+,- or %): ')

    if operation == '*':
        print(num1 * num2)
    elif operation == '/':
        print(num1 / num2)
    elif operation == '+':
        print(num1 + num2)
    elif operation == '-':
        print(num1 - num2)
    elif operation == '%':
        print(num1 % num2)
    else:
        print("Operation provided isn't valid, please,try again")
        reply = input('continue? (y/n): ')
        if reply == 'y':
            calculator()

calculator()


#5)Write a program that takes an integer as input and prints out whether that integer is prime or not.

num = int(input('enter the integer: '))

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print('integer is not a prime number')
            break
    else:
        print('integer is a prime number')
else:
    print('integer is not a prime number')