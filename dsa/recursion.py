# Factorial

def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


# Fibonacci Sequence
def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)

