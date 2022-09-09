class Solution(object):
    def leftMostColumnWithOne(self, binaryMatrix):
        """
        :type binaryMatrix: BinaryMatrix
        :rtype: int
        """
        r,c = binaryMatrix.dimensions()
        result = set()
        
        for i in range(r):
            l,r = 0, c-1 
            while l<r:
                m = l + (r - l)//2
                if binaryMatrix.get(i,m) == 0:
                    l = m+1 
                else:
                    r = m 
            if binaryMatrix.get(i,r) == 1:
                result.add(r)
            
        return min(result) if result else -1