class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        monotonic_dict = {}
        monotonic_stack = []
        output = []
        
        for index, num in enumerate(nums2):
            if len(monotonic_stack) == 0:
                monotonic_stack.append(num)
                monotonic_dict[monotonic_stack[-1]] = -1
            elif monotonic_stack[-1] > num:
                monotonic_stack.append(num)
                monotonic_dict[monotonic_stack[-1]] = -1
            elif monotonic_stack[-1] < num:
                while monotonic_stack and monotonic_stack[-1] < num:
                    monotonic_dict[monotonic_stack[-1]] = num 
                    monotonic_stack.pop()
                monotonic_stack.append(num)
                monotonic_dict[num] = -1
        
        for num in nums1:
            output.append(monotonic_dict[num])
        return output
       
    
    
    
    
    
    
        # output = []
        # for num in nums1:
        #     index = nums2.index(num)
        #     for j in range(index, len(nums2)):
        #         if num < nums2[j]:
        #             output.append(nums2[j])
        #             break
        #         elif j == len(nums2)-1 :
        #             output.append(-1)
        # return output