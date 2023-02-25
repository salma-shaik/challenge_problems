'''

Given two binary strings a and b, return their sum as a binary string.



Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"


Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself. # so if the final result is 0, then just send it

10010011
    1011

'''
import math


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_len = str.__len__(a)
        b_len = str.__len__(b)

        if a_len < b_len:
            a = ('0'*(b_len-a_len))+a
        elif a_len > b_len:
            b = ('0' * (a_len - b_len)) + b

        sum_bin = list('0' *str.__len__(a))

        idx = -1
        carry = 0
        for i, j in zip(a[::-1],b[::-1]):
            i_var = int(i)
            j_var = int(j)
            if i_var+j_var+carry == 0:
                sum_bin[idx] = 0
                carry = 0
            elif i_var+j_var+carry == 1:
                sum_bin[idx] = 1
                carry = 0
            elif i_var+j_var+carry == 2:
                sum_bin[idx] = 0
                carry = 1
            elif i_var+j_var+carry == 3:
                sum_bin[idx] = 1
                carry = 1

            idx -= 1

        if carry == 1:
            sum_bin.insert(0,1)

        return ''.join(str(x) for x in sum_bin)

result = Solution.addBinary(Solution(), '11', '1')
print(result)

# result = Solution.addBinary(Solution(), '1010', '1011')
# print(result)

'''
Input: a = "1010", b = "1011"
Output: "10101"
'''


"""
TOP:
def addBinary(self, a: str, b: str) -> str:
        return format(int(a, base=2) + int(b, base=2), 'b')
"""