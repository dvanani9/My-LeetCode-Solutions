class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        left, right = 0, len(arr)-1
        save = -1

        while left <= right:
            mid = left + (right-left)//2

            if arr[mid]>mid:
                right = mid-1

            elif arr[mid]<mid:
                left = mid+1

            else:
                right = mid-1
                save = mid 

        return save