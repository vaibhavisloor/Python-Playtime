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

import os

def clear_terminal():
       if os.name == 'nt':  
            os.system('cls')

def show():
      for i in range(0,len(blanks)):
            print(blanks[i],end=" ")          



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

word = "Vaibhav".lower()
blanks=[]
number_of_chances = 6
stages_index = 5



for i in range(0,len(word)):
    blanks.append('_')
show()

while number_of_chances != 0:


    choice = input("\n\nEnter your choice : ")

    for i in range(0,len(word)):
            if choice == word[i]:
                blanks[i] = choice
            
    if choice not in word:
        number_of_chances-=1
        print(f"Incorrect guess. You have {number_of_chances} chances left")
        print(stages[stages_index])
        stages_index-=1

    if '_' not in blanks:
        print("Congratulations you win !")              
    
    show()            

if number_of_chances == 0:
    print(f"The word was {word}")