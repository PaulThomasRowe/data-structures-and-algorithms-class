from solution.solution import Solution

solutionClass = Solution()

def test_solution(original_string: str, reversed_string: str) -> bool:
    try:
        result_string = solutionClass.reverse_string(original_string)
        if result_string == reversed_string:
            return True
        raise Exception('Expected output (' + expected_output + ') does not equal provided output (' + actual_output + ').')
    except Exception as error:
        print(error)
        return False

def test_case_1():
    original_string = "dog"
    reversed_string = "god"
    result = test_solution(original_string, reversed_string)
    if result:
        print('Passed Test Case 1')
    else:
        print('Failed Test Case 1')

def test_case_2():
    original_string = "blue stripes are blue"
    reversed_string = "eulb era sepirts eulb"
    result = test_solution(original_string, reversed_string)
    if result:
        print('Passed Test Case 2')
    else:
        print('Failed Test Case 2')

def test_case_3():
    original_string = "Just do it!"
    reversed_string = "!ti od tsuJ"
    result = test_solution(original_string, reversed_string)
    if result:
        print('Passed Test Case 3')
    else:
        print('Failed Test Case 3')

test_case_1()
test_case_2()
test_case_3()
