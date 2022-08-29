class RandomizedSet:

    def __init__(self):
        self.arr=[]

    def insert(self, val: int) -> bool:
        if val in self.arr:
            return 0
        self.arr.append(val)
        return 1

    def remove(self, val: int) -> bool:
        if val not in self.arr:
            return 0
        self.arr.remove(val)
        return 1
        

    def getRandom(self) -> int:
        return choice(self.arr)