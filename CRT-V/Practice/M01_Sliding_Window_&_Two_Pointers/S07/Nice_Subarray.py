'''
leetcode:- 1763
'''
from typing import List
def longestNiceSubstring(s: str) -> str:
        if len(s)<2:
            return ""
        char_set=set(s)
        for i , c in enumerate(s):
            if c.lower() in char_set and c.upper() in char_set:
                continue
            sub1=longestNiceSubstring(s[:i])
            sub2=longestNiceSubstring(s[i + 1:])
            return sub1 if len(sub1) >= len(sub2) else sub2
        return s
s = "YazaAay"
print(longestNiceSubstring(s))