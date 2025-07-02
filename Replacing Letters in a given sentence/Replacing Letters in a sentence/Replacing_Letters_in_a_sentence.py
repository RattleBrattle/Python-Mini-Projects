"""
Author: Basel M. Mostafa Sayed
Email: baselmohamed802@gmail.com
Description: Simple program that takes string input from user,asks the user which letter(s) do
             they want to change and which to replace it with.
"""

# importing functions folder
from Functions import *

start_up()

# Taking string input from user
string_user = input("Enter string you want: ")

# print(f"{string_user}") # debug!!! delete later or comment out

# Menu to choose the operation to be performed
print("1) Change one letter with one letter.")
print("2) Change one word with another.")
print("3) Change one letter with a number.")
operation = int(input("Choose which operation to perform: "))

# Switch case to perform the requested operation and call the functions
def switch(operation):
    match operation:
        case 1:
            letter_to_change = get_valid_letter_input("Enter the Letter you want to change in the sentence: ")
            letter_to_replace = get_valid_letter_input("Enter the Letter you want to replace it with: ")
            new_string = switch_letters(string_user, letter_to_change, letter_to_replace)
            return new_string
        case 2:
            word_to_change = get_valid_word_input("Enter the Word you want to change in the sentence: ")
            word_to_replace = get_valid_word_input("Enter the Word to replace the word given with: ")
            new_string = switch_words(string_user, word_to_change, word_to_replace)
            return new_string
        case 3:
            letter_to_change = get_valid_letter_input("Enter the Letter you want to change in the sentence: ")
            number_to_replace = get_valid_number_input("Enter the number to replace the letter with: ")
            new_string = switch_letter_number(string_user, letter_to_change, number_to_replace)
            return new_string


# Printing out the final output:
print(switch(operation))