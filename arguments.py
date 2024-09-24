def add(*args): 
    sum=0
    print(type(args))
    for n in args:
        sum+=n
    print(sum)

add(1,2,3,4,5,6,7,8,9,10)        

# -------------------------------

class PC:
    def __init__(self,**kw):
        self.make=kw.get("make")
        self.model=kw.get("model")

one = PC(make="HP")
print(one.model)        
print(one.make)      

# ------------------------------------

def display(**kwargs):
    for x,y in kwargs.items():
        print(y)

display(n="Vai",a=20, p=305)

