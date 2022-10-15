class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        nums = collections.Counter(secret) # Counting occurences of each digit in secret.
        cows = 0
        bulls = 0
        
        # Counting Cows
        for n in guess:
            if n in nums:
                cows += 1
                
                # Subtracting occurences of digit from hash-map to avoid counting same number multiple times.
                # Eg: secret: 1234567 and guess: 1111112 will give cows = 8 without the below code.
                nums[n] -= 1
                if nums[n] == 0:
                    nums.pop(n)
        
        # Counting Bulls
        for n1, n2 in zip(secret, guess):
            if n1 == n2:
                bulls += 1
                cows -= 1 # Subtracting cows which are bulls.
                
        return f"{bulls}A{cows}B"