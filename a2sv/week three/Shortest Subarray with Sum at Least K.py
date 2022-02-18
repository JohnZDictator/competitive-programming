class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # minSubLen -> stores min length of subarray that whose sum is >= (at least) k
        # if the sum of the subarray is never going to be greater than k, then return -1
        
        minSubLen = len(nums)+1
        prefixSum = [0] * (len(nums)+1)
        indexDeque = collections.deque()
        
        for i in range(len(nums)+1):
            prefixSum[i] = prefixSum[i-1] + nums[i-1]
        
        
        for i in range(len(prefixSum)):
            while indexDeque and prefixSum[i] - prefixSum[indexDeque[0]] >= k:
                minSubLen = min(minSubLen, i-indexDeque.popleft())
            while indexDeque and prefixSum[i] < prefixSum[indexDeque[-1]]:
                indexDeque.pop()
            indexDeque.append(i)
        
        return minSubLen if minSubLen != len(nums)+1 else -1