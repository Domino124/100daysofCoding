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
images = [rock, paper, scissors]

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
print("Player:")
if player > 2 or player < 0:
  print("It's a valid number")
else:
  print(images[player])

#if player == 0:
  #print(rock)
#elif player == 1:
  #print(paper)
#elif player == 2:
  #print(scissors)
#else:
  #print("It's a valid number")

import random
computer = random.randint(0,2)
print("Computer:")
print(images[computer])
#if computer == 0:
  #print(rock)
#elif computer == 1:
  #print(paper)
#else:
  #print(scissors)

if player == 0 and computer == 2:
  print("You win")
elif player == 2 and computer == 1:
  print("You win")
elif player == 1 and computer == 0:
  print("You win")
elif player == computer:
  print("Play again")
elif player > 2 or player < 0:
  print("You lose")
else:
  print("You lose")