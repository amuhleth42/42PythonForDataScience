class calculator:

    def __init__(self, lst):
        self.lst = lst


    def __add__(self, object) -> None:
        self.lst = [x + object for x in self.lst]
        print(self.lst)


    def __mul__(self, object) -> None:
        self.lst = [x * object for x in self.lst]
        print(self.lst)


    def __sub__(self, object) -> None:
        self.lst = [x - object for x in self.lst]
        print(self.lst)


    def __truediv__(self, object) -> None:
        if (object == 0):
            print("Error: division by 0 is not allowed")
        else:
            self.lst = [x / object for x in self.lst]
            print(self.lst)
