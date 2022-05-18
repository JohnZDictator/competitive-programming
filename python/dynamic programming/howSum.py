# memoized
def howSum(targetSum, numbers, memo):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return []
    if targetSum < 0:
        return None

    for num in numbers:
        rem = targetSum - num
        memo[targetSum] = howSum(rem, numbers, memo)
        if memo[targetSum] != None:
            memo[targetSum].append(num)
            return memo[targetSum]
    memo[targetSum] = None
    return None

print(howSum(7, [2,3,4,7], {}))
print(howSum(7, [4,3,2,7], {}))
print(howSum(7, [2,4], {}))
print(howSum(300, [7,14], {}))

# Time complexity: O(n*m)
# Space complexity: O(m)

# def howSum(targetSum, numbers):
#     if targetSum == 0:
#         return []
#     elif targetSum < 0:
#         return None
    
#     for num in numbers:
#         remainder = targetSum - num
#         arr = howSum(remainder, numbers)
#         if arr != None:
#             arr.append(num)
#             return arr
#     return None

# print(howSum(7, [2,3,4,7]))
# print(howSum(7, [4,3,2,7]))
# print(howSum(7, [2,4]))
# print(howSum(300, [7,14]))

# n = numbers.length, m = targetSum
# Time complexity: O(n^m)
# The base is the number of branches at each depth which is len(numbers)
# The exponent is the depth of the tree as long as targetSum > 0
# Space complexity: O(m)
# by both the recursive call and the array len returned