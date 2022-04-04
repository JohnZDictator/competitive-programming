class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        scoreDict = {"a": a, "b": b, "c": c}
        
        count = 0
        while len(scoreDict) > 1:
            sortedScore = sorted(list(scoreDict.items()), key=lambda x: x[1])
            
            min_key = sortedScore[0][0]
            scoreDict[min_key] -= 1
            
            max_key = sortedScore[-1][0]
            scoreDict[max_key] -= 1
            
            if scoreDict[min_key] == 0:
                scoreDict.pop(min_key)
            if scoreDict[max_key] == 0:
                scoreDict.pop(max_key)
        
            count += 1
        return count