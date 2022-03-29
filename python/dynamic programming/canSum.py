# def canSum(targetSum, numbers):
    # if targetSum == 0: return True
    # if targetSum < 0: return False

    # for num in numbers:
    #     remainder = targetSum - num
    #     if canSum(remainder, numbers) == True: return True
    
    # return False
class Solution:
    def __init__(self):
        self.memo = {}

    def canSum(self, targetSum, numbers, memo = {}):
        if not memo:
            self.memo = {}
        if targetSum in self.memo: return self.memo[targetSum]
        if targetSum == 0: return True
        if targetSum < 0: return False

        for num in numbers:
            remainder = targetSum - num
            if self.canSum(remainder, numbers, self.memo) == True: 
                self.memo[targetSum] = True
                return True

        self.memo[targetSum] = False
        return False

if __name__ == '__main__':
    s = Solution()
    print('1: ', s.canSum(7, [2,3]))
    print('2: ', s.canSum(7, [2,4]))
    print('3: ', s.canSum(300, [7, 14]))