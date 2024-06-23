import unittest
from exercise2 import is_palindrome

class TestPalindromeChecker(unittest.TestCase):
    def test_palindrome_basic(self):
        """Tests if a simple palindrome ("racecar") is correctly identified."""
        self.assertTrue(is_palindrome("racecar"), "racecar should be a palindrome")

    def test_palindrome_mixed_case(self):
        """Tests if a palindrome with mixed case ("Level") is correctly identified."""
        self.assertTrue(is_palindrome("Level"), "Level should be a palindrome, ignoring the case")

    def test_palindrome_non_palindrome(self):
        """Tests if a non-palindrome string ("hello") is correctly identified as not a palindrome."""
        self.assertFalse(is_palindrome("hello"), "hello should not be a palindrome")

    def test_palindrome_single_character(self):
        """Tests if a single-character string ("a") is considered a palindrome."""
        self.assertTrue(is_palindrome("a"),"a single character should be a palindrome")

if __name__ == "__main__":
    unittest.main()