"""
Escape Characters:

new_line  = '\n'

tab       = '\t'

backslash = '\\'

backspace = '\b'
"""

print("amina is an \n intelligent \t girl and \\ hard \bworker")

print("Hello, World! 	\U0001F600	") # 1

# grinning face
print("\U0001f600")
 
# grinning squinting face
print("\U0001F606")
 
# rolling on the floor laughing
print("\U0001F923")

def main():
    quote = "Hasta la vista, baby"
    first_word = quote[9:14]
    print(first_word)
    print(quote)

if __name__ == '__main__':
    main()


def main():
    quote = "Where is Gamora?"

    print(quote)
    quote = "Who" + quote[5:]
    print(quote) # who is Gamora?
    quote = "Why" + quote[3:]
    print(quote) # why is Gamora?
    

if __name__ == '__main__':
    main()


def main():
    # len(str) returns the length of the given string
    quote = 'Hakuna Matata'
    print('length of', quote, '=', len(quote))
    
    # ord(char) takes in a single character and returns the associated unicode
    # value


    print('unicode for \'A\':', ord('A'))
    print('unicode for \"a\":', ord('a'))
    print('unicode for 🥳:', ord('🥳'))
    print('unicode for \'$\':', ord('$'))
    print('unicode for \'好\':', ord('好'))

    word = "this is my book"

    word = word.replace(" ","").lower()
    print(word) # ['this', 'is', 'my', 'book']
    print(len(word))

    for i in range(len(word)):
        r = -1
        if word[i] == word[r]:
            

if __name__ == '__main__':
    main()