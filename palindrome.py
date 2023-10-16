"""
assignment 4 palindrome
"""
from collections import deque

def is_palindrome(value):
    if isinstance(value, str) != True:
        assert ValueError
    elif len(value) == 0:
        print("False")
    else:
        value_lower = value.lower()         # need to change everything to lower case for comparison
        original = deque(value_lower)
        pal = deque()
        for val in original:
            pal.appendleft(val)
        #print(original)     # for debugging
        #print(pal)          # for debugging
        original_list = list(original)
        pal_list = list(pal)

        if pal_list == original_list:
            print("True")
        else:
            print("False")

