class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        myDict = {}
        monotonicStack = []
        
        for index in range(len(position)):
            myDict[position[index]] = speed[index]
        
        myDict = {pos:myDict[pos] for pos in sorted(myDict)}
        
        for pos in myDict:
            timeSpent = (target-pos) / myDict[pos]
            if not monotonicStack or monotonicStack[-1] > timeSpent:
                monotonicStack.append(timeSpent)
            else:
                while monotonicStack and monotonicStack[-1] <= timeSpent:
                    monotonicStack.pop()
                monotonicStack.append(timeSpent)
        
        return len(monotonicStack)