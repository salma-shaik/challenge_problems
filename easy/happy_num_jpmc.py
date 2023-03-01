'''

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.



Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Example 2:

Input: n = 2
Output: false


Constraints:

1 <= n <= 231 - 1

'''

'''
Key is if result is 1 then return True or will end up in an endless cycle if result is 4
'''
class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 1:
            return True
        elif n == 0 or n == 4:
            return False
        try:
            num_str = str(n)
        except RecursionError:
            return False

        if num_str[0] == '1' and num_str[1:] == '0' * len(num_str[1:]):
            return True

        new_num = 0
        for num in num_str:
            new_num += int(num) * int(num)
        res = self.isHappy(new_num)
        return res

'''
In general, it is best to rewrite a function to use an iterative approach instead of increasing the recursion limit.
The “maximum recursion depth exceeded in comparison” error is raised when you try to execute a function that exceeds Python’s built in recursion limit. You can fix this error by rewriting your program to use an iterative approach or by increasing the recursion limit in Python.
'''
# res = Solution.isHappy(Solution(), 1000)
# print(res)

# res = Solution.isHappy(Solution(), 1)
# print(res)

# res = Solution.isHappy(Solution(), 0)
# print(res)

# res = Solution.isHappy(Solution(), 2)
# print(res)

# res = Solution.isHappy(Solution(), 12)
# print(res)

res = Solution.isHappy(Solution(), 19)
print(res)




'''
# SIMPLE SOLUTION - DON'T HAVE TO KNOW ANY COMPLEX MATH just that if the number is not
happy, then some 'sum' numbers might duplicate
TOP:
    def isHappy(self, n: int) -> bool:
        def sumofsquare(n):
            s = 0
            while n:
                s += (n % 10) ** 2
                n = n // 10
            return s
        d = set()

        while True:
            if n == 1:
                return True
            if n in d:
                return False
            d.add(n)
            n = sumofsquare(n)

'''