# Welcome to Exercise 2!
# Time to check if a string is a palindrome.

def is_palindrome(s):
    # TODO: Implement the function to check if the string is a palindrome
    # Hint: A string is a palindrome if it reads the same forward and backward
    # Placeholder: return s == s[::-1]
    pass

if __name__ == "__main__":
    import sys
    input_value = int(sys.stdin.read().strip())
    print(is_palindrome(input_value))

# Example usage:
# print(is_palindrome("racecar"))  # Expected output: True
# print(is_palindrome("hello"))    # Expected output: False
# print(is_palindrome("Level"))    # Expected output: True
# print(is_palindrome("a"))        # Expected output: True