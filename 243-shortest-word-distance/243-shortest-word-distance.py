class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        a,b=word1,word2
        counta,countb=0,0
        finala,finalb=math.inf,math.inf
        flg1,flg2=False,False
        for i in range(len(wordsDict)):
            if wordsDict[i]==a:
                counta=0
                flg1=True
                if flg2:
                    finalb=min(countb,finalb)
            elif wordsDict[i]==b:
                countb=0
                flg2=True
                if flg1:
                    finala=min(counta,finala)
            counta+=1
            countb+=1
        return min(finala,finalb)