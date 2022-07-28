# S = "()))(("
S = "((())"
# Output: 4
while "()" in S:
    S = S.replace("()","")
print(S)
