cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
# Output:
# ["901 mail.com",
# "50 yahoo.com",
# "900 google.mail.com",
# "5 wiki.org",
# "5 org",
# "1 intel.mail.com",
# "951 com"]

dic = {}
for c in cpdomains:
    l = c.split(" ")
    number = int(l[0])
    ll = l[1].split(".")[::-1]
    print(ll)
    pp = ''
    for i in ll:
        pp = i + "." + pp
        # print(pp)
        if pp not in dic:
            dic[pp] = number
        else:
            dic[pp] += number

re = [str(dic[key]) + " " + key.strip(".") for key in dic]
print(re)



