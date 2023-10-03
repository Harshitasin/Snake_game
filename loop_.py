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

user_ip=int(input("Enter 0 for choosing rock 1 for paper and 2 for scissors \n"))
if user_ip==0:
    print("You choose\n\n",rock)
elif user_ip==1:
    print("You choose\n\n", paper)
elif user_ip==2:
    print("You choose\n\n", scissors)
else:
    print("Enter valid input")
comp_ip=random.randint(0,2)
if comp_ip==0:
    print("Computer choose\n\n",rock)
elif comp_ip==1:
    print("Computer choose\n\n", paper)
elif comp_ip==2:
    print("Computer choose\n\n", scissors)
else:
    print("Enter valid input")
if user_ip==0 and comp_ip==1:
    print("You loose")
elif user_ip==0 and comp_ip==2:
    print("You win")
elif user_ip==1 and comp_ip==0:
    print("You win")
elif user_ip==1 and comp_ip==2:
    print("You lose")
elif user_ip==2 and comp_ip==0:
    print("You lose")
elif user_ip==2 and comp_ip==1:
    print("You win")
elif user_ip==comp_ip:
    print("Match draw")
