cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

import random
total_user = 0
total_computer = 0
user_cards = []
computer_cards = []
random_user_card = 0
random_computer_card = 0

def show():
    print("Your cards are :")
    print(user_cards)

    # print("The computer cards are : ")
    # print(computer_cards)

def show_both():
    print("Your cards are :")
    print(user_cards)

    print("The computer cards are : ")
    print(computer_cards)
        

choice = 'y'
random_user_card = random.choice(cards)
user_cards.append(random_user_card)
    
random_computer_card = random.choice(cards)
computer_cards.append(random_computer_card)

total_user += int(random_user_card)
total_computer += int(random_computer_card) 

show()
while choice == 'y':
    
    choice = input("Do you want to pick another card ?? 'y' or 'n' \n")
    if choice == 'y':
        random_user_card = random.choice(cards)
        user_cards.append(random_user_card)
    
        random_computer_card = random.choice(cards)
        computer_cards.append(random_computer_card)


        total_user += int(random_user_card)
        total_computer += int(random_computer_card) 

        show()

        if total_user > 21:
            print("You exceeded 21. You loose\n")
            show_both()  
            exit()

        if total_computer > 21:
            print("Computer exceeded 21. You win\n")
            show_both()  
            exit()

        if total_user == 21:
            print("You hit the BlackJack !! You win\n")
            show_both()  
            exit()

        if total_computer == 21:
            print("Computer Wins !\n")
            show_both()  
            exit()
            
               
    else:
        if total_user == total_computer:
            print("Game Draw\n")

        elif 21 - total_user < 21 - total_computer:
            print("You win \n")   
                 
        elif 21 - total_user > 21 - total_computer: 
            print("Computer wins \n")

        show_both()  
        exit()     
                

    
    

