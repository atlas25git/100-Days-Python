#syntax
class Animal:
    def __init__(self) -> None:
        pass

class Fish(Animal):
    def __init__(self) -> None:
        super().__init__()
    
    def otherAddedFn(self):
        print("This is the added fn over inherited class")
