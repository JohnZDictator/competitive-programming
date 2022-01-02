class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        monotonic_stack = []
        counter = 0
        for index, num_elem in enumerate(num):
            while monotonic_stack and counter < k and int(monotonic_stack[-1]) > int(num_elem):
                monotonic_stack.pop()
                counter += 1
            monotonic_stack.append(num_elem)
        while counter < k:
            counter += 1
            monotonic_stack.pop()
        if not monotonic_stack or max(monotonic_stack) == "0":
            return "0"
        return "".join(monotonic_stack).lstrip("0")