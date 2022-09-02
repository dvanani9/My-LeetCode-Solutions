class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        
        for house in range(1,len(costs)):
            
            costs[house][0] += min(costs[house-1][1], costs[house-1][2])
            costs[house][1] += min(costs[house-1][0], costs[house-1][2])
            costs[house][2] += min(costs[house-1][1], costs[house-1][0])
            
            
        return min(costs[-1])