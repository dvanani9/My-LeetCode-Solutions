class MyCalendar:

    def __init__(self):
        self.start, self.end = [float(-inf)], [float(-inf)]

    def book(self, start: int, end: int) -> bool:
        s = self.start
        e = self.end
        
        closes_end = bisect.bisect_right(e, start)

        if closes_end == len(e):
            s.append(start) 
            e.append(end)
            return True
      
        if e[closes_end-1] <= start and s[closes_end] >= end:
            bisect.insort(s, start, closes_end)
            bisect.insort(e, end, closes_end)
            return True
        return False
    
    
    