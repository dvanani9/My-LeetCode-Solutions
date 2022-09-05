class Solution:
    def generateAbbreviations(self, s: str) -> List[str]:
        result = []

        if len(s) == 1:
            return [s, '1']
        substrings = self.generateAbbreviations(s[1:])

        # Add s[0] to the beginning of every substring
        for sub in substrings:
            result.append(s[0] + sub)

        # Add 1 to the beginning of every substring, combine nums if necessary
        for sub in substrings:
            if sub[0].isnumeric():
                i = 0
                while i < len(sub) and sub[i].isnumeric():
                    i += 1
                num = 1 + int(sub[0:i])
                result.append(str(num) + sub[i:])
            else:
                result.append('1' + sub)
        return sorted(result)