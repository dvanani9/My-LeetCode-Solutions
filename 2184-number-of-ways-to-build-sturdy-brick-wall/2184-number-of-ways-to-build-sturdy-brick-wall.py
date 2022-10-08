class Solution:
    def buildWall(self, height: int, width: int, bricks: List[int]) -> int:
        
        # step 1: get all combinations of bricks
        ways = set()
        
        def helper(path, t):
            if t == 0:
                ways.add(path)
                return
            for i in range(len(bricks)):
                if t >= bricks[i]:
                    helper(path + (bricks[i],), t - bricks[i])

        helper(tuple(), width)
        if not ways:
            return 0
        
        # step 2: prefix sum and bitmask
        out = set()
        for way in ways:
            mask = 0
            for acc in accumulate(way):
                if acc == width: continue
                mask ^= 1 << acc
            out.add(mask)

        # step 3: build graph for non overlapping prefix sum
        nei = defaultdict(set)
        for x in out:
            nei[x] = set()
            for y in out:
                if x & y == 0: nei[x].add(y)

        # step 4: DP
        @lru_cache(None)
        def dp(i, prev):
            if i == height:
                return 1
            return sum(dp(i+1, x) % (10**9+7) for x in nei[prev]) % (10**9+7)            
        
        return sum(dp(1, x) for x in nei) % (10**9+7)