def reverse_string(input_string):
    reversed_str = ""
    for char in input_string:
        reversed_str = char + reversed_str
    return reversed_str

# Test the function
original_string = "hello"
reversed_string = reverse_string(original_string)
print("Original:", original_string)
print("Reversed:", reversed_string)
