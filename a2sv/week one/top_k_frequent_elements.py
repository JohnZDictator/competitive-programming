class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numFrequency = {}
        output = []
        
        for i in range(len(nums)):
            if str(nums[i]) in numFrequency:
                numFrequency[str(nums[i])] += 1
            else:
                numFrequency[str(nums[i])] = 1
        
        for j in range(k):
            max_num = max(numFrequency, key=numFrequency.get)
            output.append(max_num)

            numFrequency.pop(max_num)
        return output