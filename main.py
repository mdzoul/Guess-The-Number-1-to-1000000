from number import Number
from hint import Hint


game_is_on = True
while game_is_on:
    num = Number()
    num.get_digit(int(num))
    hint = Hint()

    num_of_guesses = 0
    
    print("Welcome to Guess The Number Game!\n")
    print("I am thinking of a number between 1 and 1,000,000.\n")
        
    is_correct = False
    while not is_correct:        
        if num_of_guesses == 3:
            hint.hint1()

        if num_of_guesses == 7:
            hint.hint2()

        if num_of_guesses == 11:
            hint.hint3()

        if num_of_guesses == 15:
            hint.hint4()             

            
        user_guess = input("What is your guess? ")
        if int(user_guess) < int(num):
            print("Too low\n")
            num_of_guesses += 1
        elif int(user_guess) > int(num):
            print("Too high\n")
            num_of_guesses += 1
        elif int(user_guess) == int(num):
            print("Correct!\n")
            num_of_guesses += 1
            is_correct = True


    print(f"It took you {num_of_guesses} guesses to get the random number correctly!\n")
    
    continue_game = input("Would you like to play again? Y/N\n").lower()
    if continue_game == "y":
        is_correct = False
    elif continue_game == "n":
        game_is_on = False
        print("Thank you for playing!")