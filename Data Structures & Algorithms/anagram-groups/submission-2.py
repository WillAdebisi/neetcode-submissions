class Solution:
    from collections import defaultdict

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ans = defaultdict(list)
        for item in strs:
            x = "".join(sorted(item))
            ans[x].append(item)
        ans = list(ans.values())
        return(ans)
            
        
                    

        