class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        
        for i in range(len(dict[0])):
            
            all_opt = set()
            
            for w in dict:
                w1 = w[:i] + w[i+1:]
                
                if w1 in all_opt:
                    return True
                all_opt.add(w1)
                
        return False
    
    