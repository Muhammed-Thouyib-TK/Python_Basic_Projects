# importing library
import random

# creation of lists
let = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
num = ['0','1','2','3','4','5','6','7','8','9']
symb = ["!","@","#","$","%","&","(",")","/","?"]

# to get input from user
letters = int(input("Enter How many letter you need in your password : "))
symbols = int(input("Enter How many symbols you need in your password : "))
numbers = int(input("Enter How many numbers you need in your password : "))

# initialize empty set
password_preview = []

# to random choices from the list
for i in range(1,letters+1):
    dh = random.choice(let)
    password_preview += dh

for j in range(1,symbols+1):
    fg = random.choice(symb)
    password_preview += fg

for k in range(1,numbers+1):
    th = random.choice(num)
    password_preview += th

# to shuffle the list
random.shuffle(password_preview)

# initialize a empty string
password = ""

# to convert list into string 
for n in password_preview:
    password += n

# print the final output
print(password)