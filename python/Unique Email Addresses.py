emails = ["test.email+alex@leetcode.com",
          "test.e.mail+bob.cathy@leetcode.com",
          "testemail+david@lee.tcode.com"]
# Output: 2
# Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails

## 把"+"位子記起來，後面的位子全部不要
retemp = []
for email in emails:
    local = email.split("@")[0]
    domain = email.split("@")[1]

    local = local.replace(".", "")
    indextemp = []
    for i, c in enumerate(local):
        if c == "+":
            indextemp.append(i)

    retemp.append(local[:indextemp[0]] + "@" + domain)

print(len(set(retemp)))