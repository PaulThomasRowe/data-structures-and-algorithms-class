from solution.solution import Solution

solution = Solution()

nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(f"nums: {nums}, k: {k}")
solution.maximumSubarray(nums,k)
