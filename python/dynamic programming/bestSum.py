def bestSum(targetSum, numbers, memo):
    if targetSum in memo:
        return memo[targetSum]

    if targetSum == 0:
        return []
    if targetSum < 0:
        return None

    memo[targetSum] = None
    for num in numbers:
        rem = targetSum - num
        arr = bestSum(rem, numbers, memo)
        if arr != None:
            arr.append(num)
            if memo[targetSum] == None or len(arr) < len(memo[targetSum]):
                memo[targetSum] = arr
    return memo[targetSum]

print(bestSum(7, [2,3,4,7], {}))
print(bestSum(7, [2,3,4], {}))
print(bestSum(7, [2,4], {}))
print(bestSum(300, [7, 14], {}))


# def bestSum(targetSum, numbers):
#     if targetSum == 0:
#         return []
#     if targetSum < 0:
#         return None

#     shortestCombination = None
#     for num in numbers:
#         rem = targetSum - num
#         arr = bestSum(rem, numbers)
#         if arr != None:
#             arr.append(num)
#             if shortestCombination == None or len(arr) < len(shortestCombination):
#                 shortestCombination = arr         
    
#     return shortestCombination

# print(bestSum(7, [2,3,4,7]))
# print(bestSum(7, [2,3,4]))
# print(bestSum(7, [2,4]))
# print(bestSum(300, [7, 14]))

# Time complexity: O(n^m)
# Space complexity: O(m)