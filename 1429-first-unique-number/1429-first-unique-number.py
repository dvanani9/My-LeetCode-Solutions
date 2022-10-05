class FirstUnique:

    def __init__(self, nums: List[int]):
        self.nums_all_set = set()
        self.nums_dup_set = set()
        self.queue = []
        self.idx = 0
        
        for num in nums:
            self.add(num)
        
    def showFirstUnique(self) -> int:
        while self.idx < len(self.queue):
            if self.queue[self.idx] not in self.nums_dup_set:
                return self.queue[self.idx]
            else:
                self.idx += 1
        return -1

    def add(self, value: int) -> None:
        if value in self.nums_all_set:
            self.nums_dup_set.add(value)
        self.nums_all_set.add(value)
        self.queue.append(value)