'''

Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


Constraints:

-2^31 <= x <= 2^31 - 1

'''

import math

def palindrome_chk(num):
    # convert to a string coz can have negative sign
    num_str = str(num)

    if num < math.pow(2,-31) or num > (math.pow(2, 31)-1):
        return 'Invalid Number'

    num_str_rev = num_str[::-1]

    if num_str == num_str_rev:
        return True
    else:
        return False

# res = palindrome_check(math.pow(2,32))
# print(res)

# res = palindrome_check(121)
# print(res)
#
# res = palindrome_check(-121)
# print(res)
#
# res = palindrome_check(10)
# print(res)


def palindrome_check(num):
    # convert to a string to accommodate negative sign
    return str(num) == str(num)[::-1]

# res = palindrome_check(10)
# print(res)

# res = palindrome_check(-121)
# print(res)

res = palindrome_check(121)
print(res)