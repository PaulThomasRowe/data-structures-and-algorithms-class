from solution.solution import Solution
solution = Solution()
inputValue = [1,2,3,4]
expectedValue = [24,12,8,6]
resultValue = solution.productExceptSelf(inputValue)
print(f"Expected Value: {expectedValue}, Actual Value: {resultValue}")

inputValue = [-1,1,0,-3,3]
expectedValue = [0,0,9,0,0]
resultValue = solution.productExceptSelf(inputValue)
print(f"Expected Value: {expectedValue}, Actual Value: {resultValue}")

