
# Write a program using a user defined function to check if a string is a palindrome or not.
# (A string is called a palindrome if it reads some backward as forward.
#  For example, Kanak is a palindrome.)

def checkPalindrome(st):
    sc = st.lower()
    return sc[::-1] == sc

# main code

word = input('Enter any word: ') 
print('Palindrome' if checkPalindrome(word) else 'Not Palindrome')