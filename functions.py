#Task 1: Write a function that takes two parameters (a and b) and returns their sum.
def summation(a, b):
    result = a + b
    print(result)

summation(2, 3)

#Task 2:Write a function that takes a string as a parameter and returns the number of vowels (aeiou) in the string.
# Hint: you can use given_character in "aeiou"
def vowels_amount(text:str):
    counter = 0
    given_character = ['a', 'e', 'i', 'o', 'u']
    for i in text.lower():
        if i in given_character:
            counter += 1
    print("Number of vowels in the given string is: ", counter)

vowels_amount('Write a function that takes a string as a parameter and returns the number of vowels (aeiou) in the string')

#Task 3:Write a function that takes a string as a parameter and returns True if the string is a palindrome and False otherwise
def is_palindrome(word:str):
    reverse = word[::-1]
    if word == reverse:
        return True
    else:
        return False

is_palindrome('kayak')

#Task 4:Write a function that takes a list of integers as a parameter and returns a list of only the even integers in the original list
def leave_even_numbs(my_list:list):
    even_numbs = []
    for i in my_list:
        if i % 2 == 0:
            even_numbs.append(i)
    print(even_numbs)

leave_even_numbs([1,2,2,3,4,5,6])

#Task 5:Write a function that takes a list of integers and a target sum as parameters and returns a list of two
# integers from the original list that add up to the target sum.
def find_sum(my_list:list, target:int) -> list:
    length = len(my_list)
    for i in range(length - 1):
        for j in range(i + 1, length):
            if my_list[i] + my_list[j] == target:
                    new_list = i, j
                    print(list(new_list))

find_sum([1,2,2,3,4,5,6], 10)

#Task 6: Write a function that takes a list of integers as a parameter and returns the product of all the integers in the list.
def multiplication(my_list:list):
    numb = 1
    for i in my_list:
        numb = numb * i
    print(numb)

multiplication([1,2,2,3,3])

#Task 8:Write a function that takes a dictionary as a parameter and returns a list of all the keys in the dictionary
# that have an even value.
def even_key(my_dict:dict) -> list:
    my_list = []
    for i in my_dict.keys():
        if i % 2 == 0:
            my_list.append(i)
    print(my_list)

even_key({1: "One", 2: "Two", 3: "Three", 4:"four"})

#Task 9:Write a function that takes a list of dictionaries as a parameter and returns a new dictionary that contains
# the sum of the values for each key in the original dictionaries.
def values_sum(my_list:list) -> dict:
    my_dict = {}
    for dicts in my_list:
        for k, v in dicts.items():
            if k in  my_dict.keys():
                my_dict[k] += v
            else:
                my_dict[k] = v
    print(my_dict)

values_sum([{'a':5, 'b':10, 'c':90},
            {'a':45, 'b':78, 'd': 15},
            {'a':90, 'c':10}])

#Task 10:Write a function that takes a tuple as a parameter and returns a new tuple that has the first and last elements swapped.
def swapped_elements(my_tuple:tuple):
    my_list = list(my_tuple)
    my_list[0], my_list[-1] = my_list[-1], my_list[0]
    new_tuple = tuple(my_list)
    print(new_tuple)

swapped_elements(('Ben', 'Jim', 'Tom', 'Zack'))

#Task 11:Write a function that takes a set as a parameter and returns a new set that contains only the elements
# that are not divisible by 3.
def not_divisible_3(my_set:set):
    my_list = list(my_set)
    new_set = set()
    for i in my_list:
        if i % 3 != 0:
            new_set.add(i)
    print(new_set)

not_divisible_3({4,2,6,3,0,10,34})