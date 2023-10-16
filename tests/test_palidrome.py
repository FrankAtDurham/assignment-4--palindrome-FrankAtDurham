"""
test module for palindrome
"""
import pytest
import sys
sys.path.append("assign4PalindromeFrankAtDurham")
import palindrome

def test_step_1():
    """Testing Step 1  """
    palindrome.is_palindrome(None)
def test_step_2():
    """Testing Step 2  """
    palindrome.is_palindrome("")
