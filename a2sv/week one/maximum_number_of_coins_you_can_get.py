class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        loop = len(piles) // 3
        my_max_total_coins = 0
        my_max_coin_index = len(piles)-2
        
        sorted_piles = sorted(piles)
        
        for i in range(loop):
            my_max_total_coins += sorted_piles[my_max_coin_index] 
            my_max_coin_index -= 2
        return my_max_total_coins