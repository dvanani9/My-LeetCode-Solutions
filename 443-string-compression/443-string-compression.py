class Solution:
    def compress(self, chars: List[str]) -> int:  
        i, j = 0, 0
        count = 1
        length = 0
        while i<len(chars):
            if i<len(chars)-1 and chars[i] == chars[i+1]:
                count += 1
            else:
                chars[j] = chars[i]
                j += 1
                length += 1
                if count>1:
                    for chr in str(count):
                        chars[j] = chr
                        j += 1
                        length += 1
                count = 1     
            i += 1      
            
        return length