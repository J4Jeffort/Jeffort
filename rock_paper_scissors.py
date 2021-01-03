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
game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))


if user_choice >= 3:
    print("invalid number. you lost ")
else:
    print("You chose:")
    print(game_images[user_choice])
    cpu_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[cpu_choice])

    if user_choice == cpu_choice:
        print("You tied!")
    else:
        if user_choice == 0 and cpu_choice == 2:
        	print("You win!")
        elif cpu_choice == 0 and user_choice ==2:
            print("You Lose!")
        elif cpu_choice > user_choice:
            print("You Lose!")
        elif cpu_choice < user_choice:
            print("You win!")
