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
def test_step_3():
    """Testing Step 3  """
    palindrome.is_palindrome("a")
