class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        indice1 = []
        indice2 = []
        min_distance = 3*10**4 + 1
        for i, word in enumerate(wordsDict):
            if word == word1:
                indice1.append(i)
            elif word == word2:
                indice2.append(i)
        for i in indice1:
            for j in indice2:
                min_distance = min(min_distance, abs(i-j))
        return min_distance 