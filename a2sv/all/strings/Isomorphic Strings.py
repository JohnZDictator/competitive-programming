class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        top_dict = {}
        bottom_dict = {}
        n = len(s)
        for idx in range(n):
            if s[idx] not in top_dict:
                top_dict[s[idx]] = t[idx]
            elif top_dict[s[idx]] != t[idx]:
                return False
            if t[idx] not in bottom_dict:
                bottom_dict[t[idx]] = s[idx]
            elif bottom_dict[t[idx]] != s[idx]:
                return False
        return True