class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        
        for i in range(len(words)):
            rowWord, colWord = words[i], []
            for j in range(len(words)):
                if len(words[j])-1 < i:
                    break
                colWord.append(words[j][i])
            if rowWord != ''.join(colWord):
                return False
        return True
    
    
    
    
    