class DetectSquares:

    def __init__(self):
        self.points = defaultdict(int)
        self.y_points = defaultdict(set)

    def add(self, point: List[int]) -> None:
        x,y = point
        self.points[(x,y)] += 1
        self.y_points[y].add(x)

    def count(self, query: List[int]) -> int:
        qx,y = query
        csum = 0
        for x in self.y_points[y]:
            diff = abs(qx - x)
            if diff != 0:
                if (qx, y+diff) in self.points and (x, y+diff) in self.points:
                    csum += self.points[(x,y)]*self.points[(qx,y+diff)]*self.points[(x,y+diff)]
                if (qx, y-diff) in self.points and (x, y-diff) in self.points:
                    csum += self.points[(x,y)]*self.points[(qx,y-diff)]*self.points[(x,y-diff)]
        return csum