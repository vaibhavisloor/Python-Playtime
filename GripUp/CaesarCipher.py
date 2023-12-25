alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
new_text=''
text = input("Enter the text to be encryted : ")
shift = int(input("Enter the shift amount : "))

for i in range (0,len(text)):
    for j in range (0,49):
        if text[i] == alphabet[j]:
            new_position = j + shift
            new_text += alphabet[new_position]
            break



print(new_text)