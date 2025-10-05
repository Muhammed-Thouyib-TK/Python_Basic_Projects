import string # to get the list of alphabets
letters = list(string.ascii_lowercase)

def encrypt(text,shift): # for encryption
    ot = ''
    for i in text:
        if i in letters:
            position=letters.index(i)
            new_pos = (position+shift)%26 # x+shift %26
            ot += letters[new_pos]
        else:
            ot += i
    print('Encrypted Text is ',ot)

def decrypt(text,shift): # for decryption
     to = ''
     for j in text:
          if j in letters:
            pos = letters.index(j)
            npos = (pos-shift)%26
            to += letters[npos]
          else:
              to += j
     print('Decrypted Text is ',to)

end = False
while not end: # to recive user input and cross check it
    choice = input('Enter \'encrypt\' to Encrypt and Enter \'decrypt\' to Decrypt :').lower()
    text = input('Enter Your Text :').lower()
    shift = int(input('Enter Your Shift Number :')) 
    if choice == 'encrypt':
        encrypt(text,shift)
    elif choice == 'decrypt':
        decrypt(text,shift)
    else:
        print('Enter a valid one Choice!')
    play_again = input('Do You want to play again?[Y/N]').lower()
    if play_again == 'n':
        end=True
        print('Have a Nice Day...Bye')