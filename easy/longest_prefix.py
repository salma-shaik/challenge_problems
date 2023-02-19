'''

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.

'''


def find_longest_prefix(str_list):
    if len(str_list) < 1 or len(str_list) > 200:
        return 'Too many list elements'

    if len(str_list) == 1:
        #[""]
        if str_list[0] == "":
            return ""
        #["a"]
        else:
            return str_list[0]

    # ["flower","flower","flower","flower"]
    if len(set(str_list)) == 1:
        return str_list[0]

    smallest_str = sorted(str_list, key=len)[0]

    i = 0
    j = 1


    # TypeError: descriptor '__len__' requires a 'str' object but received a 'unicode' error in leet code so had to explicitly
    # convert to str type wherever doing this
    # smallest_str_len = str.__len__(str(smallest_str))

    smallest_str_len = str.__len__(smallest_str)

    max_str = ""

    # AttributeError: 'list' object has no attribute 'copy'
    # so had to do str_list_copy = str_list[:]
    str_list_copy = str_list.copy()
    str_list_copy.remove(smallest_str)

    #["ab", "a"] hence <=
    while j <= smallest_str_len:
        count = 0
        check_str = smallest_str[i:j]
        # to not check the smallest elem against itself
        # removes in place
        for s in str_list_copy:
            if str.__len__(s)  > 200:
                return 'String too long'
            if s[i:j] == check_str:
                count += 1
        if count == (len(str_list)-1) and (str.__len__(check_str) >= str.__len__(max_str)):
            max_str = check_str
        j += 1

    return max_str


# res = find_longest_prefix(["flower", "flow", "flowing", "florence"])
# print(res)

# res = find_longest_prefix(["flower","flow","flight"])
# print(res)

# res = find_longest_prefix(["dog","racecar","car"])
# print(res)

# res = find_longest_prefix(["a"])
# print(res)

# res = find_longest_prefix([""])
# print(res)

# res = find_longest_prefix(["ab", "a"])
# print(res)

# res = find_longest_prefix(["flower","flower","flower","flower"])
# print(res)

# res = find_longest_prefix(["aac","acab","aa","abba","aa"])
# print(res)



def longestCommonPrefix(strs):
    ans = ""
    minLen = min([len(s) for s in strs])
    for i in range(minLen):
        prefixChar = list(set([s[i] for s in strs]))
        if len(prefixChar) != 1:
            break
        ans += prefixChar[0]
    return ans


# res = longestCommonPrefix(["flower", "flow", "flowing", "florence"])
# print(res)

# res = longestCommonPrefix(["flower","flow","flight"])
# print(res)

res = longestCommonPrefix(["aac","acab","aa","abba","aa"])
print(res)