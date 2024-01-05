import random


def start_game():
    winning_number = random.randrange(1,10)
    guess = 0
    attempts = 1
    high_score = 8
    
    print("\nWelcome To The Number Guessing Game!")
    print("\nCurrent High Score is:", high_score)
    
    

    while guess != winning_number:
        try:
            guess = int(input("\nEnter a number: "))
            #keeps the games guesses in range of 1-10
            
            #Extra credit number 3 handle numbers out of range.
            if guess < 1 or guess >10:
                raise Exception("\nSorry the number you picked is outside of game play. Please only choose a number from 1-10. Try again!")


        except ValueError:
            print("\nSorry that entry is an invalid choice. Please choose a number between (1-10).")
            
        except Exception as invalid_literal:
            print(invalid_literal)
            
        else:
            if guess > winning_number:
                attempts += 1
                print("\nA bit too high for my taste try a lower number?")
                
            elif guess < winning_number:
                attempts += 1
                print("\nNot quite there, try a higher number?")
    else:
        if guess == winning_number:
            print("\nYou got it! The number was {}. It took you {} attempts. Nicely done!".format(winning_number, attempts))
            if attempts < high_score:
                high_score = attempts
                print("\nCongratulations! New High Score: {}".format(high_score))
            else:
                print("\nCurrent High score is: {}! can you beat it?".format(high_score))
            
            
            #retry menu for when game ends and ask the player to play again or end the game.
        while True:
            retry = input("\nWould you like to try again?  (Y)es / (N)o   ")
            if retry.lower() != "y" and retry.lower() != "n":
                print("\nPlease enter only Y or N.")
                
            elif retry.lower() == "y":
                print("\nGame is restarting!")
                return start_game()
            
            else:
                print("\nThanks for playing, please come again!")
                quit()  

start_game()
