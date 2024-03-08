try:
    file = open("./file.txt", "r+")
except FileNotFoundError: #If exception found 
    # If the file doesn't exist, create it
    file = open("./file.txt", "w")
    file.write("File created")
else: #If no execption
    # File exists, so write additional content
    file.write("Additional content")
finally:
    raise TypeError
    file.close()
