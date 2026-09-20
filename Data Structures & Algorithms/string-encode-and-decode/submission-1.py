class Solution:
    from collections import defaultdict

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            for char in word:
                encoded_string+=str(ord(char))
                encoded_string+=','
            encoded_string += ']'
            encoded_string+=','

        return encoded_string

    def decode(self, s: str) -> List[str]:
        ans = []
        s_list = s.split(",")
        s_list = s_list[:-1]
        word = ""

        for num in s_list:
            if num == ']':
                ans.append(word)
                word = ""
            else:
                word+=chr(int(num))
            
        return(ans)
