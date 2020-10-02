from random import randint
import sys

active = True

def play_message():
    message = input('Would you like to play guess the number? (y/n) ')
    if message == 'y':
        number_game()
    elif message == 'n':
        print('Please come back again!')
        sys.exit()
    else:
        print('Could not render request, goodbye.')
        sys.exit()

def play_again():
    message = input('Would you like to play again? (y/n) ')
    if message == 'y':
        number_game()
    elif message == 'n':
        print('Thanks for playing!')
        sys.exit()
    else: 
        print('Could not render request, goodbye.')
        sys.exit() 

def number_game():
    turn = 0
    random_number = randint(1, 21)

    while active:
        user_guess = int(input('Please pick a number between 1 and 20: '))

        if turn < 4:
            if user_guess == random_number:
                print('You are correct!')  
                play_again()
            elif user_guess < random_number:
                print('Too low, guess again.')
                turn += 1
                print(f'Turns remaining: {5 - turn}')
                print(user_guess)
            elif user_guess > random_number:
                print('Too high, guess again.')
                turn += 1
                print(f'Turns remaining: {5 - turn}')
                print(user_guess)    
        else: 
            print('Sorry, you have lost!')
            play_again()

play_message()
number_game()


