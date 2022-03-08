class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        output = -1
        
        while left <= right:
            mid = left + (right-left)//2
            
            counter = 0
            weightCapacity = 0
            daysToShip = 0
            while counter < len(weights):
                weightCapacity += weights[counter]
                
                if weightCapacity > mid:
                    daysToShip += 1
                    weightCapacity = weights[counter]
                counter += 1
            
            if 0 < weightCapacity:
                daysToShip += 1
            
            
            if daysToShip > days:
                left = mid+1
            else:
                right = mid-1
                output = mid
        
        return output