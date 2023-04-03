#1.Create a class named Car that has the following attributes: make, model, and year. It should also have a method
# called get_info() that returns a string with the car's make, model, and year.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return "Car made by " + self.make + " in " + self.year + ", model: " + self.model


car1 = Car("audi","80", "1985")
print(car1.get_info())

#2.Create a class named Rectangle that has the following attributes: width and height. It should also have methods
# called area() and perimeter() that return the area and perimeter of the rectangle, respectively.

class Rectangle:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def area(self):
        return self.width*self.height

    def perimeter(self):
        return (self.width+self.height)*2

rectangle1 = Rectangle(2, 3)
print(rectangle1.area())
print(rectangle1.perimeter())


#3.Create a class named BankAccount that has the following attributes: account_number, balance, and owner_name.
# It should also have methods called deposit() and withdraw() that update the balance accordingly.

class BankAccount:
    def __init__(self, account_number: str, balance: float, owner_name: str):
        self.account_number = account_number
        self.balance = balance
        self.owner_name = owner_name

    def deposit(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def withdraw(self, amount):
        self.balance = self.balance - amount
        return self.balance

account1 = BankAccount('LT123456789', 799.37, 'John Smith')
print(account1.deposit(100))
print(account1.withdraw(10))


#4.Create a class named Person that has the following attributes: name, age, and address.
# It should also have a method called get_info() that returns a string with the person's name, age, and address.

class Person:
    def __init__(self, name: str, age: int, address: str) -> None:
        self.name = name
        self.age = age
        self.address = address
    
    def get_info(self):
        return self.name + " is " + str(self.age) + " years old and lives in: " + self.address


person1 = Person("John","30", "Vilnius, Lithuania")
print(person1.get_info())

#5.Create a class named Animal that has the following attributes: name and species. It should also have a method
# called speak() that returns a string with the animal's sound.

class Animal:
    def __init__(self, name, species) -> None:
        self.name = name
        self.species = species

    def speak(self, sound):
        return sound
    
pet1 = Animal('snowy', 'cat')
print(pet1.speak('meow'))

#6.Create a base class named Vehicle that has the following attributes: make, model, and year.
# It should also have a method called get_info() that returns a string with the vehicle's make, model, and year.
# Then create two subclasses, Car and Truck, that inherit from Vehicle and add additional attributes and methods
# specific to each type of vehicle.

class Vehicle:
    def __init__(self, make, model, year) -> None:
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return "Vehicle made by " + self.make + " in " + self.year + ", model: " + self.model
    
class Car(Vehicle):
    def __init__(self, make, model, year, seats) -> None:
        self.seats = seats
        super().__init__(make, model, year)

    def get_seats(self):
        return self.seats

class Truck(Vehicle):
    def __init__(self, make, model, year, weight) -> None:
        self.weight = weight
        super().__init__(make, model, year)
    
    def get_weight(self):
        return self.weight

a = Car("audi","80", "1985", "4")
print(a.get_info())
print(a.get_seats())

b = Truck("scania","R560", "2004", "44 t")
print(b.get_info())
print(b.get_weight())
        

#7.Create a base class named Person that has the following attributes: name, age, and address.
# It should also have a method called get_info() that returns a string with the person's name, age, and address.
# Then create two subclasses, Student and Teacher, that inherit from Person and add additional attributes and methods
# specific to each role.
import datetime

class Person:
    def __init__(self, name: str, age: int, address: str) -> None:
        self.name = name
        self.age = age
        self.address = address
    
    def get_info(self):
        return self.name + " is " + str(self.age) + " years old and lives in: " + self.address

class Student(Person):
    def __init__(self, name: str, age: int, address: str, graduate_year: int) -> None:
        self.graduate_year = graduate_year
        super().__init__(name, age, address)

    def years_left_to_study(self):
        today = datetime.date.today()
        current_year = today.year
        return self.graduate_year - current_year

class Teacher(Person):
    def __init__(self, name: str, age: int, address: str, module: str) -> None:
        self.module = module
        super().__init__(name, age, address)

    def get_module(self):
        return self.module

person1 = Student("John", 30, "Vilnius", 2025)
print(person1.years_left_to_study())

person2 = Teacher("Ronald", 56, "Vilnius", "filosophy")
print(person2.get_module())

#For I/O:

#8.Write a Python program that reads a JSON file containing a list of dictionaries, sorts the list by a specific key,
# and writes the sorted list back to the file.

import json

def json_rewriter(key):
    with open("first.json", "r") as f:
        text = json.load(f)
        new_text = sorted(text, key=lambda d: d[key])

    with open("first.json", "w") as out_f:
        out_f.write(str(new_text))

json_rewriter("age")

'''[{
	"name": "Homer",
	"age": "39"
}, {
	"name": "Bart",
	"age": "10"
}]'''
      

#9.Write a Python program that reads a CSV file containing student grades, calculates their average score,
# and writes the average to a new file.

import pandas as pd

df = pd.read_csv(r'student_grades.csv')
print(df)

df['avg_score'] = df.loc[:, ["english","math"]].mean(axis = 1)
print(df)

new_entry = pd.DataFrame()
new_entry= df.drop(["english","math"], axis=1)
new_entry = new_entry.set_index('student')
print(new_entry)

new_entry.to_csv('students_avg.csv')

#10.Write a Python program that reads a CSV file containing student grades and writes a new CSV file with the grades
# sorted by student name.
import csv

students = list()
with open("student_grades.csv", "r") as f:
    all_grades = csv.reader(f, delimiter=',')
    for name in all_grades:
        students.append(name)

new_entry = students[1:]
new_entry.sort(key= lambda student: student[0])
print(new_entry)

with open("sorted_student_grades.csv", "w", newline="") as f:
    writer = csv.writer(f, delimiter=',')
    writer.writerow(students[0])
    writer.writerows(new_entry)