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



# s1 = [1,1,2,3,3,3,4,5]
# print(set(s1))
# print(type(list(set(s1))))



# import requests
# i=1
# while True:
#     requests.get("https://tubefetcher.xyz/")
#     print(i)
#     i+=1
# import math

# num = int(input())

# def prime(num):
#     for i in range(2,num):
#         if num%i == 0:
#             print("Not prime")
#             return
#     print("Prime")  

# prime(num)


# n='abc'

# h='xysdagidabc'

# for i in range(len(h)):
#     substring = h[i:i+len(n)]

#     print(substring)


# num = [1,2,3]

# def sq(x):
#     return x**2
# print(list(map(sq ,num)))


# string = "abc"

# for i,val in enumerate(string):
#     print(i,val)

# import random
# num = random.randint(0,9)
# print(num)

# import random
# a="Welcome Home dear doggy. You will stay here from today"
# print((a.split()))


# a = [1,2,3,4,5,6,7,8,9]

# print([x*x for x in a if x%2==0])

# def make_counter(x=0):
#     def inner():
#         nonlocal x
#         x += 1
#         return x
#     return inner
# counter = make_counter()
# print(counter())
# print(counter())
# print(counter())
# print(counter())
        
# def make_adder(x):
#     def inner(n):
#         return x+n
#     return inner

# adder_5 = make_adder(5)
# print(adder_5(10))


# def make_uppercase(func):
#     def wrapper(name):
#         name = name.upper()
#         return func(name)
#     return wrapper

# @make_uppercase
# def say_hi(name):
#     return f"Hello, {name}"

# print(say_hi('vaibhav'))

# products = [
#     {"name": "Bamboo Cutting Board", "cost": 5, "selling_price": 25, "weight_kg": 1.2},
#     {"name": "Silicone Spatula Set", "cost": 3, "selling_price": 19, "weight_kg": 0.4},
#     {"name": "Ergonomic Mouse", "cost": 12, "selling_price": 30, "weight_kg": 0.2},
#     {"name": "Desk Mat", "cost": 8, "selling_price": 20, "weight_kg": 0.8},
#     {"name": "Wireless Charger", "cost": 10, "selling_price": 28, "weight_kg": 0.3}
# ]

# print([product["name"] for product in products if product["selling_price"] - product["cost"] >= 15 and product["weight_kg"] > 0])


# def make_tracker(initial_hours):
#     def inner(x):
#         nonlocal initial_hours
#         initial_hours += x
#         return initial_hours
#     return inner

# tracker = make_tracker(100)
# tracker(10)
# tracker(30)
# print(tracker(1))
# print(tracker(1))
# print(tracker(1))

# import time
# def measure_latency(func):
#     def wrapper():
#         start_time = time.time()
#         func()
#         end_time = time.time()
#         print(end_time  - start_time)
#     return wrapper

# @measure_latency
# def sample_func():
#     time.sleep(1.5)

# print(sample_func())

# def generator(n=1):
#     while n:
#         yield n
#         n+=1
# counter = generator()
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))


# from contextlib import contextmanager
# import time

# @contextmanager
# def capture_session(game_title):
#     print(f"Initializing {game_title}......")
#     time.sleep(1.5)
#     print(f"Preparing to record gameplay {game_title}......")
#     time.sleep(1.5)
#     print(f"Recording and game started")

#     recording = "ACTIVE"

#     try:
#         print("Yielding boy")
#         yield recording
#         print("Yield Completed")
#     finally:
#         print("Stopping the recording.....")
#         time.sleep(1.5)
#         print("Saving the recording.....")
#         time.sleep(1.5)
#         print("Closing down the game.....")

# try:
#     with capture_session("GTA6") as game:
#         print("\n\nGame play has started (YAAY)")
#         time.sleep(1)
#         print(f"GAME STATUS : {game}")

#         print('Uhhh....Ohh...GPU Overloading')
#         # raise Exception("GPU overloading bruhhh")
# finally:
#     print("Game over bruhh byeee..")


# sample_dict = {
#     'hello' : [1,2,3,4,5],
#     'namaste' : [5,6,7,8]
# }

