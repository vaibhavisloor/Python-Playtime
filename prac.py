# a=['a','b','c']
# # print(int(a))
# a=[1,2,3]
# print(list(reversed(a)))

# b="abcdef"
# print(list(reversed(b)))

# c=''.join('a')
# print(c)

# num='123'

# zeros=5

# final = num + "0" * zeros
# print(final)

# print(reversed('1234'))


# import os

# for i in os.environ.items():
#     print(i)

# a1=[1,2,1]
# a2=[1,1,2]
# a3=[2,1,1]

# a11=sorted(a1)
# a22=sorted(a2)
# a33=sorted(a3)

# print(a11,a22,a33)


# from datetime import datetime

# d = str(datetime.now())

# print(d[11:19])

# response={'exercises': [{'tag_id': 317, 'user_input': 'ran', 'duration_min': 300.06, 'met': 9.8, 'nf_calories': 3430.69, 'photo': {'highres': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_highres.jpg', 'thumb': 'https://d2xdmhkmkbyw75.cloudfront.net/exercise/317_thumb.jpg', 'is_user_uploaded': False}, 'compendium_code': 12050, 'name': 'running', 'description': None, 'benefits': None}]}

# for exercise in response['exercises']:
#     print(exercise)
# print(response['exercises'][0])



s1 = [1,1,2,3,3,3,4,5]
print(set(s1))
print(type(list(set(s1))))



import requests
i=1
while True:
    requests.get("https://tubefetcher.xyz/")
    print(i)
    i+=1

