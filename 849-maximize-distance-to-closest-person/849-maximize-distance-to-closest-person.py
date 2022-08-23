class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        spaces = []
        prev = 0
        for i in range(len(seats)):
            if seats[i] == 1:
                spaces.append(i - prev)
                prev = i
        spaces.append(len(seats) - prev - 1)
        return max([spaces[0], spaces[-1], max(spaces) // 2])