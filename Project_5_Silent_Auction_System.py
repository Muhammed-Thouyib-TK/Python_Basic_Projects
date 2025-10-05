import os

details = {}

def details_adder():  # to add user details 
    print('='*10,'WELCOME TO THE AUCTION','='*10)
    name = input("Enter Your Name: ")
    bid = int(input("Enter Your Bid Amount : "))
    details[name] = bid


def main(): # to make the aution silent and print the output
    while True:
        details_adder()
        choice = input("Any Other Person to Bid [Yes/No]: ").lower()

        if choice == 'yes':
            os.system('cls')
        elif choice == 'no':
            os.system('cls')
            break
    result = ''
    max = 0
    for key,value in details.items():
        if value>max:
            max=value
            result = key

    print(f'The Winner is {result} and The Bid is {max}')
main()