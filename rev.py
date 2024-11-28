def main():
    word=input("inter a word  ")
    print("the veversed word is ",reversed_word(word))


def reversed_word(word):
    reverse=""
    for i in word:
        reverse=i+reverse
    return reverse    
main()
