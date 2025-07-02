# Mini Application #1: Number Guessing Magician
# Description: The Program prompts the Player to enter a number (integer) and the
#              Program Proceeds to guess it by asking a set of questions and trying to
#              zero in on the number and asks the player if it's correct or not.
# Author: Basel M. Mostafa Sayed
# Email: baselmohamed802@gmail.com


from statistics import correlation


print("Hello to the Guessing Game Program!")
print("You are going to enter a random number and the Program will try to guess it by asking a series of questions.")

while True:
    userInput = input("Enter a Number from -500 to 500 (Enter Q to quit): ")

    if userInput.lower() == 'q':
        print("Goodbye!")
        break

    # Validation loop to ensure user enters no Characters, Only integers and within valid range (-500 to 500)
    while True:
        try:
            validNumber = int(userInput)
            if -500 <= validNumber <= 500:
                print(f"You entered: {validNumber}")
                break  # Exit validation loop
            else:
                userInput = input("Invalid input, please enter a number between -500 and 500: ")
        except ValueError:
            userInput = input("Not a valid number, please enter an integer: ")

    # Guessing Logic Phase 1: Asking Questions
    print("Answer the following questions with (y | n):")
    correctInput, correctInput2 = 0, 0
    correctInput3, correctInput4 = 0, 0
    correctInput5 = 0

    while correctInput == 0:
        isPositive = input("Is the Number a positive?: ")

        if isPositive.lower() == 'y':
            correctInput = 1 # Disable validation loop
        elif isPositive.lower() == 'n':
            correctInput = 1 # Disable validation loop
        else:
            print("You did not answer the question correctly, Please try again....")
            correctInput = 0 #Incorrect Answer, Retry
    while correctInput2 == 0:
        isEven = input("Is the Number even?: ")

        if isEven.lower() == 'y':
            correctInput2 = 1 # Disable validation loop
        elif isEven.lower() == 'n':
            correctInput2 = 1 # Disable validation loop
        else:
            print("You did not answer the question correctly, Please try again....")
            correctInput2 = 0 #Incorrect Answer, Retry

    # if and elif for if the number greater than 100 or greater than -100.
    if isPositive == 'y':
        while correctInput3 == 0:
            isGreaterThan100 = input("Is the Number greater than 100?: ")

            if isGreaterThan100.lower() == 'y':
                correctInput3 = 1 # Disable validation loop
            elif isGreaterThan100.lower() == 'n':
                correctInput3 = 1 # Disable validation loop
            else:
                print("You did not answer the question correctly, Please try again....")
                correctInput3 = 0 #Incorrect Answer, Retry
    elif isPositive == 'n':
        while correctInput3 == 0:
            isGreaterThanNeg100 = input("Is the Number greater than -100?: ")
            
            if isGreaterThanNeg100.lower() == 'y':
                correctInput3 = 1 # Disable validation loop
            elif isGreaterThanNeg100.lower() == 'n':
                correctInput3 = 1 # Disable validation loop
            else:
                print("You did not answer the question correctly, Please try again....")
                correctInput3 = 0 #Incorrect Answer, Retry

    while correctInput4 == 0:
        isMultipleOfFive = input("Is the Number a Multiple of 5?: ")

        if isMultipleOfFive.lower() == 'y':
            correctInput4 = 1 # Disable validation loop
        elif isMultipleOfFive.lower() == 'n':
            correctInput4 = 1 # Disable validation loop
        else:
            print("You did not answer the question correctly, Please try again....")
            correctInput4 = 0 #Incorrect Answer, Retry

    break  # Remove this later when guessing logic is added
