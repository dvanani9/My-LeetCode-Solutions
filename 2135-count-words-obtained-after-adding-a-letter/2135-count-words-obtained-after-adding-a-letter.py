class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        starts, ans = set(), 0
        ans = 0
        for word in startWords:
            starts.add(''.join(sorted(word)))
        for word in targetWords:
            for i in range(len(word)):
                if ''.join(sorted(word[:i] + word[i+1:])) in starts:
                    ans += 1
                    break
        return ans