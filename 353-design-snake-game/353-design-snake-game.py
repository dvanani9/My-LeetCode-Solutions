class SnakeGame:
    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.width = width
        self.height = height
        self.food = collections.deque(food)
        self.score = 0
        self.body = collections.deque([[0,0]])

    def move(self, direction: str) -> int:
        print(self.food)
        head = self.body[-1]
        
        if direction == 'U':            
            newHead = [head[0] - 1, head[1]]
        elif direction == 'D':
            newHead = [head[0] + 1, head[1]]
        elif direction == 'L':
            newHead = [head[0], head[1] - 1]
        elif direction == 'R':
            newHead = [head[0], head[1] + 1]
            
        if newHead[0] < 0 or newHead[0] > self.height-1 or newHead[1] < 0 or newHead[1] > self.width-1: #check out of bound
            return -1
        elif self.food and newHead == self.food[0]: #check if have food
            self.score += 1
            self.food.popleft()
            self.body.append(newHead)
        else: #add new head to body(last element indeque)
            self.body.popleft()
            if newHead in self.body: #don't forget rto check if collision
                return -1
            else:
                self.body.append(newHead)

        return self.score