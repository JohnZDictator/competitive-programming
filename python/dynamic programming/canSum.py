# Memoized
def canSum(targetSum, numbers, memo={}):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return True
    elif targetSum < 0:
        return False
    
    for num in numbers:
        targetSum = targetSum - num
        if canSum(targetSum, numbers, memo) == True:
            memo[targetSum] = True
            return True
    memo[targetSum] = False
    return False

print(canSum(7, [2,3,4,7]))
print(canSum(7, [2,4]))
print(canSum(500, [7, 14]))

# Time Complexity: O(n*m)
# Space Complexity: O(m)

# Brute Force
# def canSum(targetSum, numbers):
#     if targetSum == 0:
#         return True
#     elif targetSum < 0:
#         return False

#     for num in numbers:
#         targetSum = targetSum - num
#         if canSum(targetSum, numbers) == True:
#             return True
#     return False

# print(canSum(7, [2,3,4,7]))
# print(canSum(7, [2,3,4]))
# print(canSum(500, [7,14]))

# Time complexity: O(n^m) 
# The base is the branch factor which is the len(numbers)
# The exponent is the depth of the tree, which is targetSum, 
# since we go deeper as long as targetSum > 0
# Space complexity: O(m)
# The recursive call is going to be called again again as lon as the targetSum > 0