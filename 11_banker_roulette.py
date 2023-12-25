# import random
# names = input("Enter the first names (Leave a space and type and the next name): \n")
# names_list = names.split(" ")

# random_index = random.randint(0,len(names_list)-1)
##In randint(a,b) both a and b are included
# random_person = names_list[random_index]

# print(f"Today {random_person} will pay the bill !!")


# Alternative

import random
names = input("Enter the first names (Leave a space and type and the next name): \n")
names_list = names.split(" ")

random_dude = random.choice(names_list)

print(f"Today {random_dude} will pay the bill")