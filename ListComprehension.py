# Basic logic of List Comprehension
# new_list = [new_item for item in list]

# name = "Vaibhav"
# new_list=[item for item in name]
# print(new_list)
#
# Output : ['V', 'a', 'i', 'b', 'h', 'a', 'v']


# new_list = [n*2 for n in range(1, 5)]
# print(new_list)
#
# Output : [2, 4, 6, 8]


names = ["Alex", "Hales", "Beth", "Caroline", "Dave", "Freddie", "Eleanor"]
#
# new_list = [name.upper() for name in names if len(name) > 5]
# print(new_list)


# DICTIONARY COMPREHENSION

# new_dict = {new_key : new_value for (key,value) in dict.items() if test}

# import random
# students_score = {student:random.randint(1,100) for student in names}
# passed_students = {student:score for (student,score) in students_score.items() if score>=40}
# print(passed_students)


# name= "Vaibhav"

# nested_list = [[1, 2, 3], [4, 5], [6, 7, 8]]
# # Expected output: [1, 2, 3, 4, 5, 6, 7, 8]


# lists = [x for letter in nested_list for x in letter]
# print(lists)


words = ["hello", "world", "python"]
# Expected output: ['olleh', 'dlrow', 'nohtyp']

num=5
lists = [num*i for i in range(1,11)]
print(lists)