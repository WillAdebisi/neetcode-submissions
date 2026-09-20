class Solution:
    from collections import defaultdict

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        set_strs = set(strs)
        set_strs = list(set_strs)
        ans = defaultdict(list)
        for i in range(len(strs)):
            item = strs[i]
            x = sorted(item)
            x = "".join(x)
            ans[x].append(item)
        ans = list(ans.values())
        return(ans)
            
        
                    

        