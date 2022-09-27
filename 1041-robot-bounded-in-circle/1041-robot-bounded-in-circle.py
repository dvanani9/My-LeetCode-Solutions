class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        currdirection = 'N'
        x,y = 0,0
        for i in range(0,len(instructions)):
            if instructions[i] == 'G':
                if currdirection=='N':
                    y += 1
                elif currdirection=='S':
                    y -= 1
                elif currdirection=='E':
                    x += 1
                else:
                    x -= 1
            else:
                var = instructions[i]
                if currdirection == 'N':
                    currdirection = 'W' if var == 'L' else 'E'
                elif currdirection == 'E':
                    currdirection = 'N' if var == 'L' else 'S'
                elif currdirection == 'S':
                    currdirection = 'E' if var == 'L' else 'W'
                else:
                    currdirection = 'S' if var == 'L' else 'N'

        if x == 0 and y == 0:
            return True 
        if currdirection != 'N':
            return True

        return False 
