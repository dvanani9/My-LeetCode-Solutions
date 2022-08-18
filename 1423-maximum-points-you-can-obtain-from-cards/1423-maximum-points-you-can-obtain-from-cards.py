class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        maxScore = score = sum(cardPoints[i] for i in range(n - k, n))
        for i in range(k):
            score += cardPoints[i]
            score -= cardPoints[n - k + i]
            maxScore = max(maxScore, score)
        
        return maxScore