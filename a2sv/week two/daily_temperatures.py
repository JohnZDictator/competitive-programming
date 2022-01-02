class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        monotonic_stack = []
        output = [0] * len(temperatures)
        for index, temp in enumerate(temperatures):
            if not monotonic_stack or monotonic_stack[-1][1] > temp:
                monotonic_stack.append([index, temp])
            else:
                while monotonic_stack and monotonic_stack[-1][1] < temp:
                    output[monotonic_stack[-1][0]] = index - monotonic_stack[-1][0]
                    monotonic_stack.pop()
                monotonic_stack.append([index, temp])
        return output