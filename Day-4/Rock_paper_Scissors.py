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
choices=[rock,paper,scissors]
p_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n>>>"))
player=choices[p_choice]
print(f"You Chose : \n{player}")
c_choice=random.choice([0,1,2])
# print(c_choice)
comp=choices[c_choice]
print(f"Computer chose : \n{comp}")
if (c_choice ==0 and p_choice==1) or (c_choice == 1 and p_choice == 2) or (c_choice==2 and p_choice==0):
    print("You Win.")
elif c_choice==p_choice:
    print("It's a draw.")
else:
    print("You Lose.")