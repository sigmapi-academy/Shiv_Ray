# Write a function to replace all vowels in the string with '*'

def replaceVowelWithChar(st,ch='*'):
    newstr = '' # empty string 
    for character in st:
        if character in 'aeiouAEIOU':
            newstr += ch
        else:
            newstr += character 
    return newstr

# main code
st = input('Enter any sentence: ')
nst = replaceVowelWithChar(st)
print(nst)