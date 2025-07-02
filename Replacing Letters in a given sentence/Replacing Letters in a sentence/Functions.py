"""
Author: Basel M. Mostafa Sayed
Email: baselmohamed802@gmail.com
Description: Functions file for Replacing letters program
"""

from ast import Str

def get_valid_letter_input(prompt):
    while True:
        user_input = input(prompt)
        # Check if the input is 1 character and not an integer
        if len(user_input) == 1 and user_input.isalpha():
            return user_input
        else:
            print("Invalid input. Please enter a single letter.")

def get_valid_word_input(prompt):
    while True:
        user_input = input(prompt)
        # Check if the input contains only alphabetic characters and is not empty
        if user_input.strip() and all(char.isalpha() or char.isspace() for char in user_input.strip()):
            return user_input.strip()
        else:
            print("Invalid input. Please enter one or more words containing only letters.")

def get_valid_number_input(prompt):
    while True:
        # Check if the number entered is not a char 
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def start_up():
    name = input("Enter your name: ")
    print(f"Hello {name}")
    print("This Program will ask you to enter any line string you want, then prompt you which letter to change and replace it with.")

    return None

def switch_letters(input_str, letter_to_change, letter_to_replace_it):
    new_string = ""
    for char in input_str:
        if char == letter_to_change:
            new_string += letter_to_replace_it
        else:
            new_string += char

    return new_string

def switch_letter_number(input_str, letter_to_change, number_to_replace_it):
    new_string = ""
    for char in input_str:
        if char == letter_to_change:
            new_string += str(number_to_replace_it)
        else:
            new_string += char

    return new_string

def switch_words(input_str, word_to_change, word_to_replace):
    words = input_str.split()
    new_words = []

    for word in words:
        if word == word_to_change:
            new_words.append(word_to_replace)
        else:
            new_words.append(word)

    return ' '.join(new_words)