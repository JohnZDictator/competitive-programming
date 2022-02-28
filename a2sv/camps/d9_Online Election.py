import heapq

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.votes = {}
        self.maxVotes = []
        self.maxVote = 0
        self.maxPersons = -1
        
        for i in range(len(self.times)):
            if self.persons[i] in self.votes:
                self.votes[self.persons[i]] += 1
            else:
                self.votes[self.persons[i]] = 1
            
            if self.votes[self.persons[i]] >= self.maxVote:
                self.maxVote = self.votes[self.persons[i]]
                self.maxPersons = self.persons[i]
                self.maxVotes.append(self.maxPersons)
            else:
                self.maxVotes.append(self.maxPersons)
                
    def q(self, t: int) -> int:
        left = 0
        right = len(self.times)-1
        
        while left <= right:
            mid = left + (right-left)//2
            
            if self.times[mid] > t:
                right = mid-1
            else:
                left = mid+1
                best = mid
                
        return self.maxVotes[best]

    
    
    
# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)