def isPalindrome(word):
    i = 0
    word = word.lower()
    while(i < len(word) // 2 and isPalindrome):
        if(word[i] != word[len(word)-(i+1)]):
            return False
        i+=1
    return True
word = input("Type a word: ")
if(isPalindrome(word)):
    print("Yes, it's a palindrome.")
else: 
    print("No, it's not a palindrome.")
