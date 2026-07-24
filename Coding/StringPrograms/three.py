# Write a program to input a sentence and reverse each word.

# Input: Shiv is learning how to code
# Output: vihS si gninrael who ot edoc

def reverseWord(word):
    return word[::-1]

def reverseEachWord(sent):
    newstr = ''
    for w in sent.split():
        newstr += reverseWord(w) + ' '
    return newstr

# main code
sent = input('Enter any sentence: ')
print(reverseEachWord(sent))