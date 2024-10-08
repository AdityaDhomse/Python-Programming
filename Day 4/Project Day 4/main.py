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

images = [rock, paper, scissors]

print("What do you choose? Type: \n0 for Rock\n1 for Paper\n2 for Scissors")
user_choice = int(input())
   
if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!")
else: 
    print("You choose: " + images[user_choice])
    
computer_choice = random.randint(0, 2)

print("\nComputer choose:" + images[computer_choice])

if user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")