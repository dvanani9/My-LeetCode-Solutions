class Solution:
    def minimumKeypresses(self, s: str) -> int:
        
        freq = {}
        
        for c in s:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1
        
        f = sorted(zip(freq.values(), freq.keys()), reverse = True)

        res = 0
        for i in range(len(f)):
            if i <= 8:
                res += f[i][0]
            elif 8 < i <= 17:
                res += 2 * f[i][0]
            else:
                res += 3 * f[i][0]
        
        return res