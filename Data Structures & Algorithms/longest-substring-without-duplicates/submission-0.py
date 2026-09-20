class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        cur_len = 0
        sub = ""
        for i in range(len(s)):
            if s[i] in sub:
                char = s[i]
                sub+=char
                sub = sub[sub.index(char) + 1:]
                cur_len = len(sub)
                max_len = max(max_len,cur_len)

            else:
                sub+=s[i]
                cur_len+=1
                max_len = max(max_len, cur_len)
        return max_len




        