"""Given a string S, we can transform every letter individually to be lowercase or uppercase to create
another string.  Return a list of all possible strings we could create.

Examples:
Input: S = "a1b2"
Output: ["a1b2", "a1B2", "A1b2", "A1B2"]

Input: S = "3z4"
Output: ["3z4", "3Z4"]

Input: S = "12345"
Output: ["12345"]"""

S = "3z4"
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

re = []

if S[0] in letters:
    re.append(S[0].lower())
    re.append(S[0].upper())
else:
    re.append(S[0])
# print(re)

# A = ['a', 'A']
def bineint(A, i):
    return [a + i for a in A]


def bineletter(A, l):
    ret = []
    for a in A:
        ret.append(a + l.lower())
        ret.append(a + l.upper())
    return ret


for i in S[1:]:
    if i in letters:
        re = bineletter(re, i)
    else:
        re = bineint(re, i)
print(re)

