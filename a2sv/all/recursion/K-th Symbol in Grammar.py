class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1 and k == 1:
            return 0
        
        mid = pow(2, n-1) // 2
        if k <= mid:
            return self.kthGrammar(n-1, k)
        elif k > mid:
            return 1 if self.kthGrammar(n-1, k-mid) == 0 else 0