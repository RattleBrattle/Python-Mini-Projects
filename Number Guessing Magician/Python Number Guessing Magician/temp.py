# Mini Application #1: Number Guessing Magician
# Description: The Program prompts the Player to enter a number (integer) and the
#              Program Proceeds to guess it by asking a set of questions and trying to
#              zero in on the number and asks the player if it's correct or not.
# Author: Basel M. Mostafa Sayed
# Email: baselmohamed802@gmail.com

print("Hello to the Guessing Game Program!")
print("You are going to enter a random number and the Program will try to guess it by asking a series of questions.")

def get_valid_yes_no_input(prompt):
    """
    Helper function to get a validated 'y' or 'n' input from the user.
    """
    while True:
        user_response = input(prompt).lower()
        if user_response == 'y' or user_response == 'n':
            return user_response
        else:
            print("You did not answer the question correctly. Please answer with 'y' or 'n'.")

while True:
    user_input = input("Enter a Number from -500 to 500 (Enter Q to quit): ")

    if user_input.lower() == 'q':
        print("Goodbye!")
        break

    valid_number = None # Initialize to None
    # Validation loop to ensure user enters no Characters, Only integers and within valid range (-500 to 500)
    while valid_number is None:
        try:
            temp_number = int(user_input)
            if -500 <= temp_number <= 500:
                valid_number = temp_number
                print(f"You entered: {valid_number}")
            else:
                user_input = input("Invalid input, please enter a number between -500 and 500: ")
        except ValueError:
            user_input = input("Not a valid number, please enter an integer: ")

    # Initialize the possible range
    possible_numbers = list(range(-500, 501)) # inclusive of 500

    # Guessing Logic Phase 1: Asking Questions and Filtering
    print("\nAnswer the following questions with (y | n):")

    # Question 1: Is the number positive?
    is_positive_answer = get_valid_yes_no_input("Is the Number positive?: ")
    if is_positive_answer == 'y':
        possible_numbers = [num for num in possible_numbers if num > 0]
    else: # 'n'
        possible_numbers = [num for num in possible_numbers if num <= 0]


    # Question 2: Is the number even?
    is_even_answer = get_valid_yes_no_input("Is the Number even?: ")
    if is_even_answer == 'y':
        possible_numbers = [num for num in possible_numbers if num % 2 == 0]
    else: # 'n'
        possible_numbers = [num for num in possible_numbers if num % 2 != 0]

    # Question 3: Range based on positivity
    if is_positive_answer == 'y':
        is_greater_than_100_answer = get_valid_yes_no_input("Is the Number greater than 100?: ")
        if is_greater_than_100_answer == 'y':
            possible_numbers = [num for num in possible_numbers if num > 100]
        else: # 'n'
            possible_numbers = [num for num in possible_numbers if num <= 100]
    else: # is_positive_answer == 'n' (number is negative or zero)
        is_greater_than_neg_100_answer = get_valid_yes_no_input("Is the Number greater than -100?: ")
        if is_greater_than_neg_100_answer == 'y':
            possible_numbers = [num for num in possible_numbers if num >= -100] # -100 is greater than itself
        else: # 'n'
            possible_numbers = [num for num in possible_numbers if num < -100]

    # Question 4: Is the number a multiple of 5?
    is_multiple_of_five_answer = get_valid_yes_no_input("Is the Number a Multiple of 5?: ")
    if is_multiple_of_five_answer == 'y':
        possible_numbers = [num for num in possible_numbers if num % 5 == 0]
    else: # 'n'
        possible_numbers = [num for num in possible_numbers if num % 5 != 0]

    # Guessing Phase:
    print("\nThinking...")
    if not possible_numbers:
        print("Hmm, I couldn't guess your number based on your answers. It's possible there was a contradiction in your responses!")
    elif len(possible_numbers) == 1:
        print(f"Is your number {possible_numbers[0]}?")
        final_check = get_valid_yes_no_input("Am I correct? (y/n): ")
        if final_check == 'y':
            print("Great! I guessed it!")
        else:
            print("Oh, I see. There might have been a mistake in your answers or my logic. Let's play again!")
    else:
        # If there's more than one possibility, try to make an educated guess
        # For simplicity, let's pick the middle element or a random one.
        # A more advanced Akinator would use more questions or a decision tree.
        # Here, I'll pick the first number in the narrowed down list.
        guessed_number = possible_numbers[0]
        print(f"Is your number {guessed_number}?")
        final_check = get_valid_yes_no_input("Am I correct? (y/n): ")
        if final_check == 'y':
            print("Yay! I guessed it!")
        else:
            print("Darn! My apologies. Let's try again!")
            # You could add more questions here to further narrow down the possibilities.
            # Or inform the user about the remaining possibilities.
            print(f"Numbers I was considering were: {possible_numbers}")

    print("\n--- Starting a new game ---")