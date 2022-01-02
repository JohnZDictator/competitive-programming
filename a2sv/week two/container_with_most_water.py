class Solution:
    def maxArea(self, height: List[int]) -> int:
        start, end = 0, len(height)-1
        areas = []
        while start < end:
            areas.append( min(height[start],height[end]) * (end-start))
            if height[start] <= height[end]:
                start += 1
            elif height[start] > height[end]:
                end -= 1
        return max(areas)