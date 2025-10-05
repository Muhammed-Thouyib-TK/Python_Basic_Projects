# import module

import random

# random number generation

def random_generator():
    actual = random.randint(1,50)
    return actual

# code for hard level

def hard():
    num = random_generator()

    for i in range (5,0,-1):
        print(f'You have {i} attempts remaining to guess the number!')
        guess = int(input('Make a guess : '))

        if guess == num:
            print('Your guess is Correct...Hurray!')
            break
        elif guess > num:
            print('Your Guess is too High!')
        elif guess < num:
            print('Your Guess is too Low!')
    else:
        print('Better Luck Next Time')

# code for easy level

def easy():
    num = random_generator()

    for i in range (10,0,-1):
        print(f'You have {i} attempts remaining to guess the number!')
        guess = int(input('Make a guess : '))

        if guess == num:
            print('Your guess is Correct...Hurray!')
            break
        elif guess > num:
            print('Your Guess is too High!')
        elif guess < num:
            print('Your Guess is too Low!')
    else:
        print('Better Luck Next Time')

# main

def main():


    print('''  ▄████  █    ██ ▓█████   ██████   ██████    ▄▄▄█████▓ ██░ ██ ▓█████     ███▄    █  █    ██  ███▄ ▄███▓ ▄▄▄▄   ▓█████  ██▀███  
 ██▒ ▀█▒ ██  ▓██▒▓█   ▀ ▒██    ▒ ▒██    ▒    ▓  ██▒ ▓▒▓██░ ██▒▓█   ▀     ██ ▀█   █  ██  ▓██▒▓██▒▀█▀ ██▒▓█████▄ ▓█   ▀ ▓██ ▒ ██▒
▒██░▄▄▄░▓██  ▒██░▒███   ░ ▓██▄   ░ ▓██▄      ▒ ▓██░ ▒░▒██▀▀██░▒███      ▓██  ▀█ ██▒▓██  ▒██░▓██    ▓██░▒██▒ ▄██▒███   ▓██ ░▄█ ▒
░▓█  ██▓▓▓█  ░██░▒▓█  ▄   ▒   ██▒  ▒   ██▒   ░ ▓██▓ ░ ░▓█ ░██ ▒▓█  ▄    ▓██▒  ▐▌██▒▓▓█  ░██░▒██    ▒██ ▒██░█▀  ▒▓█  ▄ ▒██▀▀█▄  
░▒▓███▀▒▒▒█████▓ ░▒████▒▒██████▒▒▒██████▒▒     ▒██▒ ░ ░▓█▒░██▓░▒████▒   ▒██░   ▓██░▒▒█████▓ ▒██▒   ░██▒░▓█  ▀█▓░▒████▒░██▓ ▒██▒
 ░▒   ▒ ░▒▓▒ ▒ ▒ ░░ ▒░ ░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░     ▒ ░░    ▒ ░░▒░▒░░ ▒░ ░   ░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ░ ▒░   ░  ░░▒▓███▀▒░░ ▒░ ░░ ▒▓ ░▒▓░
  ░   ░ ░░▒░ ░ ░  ░ ░  ░░ ░▒  ░ ░░ ░▒  ░ ░       ░     ▒ ░▒░ ░ ░ ░  ░   ░ ░░   ░ ▒░░░▒░ ░ ░ ░  ░      ░▒░▒   ░  ░ ░  ░  ░▒ ░ ▒░
░ ░   ░  ░░░ ░ ░    ░   ░  ░  ░  ░  ░  ░       ░       ░  ░░ ░   ░         ░   ░ ░  ░░░ ░ ░ ░      ░    ░    ░    ░     ░░   ░ 
      ░    ░        ░  ░      ░        ░               ░  ░  ░   ░  ░            ░    ░            ░    ░         ░  ░   ░     
                                                                                                             ░                 ''')
    
    print('Let me think of a number between 1 to 50.')
    choice = input('Choose Level of Difficulty - Type[  easy  ,  hard  ] : ').lower()

    if choice == 'easy':
        easy()
    elif choice == 'hard':
        hard()
    else:
        print("Invalid Input!")
main()