class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]
            print(f"Prefix: {prefix[i]} = {prefix[i-1]} * {nums[i-1]}")
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
            print(f"Suffix: {suffix[i]} = {prefix[i+1]} * {nums[i+1]}")
        answer = [prefix[i] * suffix[i] for i in range(n)]
        return answer
