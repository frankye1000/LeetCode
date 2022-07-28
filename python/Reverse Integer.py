"""
Example1:
Input: 123
Output: 321
Example2:
Input: -123
Output: -321
Example3:
Input: 120
Output: 21
"""
class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        i=str(x)
        while i.endswith("0"):
            i = i[:-1]
        print(i)
        if i.startswith("-"):
            if len(i) != 0 and (-int(i[-1:0:-1])&-0x80000000 == -2147483648): 
                return -int(i[-1:0:-1])
            else:
                return 0
        else:
            if len(i) != 0 and (int(i[::-1])&0x7fffffff==int(i[::-1])):
                return int(i[::-1])
            else:
                return 0
