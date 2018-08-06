# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"

S = "bbaa"
T = "aba"

t_index=[]
for i in range(len(S)):
    if S[i] in T:
        t_index.append(i)
# print(t_index)
t_te=[]
for j in range(len(t_index)-len(T)+1):
    temp=[]
    for k in t_index[j:j+len(T)]:
        temp.append([k,S[k]])
    # print(temp)



    if len(set([l[1] for l in temp]))==len(set(T)):

        diff = temp[-1][0]-temp[0][0]
        t_te.append([diff,temp])
try:
    f = sorted(t_te, key=lambda x:x[0])[0][1]
    print(S[f[0][0]:f[-1][0]+1])
except:
    print("except")
##################################################################
## 正解
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        count = len(t)
        minileft = 0
        miniSize = len(s) + 1
        left = 0
        cmap1 = {}
        cmap2 = {}
        for c in t:
            if c not in cmap1:
                cmap1[c] = 1
                cmap2[c] = 1
            else:
                cmap1[c] += 1
                cmap2[c] += 1

        for right in range(len(s)):
            if s[right] in cmap1:
                cmap2[s[right]] -= 1
                if cmap2[s[right]] >= 0:
                    count -= 1
                if count == 0:
                        while True:
                            if s[left] in cmap2:
                                if cmap2[s[left]] < 0:
                                    cmap2[s[left]] += 1
                                else:
                                    break
                            left += 1

                        if right - left + 1 < miniSize:
                            minileft = left
                            miniSize = right - minileft + 1

        if miniSize < len(s) + 1:
            return s[minileft:minileft + miniSize]
        else:
            return ''
