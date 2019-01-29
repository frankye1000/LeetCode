"""You have a list of words and a pattern, and you want to know which words in words matches the pattern.

A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

(Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.)

Return a list of the words in words that match the given pattern.

You may return the answer in any order.



Example 1:

Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}.
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation,
since a and b map to the same letter."""

words = ["aabbcc", "aabbaa", "ddffdd"]
pattern = "vvnnvv"

count = 0
dic = {}
for i in pattern:
    if i not in dic:
        dic[i] = count
        count += 1
print(dic)
pattern_string = ''
for i in pattern:
    pattern_string += str(dic[i])
print(pattern_string)

output = []
for word in words:
    count_ = 0
    dic = {}
    for j in word:
        if j not in dic:
            dic[j] = count_
            count_ += 1

    word_string = ''
    for j in word:
        word_string += str(dic[j])

    if word_string == pattern_string:
        output.append(word)
print(output)