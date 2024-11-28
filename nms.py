def main ():
    word=input("inter a word: ")
    print(num_word(word))

def num_word(word):
    count=0
    for char  in word:
        count = count +1

    return count 

main()