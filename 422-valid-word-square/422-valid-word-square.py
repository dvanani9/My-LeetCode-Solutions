class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        '''
        Time: O(n^2) -> In the worst case, all rows and columns must be checked!
        Space: O(1)
        '''
        n = len(words)
        for i in range(n):
            row = words[i] 
            if len(row) > len(words):
                return False       
            for j in range(len(row)):
                if len(words[j]) <= i or words[j][i] != row[j]:
                    return False
        return True