class animal:
    def __init__(self):
        print("animal")

class bird(animal):
    def __init__(self):
        super().__init__()
        print("base call")
    def show(self):
        print("birds")

class parrot(bird):
    def __init__(self):
        super().__init__() #use to call parent fucntion
        print("child call")
    def show(self):
        super().show()
        print("parrot")

bb=parrot()
bb.show()