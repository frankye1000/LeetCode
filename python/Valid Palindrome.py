"""Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false"""

def Ispalindrome(s):
    s3 = [i.lower() for i in s if i.isalnum()]
    if len(s3) == 0:
        return True
    elif len(s3) == 1:
        return True
    else:
        iterr = int(len(s3)/2)

        for i in range(iterr):
            if s3[i]!=s3[-(i+1)]:
                return False
        return True

s = "A man, a plan, a canal: Panama"
# s = ",."
# s = "race a car"
# s = "OP"
print(Ispalindrome(s))