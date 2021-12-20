class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        m = len(l)
        output = []
        for i in range(m):
            newNum = nums[l[i]:r[i]+1]
            sortedNewNum = sorted(newNum)
            arithmetic_difference = sortedNewNum[1]-sortedNewNum[0]
            if len(sortedNewNum) == 2:
                output.append(True)
                continue
            for j in range(1, len(sortedNewNum)-1):
                if sortedNewNum[j+1]-sortedNewNum[j] != arithmetic_difference:
                    output.append(False)
                    break
                elif j+2 == len(sortedNewNum):
                    output.append(True)
                    break
        return output
                