'''

Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.


Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

'''

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        half_num = int(x/(x/2))

        num_sq = half_num*half_num

        while num_sq <= x:
            half_num += 1
            num_sq = half_num * half_num

        return half_num-1

# result = Solution.mySqrt(Solution(), 8)
# print(result)

result = Solution.mySqrt(Solution(), 4)
print(result)