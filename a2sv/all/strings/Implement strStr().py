class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)
        if n > m:
            return -1
        for i in range(m):
            count = 0
            for j in range(n):
                if i+j >= m or haystack[i+j] != needle[j]:
                    break
                count += 1
                if count == n:
                    return i
        return -1