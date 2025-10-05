import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""
scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


print(f"0 == ROCK\n1 == PAPER\n2 == SCISSOR")
choice = int(input("Enter your Choice [0/1/2] : "))

num = random.randint(0,2)
print(num)

image = [rock,paper,scissor]

if choice > 2 or choice < 0:
    print("Invalid Number")
else :
    print(image[choice])
    if choice == 0 and num == 2:
        print(f"Computer Choose :\n{image[num]}")
        print("You Win")
    elif choice == 2 and num == 0:
        print(f"Computer Choose :\n{image[num]}")
        print("You Lose")
    elif choice > num:
        print(f"Computer Choose :\n{image[num]}")
        print("You Win")
    elif choice < num:
        print(f"Computer Choose :\n{image[num]}")
        print("You Lose")
    elif choice == num:
        print(f"Computer Choose :\n{image[num]}")
        print("Draw")
