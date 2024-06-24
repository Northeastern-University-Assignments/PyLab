# Welcome to Exercise 1!
# Let's calculate the factorial of a number.

def factorial(n):
if n < 0:
        raise ValueError("Error")  # Negative numbers do not have a factorial.
    # TODO: Implement the function to calculate the factorial of a number
    # Placeholder: return 1 if n == 0 else n * factorial(n - 1)
    pass

if __name__ == "__main__":
    import sys
    input_value = int(sys.stdin.read().strip())
    try:
        print(factorial(input_value))
    except ValueError as e:
        print(e)

# Example usage:
# print(factorial(5))   # Expected output: 120
# print(factorial(0))   # Expected output: 1
# print(factorial(-1))  # Expected output: Error