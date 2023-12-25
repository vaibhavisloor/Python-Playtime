# with open("Files\my_file.txt") as file #Simply opens the file 
#     contents = file.read() #Reads the file and stores the contents into a variable called contents
#     print(contents)


# If you use with statement there is no explicit need to close the file. At the end of the block the file is closed 

# By default the mode of file is set to write. We need to change it as per our need.

with open("Files\my_file.txt","w") as file : #Simply opens the file 
    contents = file.write("This is in write Mode") #Reads the file and stores the contents into a variable called contents
    print(contents)

# Append adds to the existing text.
# While write mode over writes the text.

