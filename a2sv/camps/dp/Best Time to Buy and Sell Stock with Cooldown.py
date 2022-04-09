class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        def dp(idx, turn, memo):
            state = (idx, turn)
            if state in memo:
                return memo[state]
            if idx >= len(prices):
                return 0
            
            if turn == 0:
                memo[state] = max(-prices[idx] + dp(idx+1, 1-turn, memo), dp(idx+1, turn, memo))
            elif turn == 1:
                memo[state] = max(prices[idx] + dp(idx+2, 1-turn, memo), dp(idx+1, turn, memo))
            
            return memo[state]
        
        return dp(0, 0, {})

    
"""
[7, 1, 5, 3, 6, 4]
-> 7 0 -7 | _ 0 0      

-> 1 0 -1 | _ 0 0
-> 5 1  4 | _ 0 0
-> 6 0 -6 | 4 0 -4 | 3 1 2 | _ 0 0
-> 

"""