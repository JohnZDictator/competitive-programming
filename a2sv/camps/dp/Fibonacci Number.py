class Solution:
    memo ={}
    
    def fib(self, n: int) -> int:
        
        if n in self.memo:
            return self.memo[n]
        
        if n == 1:
            return 1
        elif n == 0:
            return 0
        
        left = self.fib(n - 1)
        right = self.fib(n - 2)
        
        self.memo[n] = left + right
        
        return self.memo[n]