class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self._q = deque()
        for v in vec:
            for item in v:
                self._q.append(item)       

    def next(self) -> int:
        return self._q.popleft()

    def hasNext(self) -> bool:
        return self._q