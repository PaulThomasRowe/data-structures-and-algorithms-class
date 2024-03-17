class Solution:
    def indicesOfTwoNumbers(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        length = len(nums)
        for i in range(0, length):
            remaining = target - nums[i]
            if remaining in seen:
                corresponding_index = seen[remaining]
                return [corresponding_index, i]
            seen[nums[i]] = i
