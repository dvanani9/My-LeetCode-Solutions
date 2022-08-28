class Solution(object):
    def maximalNetworkRank(self, n, roads):
        
        degree=[0 for i in range(n)]
        adj=[[] for i in range(n)]
        
        for i,j in roads:
            degree[i]+=1
            degree[j]+=1
            adj[i].append(j)
            adj[j].append(i)
        ans=0
        for i in range(n):
            for j in range(n):
                if(i!=j):
                    if(i in adj[j]):
                        ans=max(ans,degree[i]+degree[j]-1)
                    else:
                        ans=max(ans,degree[i]+degree[j])
        return ans
    
    