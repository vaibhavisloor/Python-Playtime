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