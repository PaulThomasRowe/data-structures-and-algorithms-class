from solution.solution import Solution

solution = Solution()

def testSolution(input: list[int], expected_result: int) -> bool:
	actual_result = solution.findMaximumSubarray(input)
	print(f"Finding maximum subarray for {input}")
	if (expected_result == actual_result):
		print(f"Passed, Expected result: {expected_result}, Actual result: {actual_result}")
	else:
		print(f"Failed, Expected result: {expected_result}, Actual result: {actual_result}")

print("Test Case 1")
testSolution([-2,1,-3,4,-1,2,1,-5,4],6)

print("Test Case 2")
testSolution([1],1)

print("Test Case 3")
testSolution([5,4,-1,7,8],23)
