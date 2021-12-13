class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        result = []
        #1 bubble sort
        # for i in range(len(nums)):
        #     for j in range(len(nums)-1):
        #         if nums[j] > nums[j+1]:
        #             nums[j], nums[j+1] = nums[j+1], nums[j]
        #2 insertion sort
        # for i in range(len(nums)-1):
        #     for j in range(i+1, 0, -1):
        #         if nums[j] < nums[j-1]:
        #             nums[j], nums[j-1] = nums[j-1], nums[j]
        #3 selection sort   
        for i in range(len(nums)):
            min_element = nums[i]
            for j in range(i+1, len(nums)):
                if min_element > nums[j]:
                    min_element, nums[j] = nums[j], min_element
            nums[i] = min_element
        #4 counting sort
#         max_num = nums[0]
#         for j in range(len(nums)):
#             if max_num < nums[j]:
#                 max_num = nums[j]
#         frequency_index = [0 for _ in range(max_num)]
#         for i in range(len(nums)):
#             frequency_index[nums[i]-1] += 1
#         print(frequency_index)
#         for n in range(len(frequency_index)):
            
        result = [x for x in range(len(nums)) if target == nums[x]]
        # for x in range(len(nums)):
        #     if target == nums[x]:
        #         result.append(x)
        return result