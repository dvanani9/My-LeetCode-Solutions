class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        set1 = set(arr1)
        set2 = set(arr2)
        set3 = set(arr3)

        res1 = set1.intersection(set2)
        res2 = res1.intersection(set3)
        return sorted(res2)
