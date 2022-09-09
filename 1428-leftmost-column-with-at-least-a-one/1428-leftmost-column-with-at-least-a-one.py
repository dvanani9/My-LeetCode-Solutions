class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        dim = binaryMatrix.dimensions()
        rows = dim[0]
        cols = dim[1]
        cr = 0
        cc = cols - 1
        result = -1
        while cr < rows and cc >= 0:
            node = binaryMatrix.get(cr, cc)
            if node == 1:
                result = cc
                cc -= 1
            else:
                cr += 1
                
        return result