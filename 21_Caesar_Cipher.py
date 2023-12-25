print('''  
    __   ____    ___  _____  ____  ____  
   /  ] /    |  /  _]/ ___/ /    ||    \ 
  /  / |  o  | /  [_(   \_ |  o  ||  D  )
 /  /  |     ||    _]\__  ||     ||    / 
/   \_ |  _  ||   [_ /  \ ||  _  ||    \ 
\     ||  |  ||     |\    ||  |  ||  .  \
 \____||__|__||_____| \___||__|__||__|\_|
                                         
    __  ____  ____  __ __    ___  ____   
   /  ]|    ||    \|  |  |  /  _]|    \  
  /  /  |  | |  o  )  |  | /  [_ |  D  ) 
 /  /   |  | |   _/|  _  ||    _]|    /  
/   \_  |  | |  |  |  |  ||   [_ |    \  
\     | |  | |  |  |  |  ||     ||  .  \ 
 \____||____||__|  |__|__||_____||__|\_| 

 ''')


def encrypt(text,shift):
    cipher_text=''
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + shift
            new_letter = alphabet[new_position]
            cipher_text+=new_letter
        else:
            cipher_text+=letter    
    print(cipher_text)   


def decrypt(text,shift):
    cipher_text=''
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position - shift
            new_letter = alphabet[new_position]
            cipher_text+=new_letter
        else:   
         cipher_text+=letter
    print(cipher_text)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

again = "y"

while again == "y":

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if direction == "encode":
        encrypt(text,shift)
    elif direction == "decode":
        decrypt(text,shift)    
    else:
        print("Incorrect option .. Please enter correct option")    
    again = input("\nDo you want to try again ? (y or n)")       