"""Given two strings representing two complex numbers.

You need to return a string representing their multiplication. Note i2 = -1 according to the definition.

Example 1:
Input: "1+1i", "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
Example 2:
Input: "1+-1i", "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i."""

a = '1+-1i'
b = '1+-1i'

al = a.split('+')
bl = b.split('+')

##實數部分
R = int(al[0]) * int(bl[0]) - int(al[1][:-1]) * int(bl[1][:-1])
##複數部分
C = int(al[0]) * int(bl[1][:-1]) + int(bl[0]) * int(al[1][:-1])

print(str(R) + '+' + str(C) + 'i')