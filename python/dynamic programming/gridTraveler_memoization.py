'''
Grid Traveler is a problem in which the number of different paths that can be taken to reach 
the bottom right corner of a matrix from top left corner.
'''

'''
Classical recursive implmentation with:
    - O(2^(n+m)) time complexity
    - O(n+m) space complexity
'''
# def gridTraveler(m, n):
#     if m == 1 and n == 1: return 1
#     if m == 0 or n ==0: return 0

#     return gridTraveler(m-1, n) + gridTraveler(m, n-1)

'''
Dynamic Programming Approach with memoization:
    - O(m*n) time complexity
    - O(m+n) space complexity
'''
def gridTraveler(m, n, memo = {}):
    key = str(m) + ',' + str(n)
    if key in memo: return memo[key]
    if m == 1 and n == 1: return 1
    if m == 0 or n == 0: return 0

    memo[key] = gridTraveler(m-1, n, memo) + gridTraveler(m, n-1, memo)
    return memo[key]

print(gridTraveler(1, 1))
print(gridTraveler(2, 3))
print(gridTraveler(3, 2))
print(gridTraveler(18, 18))