s = "laetcudi"
# Output: "leotcede"
vowel = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
s = [_ for _ in s]
print(s)

indexx = [i for i, v in enumerate(s) if v in vowel][::-1]
values = [v for i, v in enumerate(s) if v in vowel]


for i in range(len(indexx)):
    s[indexx[i]] = values[i]

re=""
for i in s:
    re+=i
print(re)
