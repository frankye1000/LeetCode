import re
S = "Test1ng-Leet=code-Q!"
S = [i for i in S]
#Output: "Qedo1ct-eeLg=ntse-T!"

i, j = 0, len(S)-1

while i < j:
    fi = re.findall("[a-zA-Z]+", S[i])
    bj = re.findall("[a-zA-Z]+", S[j])
    if len(fi) > 0 and len(bj) > 0:
        S[i], S[j] = S[j], S[i]
        i += 1
        j -= 1
    if len(fi) > 0 and len(bj) == 0:
        j -= 1
    if len(fi) == 0 and len(bj) > 0:
        i += 1
    if len(fi) == 0 and len(bj) == 0:
        i += 1
        j -= 1
R = ''
for i in S:
    R += i
print(R)