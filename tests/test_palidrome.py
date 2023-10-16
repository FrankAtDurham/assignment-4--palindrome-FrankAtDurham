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
def test_step_4():
    """Testing Step 4  """
    palindrome.is_palindrome("bb")
def test_step_5():
    """Testing Step 5 """
    palindrome.is_palindrome("abc")
def test_step_6():
    """Testing Step 6 """
    palindrome.is_palindrome("laval")
def test_step_7():
    """Testing Step 7 """
    palindrome.is_palindrome("toronto")
def test_step_8():
    """Testing Step 8 """
    palindrome.is_palindrome("Able was I ere I saw Elba")