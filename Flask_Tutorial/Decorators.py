# import time
# current_time = time.time()
# print(current_time) # seconds since Jan 1st, 1970 

# def speed_calc_decorator(function):
#   def wrapper():
#     start=time.time()
#     function()
#     end=time.time()
#     print(f"{function.__name__} speed : {end-start}")
#   return wrapper

# @speed_calc_decorator
# def fast_function():
#   for i in range(1000000):
#     i * i
        
# @speed_calc_decorator
# def slow_function():
#   for i in range(10000000):
#     i * i

# fast_function()

# slow_function()

class User:
    def __init__(self, name):
        self.name = name
        self.is_authenticated = False

# def check_authenticated(function):
#     def wrapper(*args, **kwargs):
#         if args[0].is_authenticated:
#             return function()
#         else:
#             return "Not authenticated"
#     return wrapper

# @check_authenticated
# def create_blog_post(user):
#     return f"<h1>This is {user.name}'s post</h1>"

# user = User("Vaibhav")

# print(create_blog_post(user))


def decorator(func):
    def wrapper(*args):
        print(f"The first arg is {args[0]}")
        result = func(*args)
        return result
    return wrapper

@decorator
def add(*args):
    print(sum(args))

add(1,2,3,4,5,6,7,8,9,10)