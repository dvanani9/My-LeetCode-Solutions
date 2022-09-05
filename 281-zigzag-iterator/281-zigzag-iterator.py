class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        
        self.res = []
        
        while v1 and v2:
            self.res.append(v1.pop(0))
            self.res.append(v2.pop(0))
            
        if v1:
            self.res+=v1
        if v2:
            self.res+=v2

    def next(self) -> int:
        
        return self.res.pop(0)

    def hasNext(self) -> bool:
        
        return self.res!=[]