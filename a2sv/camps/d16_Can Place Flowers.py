class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                if i-1 >= 0 and flowerbed[i-1] == 1:
                    continue
                if i+1 < len(flowerbed) and flowerbed[i+1] == 1:
                    continue
                flowerbed[i] = 1
                n -= 1
        
        if n <= 0:
            return True
        return False