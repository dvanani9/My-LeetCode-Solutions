class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        ans=0
        nums.sort()
        n=len(nums)
        for i in range(n-2):
            l=i+1
            r=n-1
            while l<r:
                sumval=nums[i]+nums[l]+nums[r]
                if sumval<target:
                    ans+=(r-l)  #if sum with value at r is smaller, then all the sum  between l and r will also be smaller
                    l+=1
                else:
                    r-=1
        return ans