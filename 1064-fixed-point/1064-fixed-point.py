class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        
        #Naive solution :
        
        #Go through with a for loop
        for i in range( len ( arr ) ):
            #Check to see it matches its index
            if arr[ i ] == i:
                return i;
        #If it doesn't, return -1
        return -1;