# print(set("tea"),set("ate"),set("tae"),set("aet"),set("eat"))


# a = lambda x,y: x+y
# print(a(3,4))

# x = [1,2,3,4,5]
# a = map(lambda x:x*x , x)
# print(list(a))


# dicty = {
#     'a':1,
#     'd':10,
#     'z':4,
#     'b':2,
#     'c':3
# }

# x = sorted(dicty,key = dicty.values())


# class Soldier:
#     def __init__(self):
#         self.__gold = 0
#         self.name = "Murrah"

#     def give_gold(self, amount):
#         self.__gold += amount
#         print(f"{amount} coins have been given")

    
#     def take_gold(self,amount):
#         if self.__gold >= amount:
#             self.__gold -= amount
#             print(f"{amount} coins have been taken")
#         else:
#             print(f"This soldier has only {self.__gold} coins left.")
    
#     def view(self):
#         return self.__gold
    
# soldier1 = Soldier()
# soldier1.give_gold(10)
# soldier1.give_gold(10)
# soldier1.give_gold(10)
# soldier1.take_gold(20)
# soldier1.take_gold(30)
# soldier1.view()
# print(soldier1._Soldier__gold)
# soldier1._Soldier__gold = 1000
# soldier1.view()




# arr = [10,2,18,34,23,9,45,16,5]
# print(arr)

# def build_heap(arr):
#     index_last_non_child = len(arr)//2 - 1

#     for i in range(index_last_non_child,-1,-1):
#         heapify(arr,i,len(arr))

# def heapify(arr,i,n):
#     left = 2 * i + 1
#     right = left+1

#     largest = i

#     if left < n and arr[left] > arr[largest]:
#         largest = left
    
#     if right < n and arr[right] > arr[largest]:
#         largest = right

#     if i != largest:
#         arr[i],arr[largest] = arr[largest], arr[i]
#         heapify(arr,largest,n)

# def heap_sort(arr):
#     build_heap(arr)
#     last_index = len(arr) - 1
        
#     while last_index > 0:
#         arr[0],arr[last_index] = arr[last_index],arr[0]
#         last_index-=1
#         heapify(arr,0,last_index)

#     print(arr)
# heap_sort(arr)

# class Animal:
#     def __init__(self):
#         self.alive = 1

#     def speak(self):
#         print("Animal speaking")

# class Dog(Animal):
#     def __init__(self):
#         super().__init__()
#         self.legs=4


# d = Dog()
# d.speak()
# print(d.alive)


# class TreeNode:
#     def __init__(self,val):
#         self.val = val
#         self.left = None
#         self.right = None


# class BST:
#     def __init__(self):
#         self.root = None

#     def add_node(self,root,val):
#         if self.root is None:
#             return TreeNode(val)
#         if self.root.val > val:
#             root.left = self.add_node(root.left,val)
#         elif self.root.val < val:
#             root.right = self.add_node(root.right,val)
#         return root   

#     def search(self,val,root):
#         if root is None:
#             print("Not found")
#             return
#         if root.val == val:
#             print("Found")
#             return
#         if root.val > val:
#             return self.search(val,root.left)
#         else:
#             return self.search(val,root.right)
        
#     def get_right_min(self,root):
#         while root.left:
#             root = root.left

#     def delete_node(self,root,val):
#         if root is None:
#             return None
        
#         if root.val < val:
#             root.right =  self.delete_node(root.right,val)
#         elif root.val > val:
#             root.left =  self.delete_node(root.left,val)
#         else:
#             if root.right is None and root.left is None:
#                 return None
#             elif root.right is None:
#                 return root.left
#             elif root.left is None:
#                 return root.right
#             else:
#                 #left and right child exist, so we take rightmin.
#                 min_node = self.get_right_min(root.right)
#                 root.val = min_node.val

#                 root.right = self.delete_node(root.right,min_node.val)
#         return root



    
# bst = BST()
# root = None

# root = bst.add_node(root,10)


arr = [1]
print(arr[0])
print(arr[-1])

import math
print(math.ceil(1.2434234))