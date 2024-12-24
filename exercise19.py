words = []
word = ""
while(not words.__contains__(word)):
    if(word!= "") :
        words.append(word)
    word = input("Enter a word: ").strip()
def write_list_to_file(list, filename):
    try:
        with open(filename, 'w') as file:
            file.write(' '.join(list) + '\n')
        print(f"Successfully wrote unique words to '{filename}'.")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

print(f"You typed {len(words)} unique words")  
words.sort() # to display words alphabitically
print(f"list : {words}")
# for case-insensitivity we just use words.__contains__(word).lower()
# total words : we just add to len(words) because we exit as soon as we encounter a duplicate
decision = input("Do you want to save the unique words to a file : [y/n]")
if(decision.lower() == "y"):
    filename = input("Enter a file path : ")
    write_list_to_file(words,filename)
