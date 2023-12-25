#Dictionaries are stored in a variable and are indicated by key : value pairs. Ensure you put a ' , ' after each key value pair. While printing, we should enter the key and the value gets printed. Somewhat like a list

sample_dictionary={"Book":"A collection of papers combined together as a unit for storing some information",
                   "Mobile":"Communication Device"
}

#Ensure you use the correct data types
print(sample_dictionary["Book"])


# # If you wanna enter new data to the dictionary, if the key doesnt exist itll make a new one. If key exists the value gets over written
sample_dictionary["Vaibhav"] = "The GG boi"

print(sample_dictionary)


print(sample_dictionary)
#On printing the dictionary, you get only the keys and their value pairs as the output

# If you loop thorugh the dictionary, only then you get the keys only