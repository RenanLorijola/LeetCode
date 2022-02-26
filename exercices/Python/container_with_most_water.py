class Solution:
    def maxArea(self, height) -> int:
        maxArea = 0
        length = len(height)
        start = 0
        end = length-1
        while start < end:
            width = end - start
            area = width * height[start]
            if height[start] < height[end]:
                start+=1
            else:
                area = width * height[end]
                end -=1
            maxArea = maxArea if maxArea > area else area
        return maxArea

solution = Solution()
print(solution.maxArea([1,8,6,2,5,4,8,3,7]))