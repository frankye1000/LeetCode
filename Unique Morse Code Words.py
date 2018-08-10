morse={
"a":".-",
"b":"-...",
"c":"-.-.",
"d":"-..",
"e":".",
"f":"..-.",
"g":"--.",
"h":"....",
"i":"..",
"j":".---",
"k":"-.-",
"l":".-..",
"m":"--",
"n":"-.",
"o":"---",
"p":".--.",
"q":"--.-",
"r":".-.",
"s":"...",
"t":"-",
"u":"..-",
"v":"...-",
"w":".--",
"x":"-..-",
"y":"-.--",
"z":"--.."
}

words = ["gin", "zen", "gig", "msg"]
Output: 2

morsewords=[]
for num in range(len(words)):
    temp=""
    for i in range(len(words[num])):
        if words[num][i] in morse:
            temp+=morse[words[num][i]]
    morsewords.append(temp)
print(morsewords)

print(len(set(morsewords)))

