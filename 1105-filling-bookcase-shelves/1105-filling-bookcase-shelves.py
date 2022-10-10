class Solution:

    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:        

        @cache
        def dp(idx: int, curr_height: int, curr_width: int):
            if curr_width < 0:
                return float("inf")

            if idx == len(books):
                return curr_height

            thickness, height = books[idx]
            same_shelf = dp(idx + 1, max(curr_height, height), curr_width - thickness)
            change_shelf = curr_height + dp(idx + 1, height, shelfWidth - thickness)
            return min(same_shelf, change_shelf)

        return dp(0, 0, shelfWidth)