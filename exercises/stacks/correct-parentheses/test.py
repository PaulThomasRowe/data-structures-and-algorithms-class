from solution.solution import Solution

solution = Solution()

#Test Case 1
input = "()"
expectedOutput = True
actualOutput = solution.isCorrect(input)
if (expectedOutput == actualOutput):
    print("Test Case 1 Passed!")
else:
    print(f"Test Case 1 Failed, Expected: {expectedOutput}, Actual: {actualOutput}")

#Test Case 2
input = "()[]{}"
expectedOutput = True
actualOutput = solution.isCorrect(input)
if (expectedOutput == actualOutput):
    print("Test Case 2 Passed!")
else:
    print(f"Test Case 2 Failed, Expected: {expectedOutput}, Actual: {actualOutput}")

#Test Case 3
input = "(]"
expectedOutput = False
actualOutput = solution.isCorrect(input)
if (expectedOutput == actualOutput):
    print("Test Case 3 Passed!")
else:
    print(f"Test Case 3 Failed, Expected: {expectedOutput}, Actual: {actualOutput}")
