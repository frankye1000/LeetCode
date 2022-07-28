s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"

sp = s.split(" ")
spr = [i[::-1] for i in sp]
print(" ".join(spr))
