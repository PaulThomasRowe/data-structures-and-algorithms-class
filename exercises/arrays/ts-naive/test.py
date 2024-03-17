from solution.solution import Solution

solution_class = Solution()

def testSolution(nums: list[int], target: int, expected_indices: list[int]) -> bool:
    print(f"Test case: nums: {nums}, target: {target}, expected_indices: {expected_indices}") 
    try:
        resulting_indices = solution_class.indicesOfTwoNumbers(nums, target)
        if not len(resulting_indices) == 2:
            print(f"Expected 2 resulting indices. Found {len(resulting_indices)} indices.") 
        if not expected_indices[0] in resulting_indices:
                print(f"Did not find expected index of {expected_indices[0]}. Provided indices: {resulting_indices}")
        if not expected_indices[1] in resulting_indices:
                print(f"Did not find expected index of {expected_indices[1]}. Provided indices: {resulting_indices}")
        return True
    except Exception as error:
        print(error)
        return False


def testCase1():
    nums = [2,7,11,15]
    target = 9
    expected_indices = [1,0]
    result = testSolution(nums, target, expected_indices)

    if result:
        print("Passed Test Case 1")
    else:
        print("Failed Test Case 1")


def testCase2():
    nums = [3,2,4]
    target = 6
    expected_indices = [1,2]
    result = testSolution(nums, target, expected_indices)

    if result:
        print("Passed Test Case 2")
    else:
        print("Failed Test Case 2")

def testCase3():
    nums = [3,3]
    target = 6
    expected_indices = [0,1]
    result = testSolution(nums, target, expected_indices)

    if result:
        print("Passed Test Case 3")
    else:
        print("Failed Test Case 3")

testCase1()
testCase2()
testCase3()
