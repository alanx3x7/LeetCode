class Solution:
    
    def maxArea(self, height: List[int]) -> int:

        i = 0
        j = len(height) - 1
        maxArea = 0

        while i < j:
            currentArea = min(height[i], height[j]) * abs(i - j)
            maxArea = max(maxArea, currentArea)

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1

        return maxArea

