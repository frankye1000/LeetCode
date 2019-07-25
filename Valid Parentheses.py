"""Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true"""

s = "()[]}"
def Iscorrect(s):
    dic = {
        ']':'[',
        '}':'{',
        ')':'('
    }
    stack = [None]
    for i in s:
        if i in dic and dic[i]==stack[-1]:
            stack.pop()
        else:
            stack.append(i)

    # print(stack)
    if len(stack)==1:

        return True
    else:
        return False

print(Iscorrect(s))

