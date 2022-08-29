class Solution:
    def depthSum(self, nestedList: List[NestedInteger], depth = 1) -> int:
        
        temp_sum=0
        
        for nest in nestedList:
            if nest.isInteger():
                temp_sum += depth * nest.getInteger()
            else:
                temp_sum += self.depthSum(nest.getList(),depth+1)
                
        return temp_sum
    
    
    