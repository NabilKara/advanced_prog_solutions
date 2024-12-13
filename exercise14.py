word = input("Type a word: ")
FRAME_LEN = 30
if(len(word) >= 30) : print("lenght must be under 30")
else:
    len_first_part = (FRAME_LEN - len(word)) // 2
    for _ in range(len_first_part) :
        print("*",end='')
    print(word,end='')
    for _ in range(FRAME_LEN - (len_first_part + len(word))):
        print("*",end='')
