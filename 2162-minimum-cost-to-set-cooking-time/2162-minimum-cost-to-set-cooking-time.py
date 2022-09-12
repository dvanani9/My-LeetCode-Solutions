class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        
        std_min = targetSeconds//60
        std_sec = targetSeconds%60

        ways = []

        # Under 6000 to avoid the minute number being 100
        # "Standard" way of typing the min-sec combination
        if targetSeconds < 6000:
            if std_sec < 10:
                std_sec = "0" + str(std_sec)
            ways.append(str(std_min)+str(std_sec))

            if std_min < 10:
                std_min = "0" + str(std_min)
            ways.append(str(std_min)+str(std_sec))

            if targetSeconds < 100:
                ways.append(str(targetSeconds))
                ways.append("0"+str(targetSeconds))
                ways.append("00"+str(targetSeconds))

        # "Special" case of putting one (and only one) minute into seconds
        if int(std_min) > 1 and int(std_sec) < 40:
            alt_time = str(int(std_min)-1) + str(int(std_sec)+60)
            ways.append(alt_time)
            if len(alt_time) == 3:
                ways.append("0"+alt_time)

        time_costs = []

        # Tedious to save time during contest...
        # Adding total cost
        for x1 in range(len(ways)):
            x1_cost = 0

            # If finger already at initial digit
            if ways[x1][0] != str(startAt):
                x1_cost += moveCost
            if len(ways[x1]) == 1:
                x1_cost += pushCost
            elif len(ways[x1]) == 2:
                x1_cost += pushCost * 2
                if ways[x1][0] != ways[x1][1]:
                    x1_cost += moveCost  
            elif len(ways[x1]) == 3:
                x1_cost += pushCost * 3
                if ways[x1][0] != ways[x1][1]:
                    x1_cost += moveCost
                if ways[x1][1] != ways[x1][2]:
                    x1_cost += moveCost
            elif len(ways[x1]) == 4:
                x1_cost += pushCost * 4
                if ways[x1][0] != ways[x1][1]:
                    x1_cost += moveCost
                if ways[x1][1] != ways[x1][2]:
                    x1_cost += moveCost
                if ways[x1][2] != ways[x1][3]:
                    x1_cost += moveCost
            time_costs.append(x1_cost)

        return(min(time_costs))
