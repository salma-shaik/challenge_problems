'''

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?



Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step


Constraints:

1 <= n <= 45

'''

## Can either take 1 step or 2 steps

x = -1
num_ways = 0

class Solution:
    num_ways = 0
    def climbStairs(self, n: int) -> int:

        if n in [0, 1, 2]:
            return n

        temp_res = list()
        temp_res.append(1)
        temp_res.append(1)
        temp_res.append(2)

        for i in range(3, n+1):
            temp_res.append(temp_res[i-1] + temp_res[i-2])

        return temp_res[-1]

# result = Solution.climbStairs(Solution(), 1)
# print(result)

# result = Solution.climbStairs(Solution(), 2)
# print(result)

# result = Solution.climbStairs(Solution(), 3)
# print(result)
#
# result = Solution.climbStairs(Solution(), 4)
# print(result)

#
result = Solution.climbStairs(Solution(), 5)
print(result)


"""

    if n == 0:
        return 1
    
    if n < 0:
        return 0
    
    if n in util.mem:
        return util.mem[n]
    
    util.mem[n] = util(n-1) + util(n-2)
    return util.mem[n]
    

class Solution:
    def climbStairs(self, n: int) -> int:
        util.mem = {}
        return util(n)

"""