class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        frequency = Counter(nums)
        output = []
        n = len(nums)
        for key in frequency:
            if frequency[key] > n/3:
                output.append(key)
                
        return output
    