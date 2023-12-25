print(''' _                                   
| |_  ___  _ _  ___  _ _ _  ___  _ _ 
| . |[_] || ' |/ . || ' ' |[_] || ' |
|_|_|[___||_|_|\_. ||_|_|_|[___||_|_|
               [___|                 
''')
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

import random

def show():
    for i in range(0,word_length):
        print(blanks[i]+" ",end="")

import os

def clear_terminal():
    if os.name == 'posix':  # For Unix/Linux/MacOS
        os.system('clear')
    elif os.name == 'nt':  # For Windows
        os.system('cls')



animals = [
    "lion", "bear", "deer", "frog", "duck", "bird", "seal", "goat", "orca", "lynx",
    "horse", "zebra", "shark", "eagle", "snake", "tiger", "whale", "koala", "zebu", "gecko",
    "mouse", "sheep", "chimp", "giraffe", "lizard", "panda", "penguin", "monkey", "donkey", "hippo",
    "otter", "skunk", "jaguar", "turkey", "gibbon", "walrus", "rhino", "beaver", "bobcat", "falcon",
    "gazelle", "parrot", "hyena", "sloth", "lemur", "rabbit", "puffer", "badger", "cougar", "flamingo"
]

things = [
    "book", "desk", "lamp", "vase", "fork", "ring", "soap", "coin", "shoe", "pen",
    "chair", "table", "clock", "brush", "glove", "plant", "phone", "radio", "knife", "mug",
    "mirror", "guitar", "paint", "brush", "globe", "wallet", "camera", "garden", "mirror", "pencil",
    "picture", "laptop", "poster", "flower", "wallet", "basket", "remote", "candle", "shovel", "towel",
    "glasses", "bucket", "wallet", "marker", "ladder", "laptop", "painting", "garden", "stereo", "lotion"
]

places = [
    "Rome", "York", "Lima", "Kiev", "Paris", "Delhi", "Cairo", "Tokyo", "Sydney", "Dubai",
    "London", "Berlin", "Moscow", "Seoul", "Tokyo", "Athens", "Nairobi", "Sydney", "Beirut", "Mumbai",
    "Madrid", "Vienna", "Dublin", "Oslo", "Budapest", "Sofia", "Lisbon", "Prague", "Taipei", "Havana",
    "Athens", "Tokyo", "Riyadh", "Kuwait", "Nairobi", "Beijing", "Jakarta", "Brasília", "Wellington", "Lusaka",
    "Canberra", "Amman", "Bogotá", "Belgrade", "Tirana", "Helsinki", "Caracas", "Minsk", "Santiago", "Zagreb"
]


topic = [animals,things,places]
random_topic = random.choice(topic)
word = random.choice(random_topic)

word_lower = word.lower()
word_length = len(word)


if word in animals:
    print("Your word is related to the topic : Animals\n")
if word in things:
    print("Your word is related to the topic : Things\n")
if word in places:
    print("Your word is related to the topic : Places\n")    

print("Your word is : \n")
blanks = []    
for i in range(0,word_length):
    blanks.append("_")
show()

word_list = list(word_lower)

number_of_chances=6
inc_guess=[]

while (number_of_chances >=0):

    choice = str(input("\n\nEnter a character: "))
    clear_terminal()
    for i in range(0,word_length):
        if choice == word_list[i]:
            blanks[i]=choice
    
    if choice not in word_list:
        inc_guess.append(choice)
        print(f"Incorrect Guess\n{number_of_chances} chances remaining.")
        print(stages[number_of_chances])
        print(f"Your previous incorrect guessess are :  {inc_guess}")
        number_of_chances-=1

    show()
    

    if number_of_chances == -1:
        print(f"Game over ! The word was {word}")

    if "_" not in blanks:
        print("You Won !!")

