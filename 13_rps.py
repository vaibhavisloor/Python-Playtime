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
import random 
outcomes = [rock, paper, scissors]
outcome_name = ["Rock","Paper","Scissors"]
while True:
    user_choice = int(input('''Choose your option : \n0 - Rock 
                                                    1 - Paper 
                                                    2 - Scissors \n
                                                    3 - Exit\n'''))

    comp_choice = random.randint(0,2)

    if(user_choice == 3):
        print("Hope you enjoyed playing !!")
        exit()
    else:   
        print(f"You chose {outcome_name[user_choice]} {outcomes[user_choice]}\nComputer chose {outcome_name[comp_choice]}{outcomes[comp_choice]}\n") 
        if (user_choice == comp_choice):
            print("\nIts a Draw")
        else:
            if((user_choice == 0 and comp_choice == 2) or (user_choice == 1 and comp_choice == 0) or (user_choice == 2 and comp_choice == 1)):   
                print("You win !!") 
            else:
                print("\nYou Lost :(\n\n")
