#1)Ask the user to enter the text and a letter. Count how many occurrences of the letter provided.

text = input('enter the text: ')
letter = input('what letter are you looking for?: ')
result = text.count(letter)
print(result)

#1.1) Based on the task 1, count the occurrences of each character in the text provided and display them in the output

my_set = set(text)
for char in my_set:
    numb = text.count(char)
    print("character '{}' in the text is: {}".format(char, numb))

#2)Write the program to sort the list (without using sort function). You can implement any algorithm

my_list = list(input('enter a list: '))
# 987654321

for i in range(len(my_list)):
    for j in range(i + 1, len(my_list)):
        if my_list[i] > my_list[j]:
            my_list[i], my_list[j] = my_list[j], my_list[i]
print(my_list)