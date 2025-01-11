def anagrams(str1, str2):
    for c in str1:
        if c not in str2:
            return False
    for c in str2:
        if c not in str1:
            return False
    return True


print("test cases")
print(anagrams("listen", "silent")) 
print(anagrams("hello", "world"))

str1 = input("Enter the first string:  ") 
str2 = input("Enter the second string:  ")
print(f"The strings {str1} {str2} are anagrams : {anagrams(str1,str2)}")