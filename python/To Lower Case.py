#Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.
#
# Example1:
# Input: "Hello"
# Output: "hello"

# Example2:
# Input: "here"
# Output: "here"

# Example3:
# Input: "LOVELY"
# Output: "lovely"

alphabet = {"A":"a",
            "B":"b",
            "C":"c",
            "D":"d",
            "E":"e",
            "F":"f",
            "G":"g",
            "H":"h",
            "I":"i",
            "J":"j",
            "K":"k",
            "L":"l",
            "M": "m",
            "N": "n",
            "O": "o",
            "P": "p",
            "Q": "q",
            "R": "r",
            "S": "s",
            "T": "t",
            "U": "u",
            "V": "v",
            "W": "w",
            "X": "x",
            "Y": "y",
            "Z": "z"
            }
strings="Hello"
output=""
for i in range(len(strings)):
    if strings[i] in alphabet:
        output+=alphabet[strings[i]]
    else:
        output+=strings[i]

print(output)