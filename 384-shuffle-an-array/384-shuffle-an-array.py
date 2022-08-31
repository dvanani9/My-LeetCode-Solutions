class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.shuffles = nums[:]
        

    def reset(self) -> List[int]:
        self.shuffles = self.nums[:]
        return self.shuffles

    def shuffle(self) -> List[int]:
        random.shuffle(self.shuffles)
        return self.shuffles