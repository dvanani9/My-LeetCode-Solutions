class Solution:
    def minDeletions(self, s: str) -> int:
        
        hashmap={}
        count=0
        
        for i in s:
            if i not in hashmap:
                hashmap[i]=1
            else:
                hashmap[i]+=1
                
        arr=[]
        for i in hashmap:
            while(hashmap[i] in arr and hashmap[i]!=0):
                hashmap[i]-=1
                count+=1
            arr.append(hashmap[i])
        return count