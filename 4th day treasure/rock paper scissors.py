import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

image = [rock, paper, scissors]
user = int(input("User what do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors! "))
if user >=3 or user < 0:
    print("You typed an invalid number and you lose")
else:
    print(image[user])
computer = random.randint(0, 2)
print("Computer choice: ")
print(image[computer])
if user == 0 and computer == 2:
    print("You win")
elif computer == 0 and user == 2:
    print("You lose ")
elif user == 0 and computer == 1:
    print("You lose")
elif computer == 0 and user == 1:
    print("You win")
elif user == 1 and computer == 2:
    print("You lose")
elif computer == 1 and user == 2:
    print("You win")
elif computer == 0 and user == 0:
    print ("It is a draw! ")
elif computer == 1 and user == 1:
    print ("It is a draw! ")
elif computer == 2 and user == 2:
    print ("It is a draw! ")



















