# Example1:
# Input: ["flower","flow","flight"]
# Output: "fl"
#Example2:
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if not strs:
        return ''
    res = ''
    for i in range(len(strs[0])):
        for j in range(1, len(strs)):
            if i >= len(strs[j]) or strs[j][i] != strs[0][i]:
                return res
        res += strs[0][i]
    return res

