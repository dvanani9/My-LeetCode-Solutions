class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        length = len(chars)
        start = 0
        end = 0
        for pos, char in enumerate(chars):
            if (pos + 1) == length or chars[pos] != chars[pos + 1]:
                chars[end] = char
                end += 1
                if pos > start:
                    repeated_times = pos - start + 1
                    for num in str(repeated_times):
                        chars[end] = num
                        end += 1
                start = pos + 1
        chars = chars[:end + 1]
        return end