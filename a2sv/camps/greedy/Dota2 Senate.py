class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant = collections.deque()
        dire = collections.deque()
        
        m = len(senate)
        for idx in range(m):
            if senate[idx] == "R":
                radiant.append(idx)
            elif senate[idx] == "D":
                dire.append(idx)
        
        while radiant and dire:
            r = radiant.popleft()
            d = dire.popleft()
            
            if r < d:
                radiant.append(r + len(senate))
            elif r > d:
                dire.append(d + len(senate))
                
        if radiant:
            return "Radiant"
        return "Dire"