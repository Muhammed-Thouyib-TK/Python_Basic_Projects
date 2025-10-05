# import modules

import random
import os

# database

footballers = [
    {'name': 'Cristiano Ronaldo', 'profession': 'Footballer', 'country': 'Portugal', 'followers': 639000000},
    {'name': 'Lionel Messi', 'profession': 'Footballer', 'country': 'Argentina', 'followers': 507000000},
    {'name': 'Neymar Jr', 'profession': 'Footballer', 'country': 'Brazil', 'followers': 231000000},
    {'name': 'Kylian Mbappé', 'profession': 'Footballer', 'country': 'France', 'followers': 124000000},
    {'name': 'David Beckham', 'profession': 'Footballer (Retired)', 'country': 'England', 'followers': 88000000},
    {'name': 'Ronaldinho', 'profession': 'Footballer (Retired)', 'country': 'Brazil', 'followers': 77000000},
    {'name': 'Karim Benzema', 'profession': 'Footballer', 'country': 'France', 'followers': 76000000},
    {'name': 'Mohamed Salah', 'profession': 'Footballer', 'country': 'Egypt', 'followers': 66000000},
    {'name': 'Sergio Ramos', 'profession': 'Footballer', 'country': 'Spain', 'followers': 65000000},
    {'name': 'Paulo Dybala', 'profession': 'Footballer', 'country': 'Argentina', 'followers': 58000000},
    {'name': 'Zlatan Ibrahimović', 'profession': 'Footballer (Retired)', 'country': 'Sweden', 'followers': 65000000},
    {'name': 'Marcelo Vieira', 'profession': 'Footballer', 'country': 'Brazil', 'followers': 65000000},
    {'name': 'Gareth Bale', 'profession': 'Footballer (Retired)', 'country': 'Wales', 'followers': 53000000},
    {'name': 'James Rodríguez', 'profession': 'Footballer', 'country': 'Colombia', 'followers': 52000000},
    {'name': 'Antoine Griezmann', 'profession': 'Footballer', 'country': 'France', 'followers': 42000000},
    {'name': 'Luis Suárez', 'profession': 'Footballer', 'country': 'Uruguay', 'followers': 48000000},
    {'name': 'Mesut Özil', 'profession': 'Footballer (Retired)', 'country': 'Germany', 'followers': 28000000},
    {'name': 'Andrés Iniesta', 'profession': 'Footballer (Retired)', 'country': 'Spain', 'followers': 42000000},
    {'name': 'Vinícius Jr', 'profession': 'Footballer', 'country': 'Brazil', 'followers': 50000000},
    {'name': 'Erling Haaland', 'profession': 'Footballer', 'country': 'Norway', 'followers': 41000000}
]

# logo

def logo():
        print('''
██   ██ ██  ██████  ██   ██ ███████ ██████          
██   ██ ██ ██       ██   ██ ██      ██   ██         
███████ ██ ██   ███ ███████ █████   ██████          
██   ██ ██ ██    ██ ██   ██ ██      ██   ██         
██   ██ ██  ██████  ██   ██ ███████ ██   ██         
                                                    
                                                    
██       ██████  ██     ██ ███████ ██████           
██      ██    ██ ██     ██ ██      ██   ██          
██      ██    ██ ██  █  ██ █████   ██████           
██      ██    ██ ██ ███ ██ ██      ██   ██          
███████  ██████   ███ ███  ███████ ██   ██          
                                                    
                                                    
 ██████   █████  ███    ███ ███████                 
██       ██   ██ ████  ████ ██                      
██   ███ ███████ ██ ████ ██ █████                   
██    ██ ██   ██ ██  ██  ██ ██                      
 ██████  ██   ██ ██      ██ ███████                 
                                                    
                                                    
          ''')

# random choice generator

def random_picker(footballers):
    choice_1,choice_2 = random.sample(footballers,2)
    return choice_1,choice_2

# to display the random choices

def display_choice(c1,c2):
        return f'Option 1 : {c1['name']}, a {c1['profession']}, from {c1['country']} \n\nV/S \n\nOption 2 : {c2['name']}, a {c2['profession']}, from {c2['country']}'

# to make comparison

def comparison(c1,c2):

     if c1['followers'] > c2['followers']:
          return 1
     elif  c1['followers'] < c2['followers']:
          return 2

# main

def main():
     score = 0
     c1 , c2 = random_picker(footballers)
     while True:
        logo() 
        print(display_choice(c1,c2))
        choice = int(input("Who Have More Followers ? [1/2] : "))

        compa = comparison(c1,c2)

        if choice == compa:
            score += 1
            os.system('cls')
            print(f'Score : {score}')
            

            if compa == 1: # to make the correct one as 1 and avoid repeataion of the same 
                 c1, _ = c1,c2 
            else:
                 c1, _ = c2,c1
            c2 = random.choice(footballers)
            while c2 == c1:
                 c2 = random.choice(footballers)
        else:
            print(f'You are Wrong....Your Final Score is {score}')
            break
main()
     