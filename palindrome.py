"""
assignment 4 palindrome
"""

def is_palindrome(value):
    if isinstance(value, str) != True:
        assert ValueError
    elif len(value) == 0:
        print("False")
    else:
        print("True")

