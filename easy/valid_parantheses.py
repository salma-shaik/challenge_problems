'''

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.


Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"  ([{}])
Output: true
Example 3:

Input: s = "(]"
Output: false


Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

'''


def isValid(s):

    bracks_dict = {')': '(', ']': '[', '}': '{'}
    ope_bracks = []

    for brack in s:
        if brack in bracks_dict:
            if ope_bracks & ope_bracks[-1] == bracks_dict[brack]:
                ope_bracks.pop()
            else:
                return False
        else:
            ope_bracks.append(brack)
    return True if not ope_bracks else False
    
    # while True:
    #     break_var = False
    #
    #     if not (('[]' in s) or ('()' in s) or ('{}' in s)):
    #         break_var = True
    #
    #     s = s.replace('[]', '')
    #     s = s.replace('()', '')
    #     s = s.replace('{}', '')
    #
    #     if break_var:
    #         break
    #
    # return len(s) == 0

"""
class Solution(object):
    def isValid(self, s):
        Map={")":"(","}":"{","]":"["}
        stack=[]
        for c in s:
            if c in Map:
                if stack and stack[-1]==Map[c]:
                   stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
"""

# res = isValid('()')
# print(res)

# res = isValid('()[]{}')
# print(res)

# res = isValid('([{}])')
# print(res)
#
# res = isValid('(]')
# print(res)

# res = isValid('([)]')
# print(res)

# res = isValid('(){}}{')
# print(res)

# res = isValid('[([]])')
# print(res)

res = isValid('(){}[]{[{([()])}]}')
print(res)
