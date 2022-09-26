class Solution:
    def singleNonDuplicate(self, arr: List[int]) -> int:
        
        start = 0
        end = len(arr)-1

        while (start < end):
            mid = start + (end-start)//2

            # handle when mid is odd
            if (mid % 2 != 0):
                if (arr[mid] != arr[mid+1]):
                    start = mid+1
                else:
                    end = mid-1

            # handle when mid is even
            else:
                if (arr[mid] == arr[mid+1]):
                    start = mid+2
                else:
                    end = mid-1
        return arr[start]