"""
There are N stations in  route, starting from 0 to N-1. A train moves from the first station (0)
to last station(N-1) in only forward direction. The cost of ticket between any two stations is
given, Find the minimum cost of travel from station 0 to station N-1.
"""
"""
First intuition how the cost of ticket is represented.
cost = [
    [0, 10, 75, 94],
    [-1, 0, 35, 50],
    [-1, -1, 0, 80],
    [-1, -1, -1, 0]
]
"""
def calculateMinCost(s, d):
    if s == d or s == d-1:
        return cost[s][d]
    minCost = cost[s][d]
    for i in range(s+1, d):
        temp_cost = calculateMinCost(s, i) + calculateMinCost(i, d)
        if temp < minCost:
            minCost = temp_cost
    return minCost
