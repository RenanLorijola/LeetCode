class Solution:
    def twoSum(self, nums, target: int):
        dictionary = {}
        for i, k in enumerate(nums):
            pair = target - k
            if pair in dictionary:
                return [dictionary[pair], i]
            else:
                dictionary[k] = i

solution = Solution()
print(solution.twoSum([2,7,11,15], 9))