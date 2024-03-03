def calculate_fibonacci_sequence_number(n):
    if n <= 2:
        return 1
    fibonacci_sequence_number = calculate_fibonacci_sequence_number(n-2) + calculate_fibonacci_sequence_number(n-1)
    return fibonacci_sequence_number


def print_input_and_result(sequence_number: int, fibonacci_sequence_number: int) -> None:
    print(f"The fibonacci sequence number of {sequence_number} is {fibonacci_sequence_number}.")


sequence_number = 5
fsn = calculate_fibonacci_sequence_number(sequence_number)
print_input_and_result(sequence_number, fsn)

sequence_number = 18
fsn = calculate_fibonacci_sequence_number(sequence_number)
print_input_and_result(sequence_number, fsn)
