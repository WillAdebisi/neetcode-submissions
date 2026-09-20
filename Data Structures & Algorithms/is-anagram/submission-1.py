class Solution:
    from collections import defaultdict
    def isAnagram(self, s: str, t: str) -> bool:
        s_dic = defaultdict(int)
        t_dic = defaultdict(int)
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            a = s[i]
            b = t[i]
            s_dic[a] += 1
            t_dic[b] += 1
        return s_dic == t_dic

        