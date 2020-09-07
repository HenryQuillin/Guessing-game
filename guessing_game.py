# This is a guess the number game.
import random

print('Hello. What is your name?')
name = input()

print(f'Well, {name}, I am thinking of a number between 1 and 20')
secretNumber = random.randint(1,20)


for trys in range(1,7):
    guess = int(input('Make a guess: '))
    if guess == secretNumber:
        print(f'Good job {name}, You got it right!')
        break
    elif guess > secretNumber:
        print(f'Sorry {name}. Your guess to too high :(')
    else:
        print(f'Think bigger {name}.')


if guess == secretNumber:
    print(f'You took {str(trys)} guesses.')
else:
    print(f'Nope. The number I was thinking of was {str(secretNumber)}.')

