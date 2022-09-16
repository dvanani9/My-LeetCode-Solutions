class MyHashMap:

    def __init__(self):
        self.hp = [-1] * 1000001;

    def put(self, key: int, value: int) -> None:
        self.hp[key] = value

    def get(self, key: int) -> int:
        return self.hp[key] 

    def remove(self, key: int) -> None:
        self.hp[key] = -1