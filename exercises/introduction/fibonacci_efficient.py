def calculate_fibonacci_sequence_number(fibonacci_sequence_numbers: dict[int, int], n: int) -> int:
    if n <= 2:
        return 1
    fibonacci_sequence_number = fibonacci_sequence_numbers.get(n)
    if fibonacci_sequence_number is not None:
        return fibonacci_sequence_number
    fibonacci_sequence_number = (calculate_fibonacci_sequence_number(fibonacci_sequence_numbers, n-2) +
                                 calculate_fibonacci_sequence_number(fibonacci_sequence_numbers, n-1))
    fibonacci_sequence_numbers[n] = fibonacci_sequence_number
    return fibonacci_sequence_number


def print_input_and_result(sequence_number: int, fibonacci_sequence_number: int) -> None:
    print(f"The fibonacci sequence number of {sequence_number} is {fibonacci_sequence_number}.")


fibonacci_sequence_numbers: dict[int, int] = {}

sequence_number = 5
fsn = calculate_fibonacci_sequence_number(fibonacci_sequence_numbers, sequence_number)
print_input_and_result(sequence_number, fsn)

sequence_number = 18
fsn = calculate_fibonacci_sequence_number(fibonacci_sequence_numbers, sequence_number)
print_input_and_result(sequence_number, fsn)
