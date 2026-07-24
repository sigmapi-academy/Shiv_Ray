# Write a program with a user defined function to count the number of times a character 
# (passed as argument) occurs in a given string.

def charCount(ch, st):
    count = 0
    for character in st:
        if character == ch:
            count += 1
    return count

# main code
sent = input('Enter any sentence: ')
char = input('Enter any character to be searched: ')
count = charCount(char, sent)
print(f"Number of times character '{char}' occurs in the string: {count}")

c = sent.count(char)
print(f"Number of times character '{char}' occurs in the string: {c}")
