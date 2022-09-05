class Solution:
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) != len(words2):
            return False
        dic = collections.defaultdict(set)
        for p1, p2 in pairs:
            dic[p1].add(p2)
            dic[p2].add(p1)
        
        for w1, w2 in zip(words1, words2):
            if (w2 not in dic[w1] or w1 not in dic[w2]) and w1 != w2:
                return False
        return True
        