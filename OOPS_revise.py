# Encapsulation

class Laptop:
    def __init__(self,maker,prscr):
        self.maker = maker
        self.__prscr = prscr

    def show(self):
        return self.__show_prcr()
    
    def __show_prcr(self):
        print(self.__prscr)

    def run(self):
        print(f"This laptop built by {self.maker} using the {self.__prscr}")

hp = Laptop("hp","i5")

hp.show()

# Inheritance

class Animal:
    def __init__(self,legs) :
        self.legs = legs

    def no_legs(self):
        print("This guy has {self.legs} legs")    

class bird(Animal):
    def __init__(self, mood):
        self.mood = mood
        
    def sound(self):
        print("Chirp Chirp")

sparrow = bird(2)
sparrow.no_legs()
sparrow.sound()
        