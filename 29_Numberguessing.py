import random
choice = input("Welcome to the number guessing game.. Choose either 'easy' or 'hard' : ")

def easy_choice():
    attempts=10
    print(f"Im thinking of a number from 1 to 100 \n You have {attempts} chances left.")
    random_number=random.randint(1,100)
    for i in range(0,10):
        attempts-=1
        user_number = int(input("Make your guess : "))

        if user_number == random_number:
            print(f"You got the number !! It was {random_number}")
            exit()
        elif user_number > random_number:
            print("Your guess is higher than the number")
            print(f"You have {attempts} attempts left")
        elif user_number < random_number:
            print("Your guess is lower than the number") 
            print(f"You have {attempts} attempts left")

        if attempts == 0:
            print(f"The number was {random_number}")

def hard_choice():
    attempts=5
    print(f"Im thinking of a number from 1 to 100 \n You have {attempts} chances left.")
    random_number=random.randint(1,100)
    for i in range(0,5):
        attempts-=1
        user_number = int(input("Make your guess : "))

        if user_number == random_number:
            print(f"You got the number !! It was {random_number}")
        elif user_number > random_number:
            print("Your guess is higher than the number")
            print(f"You have {attempts} attempts left")
        elif user_number < random_number:
            print("Your guess is lower than the number")  
            print(f"You have {attempts} attempts left")  

        if attempts == 0:
            print(f"The number was {random_number}")
             

if choice == 'easy':
    easy_choice()

elif choice == 'hard':
    hard_choice()

else:
    print("Please enter a correct option")        
