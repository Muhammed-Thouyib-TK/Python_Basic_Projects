import random
import hangman_stages
import hangman_words

print("Hello Welcome , Let's Play Hagman Game")
print("You have 6 attempt , You need to find the word before that")

word = random.choice(hangman_words.simple_words)
length = len(word)
print(word)

life = 6

list = []
for i in range(length):
    list.append('_')
print(list)

d = '_'

game = False

while not game :
    user_input = input("Enter your letter : ").lower()
    if user_input > user_input[0]:
       print("Enter a Single letter :")
    else:
        for i in range(length):
            if user_input == word[i]:
                list[i] = word[i]
                print(list)
        if d not in list:
            print('You won')
            game = True
        elif user_input not in word:
            life -= 1
            print("Remaining life : ",life)
            print(hangman_stages.stages[6-life])
        if life == 0:
            print("Game Over")
            game = True
    