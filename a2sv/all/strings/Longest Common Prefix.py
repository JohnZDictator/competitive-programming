class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]
        for i in range(1, len(strs)):
            m = len(strs[i])
            n = len(prefix)
            count = 0
            for j in range(m):
                if j >= n:
                    break
                if prefix[j] != strs[i][j]:
                    prefix = strs[i][:j]
                    break
                count += 1
            if count == m:
                prefix = strs[i]
        return prefix