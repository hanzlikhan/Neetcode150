# Har oh character jo punctuation ae, una nu hatawana ae
PUNCTUATION = '.!?,-:;+()[]{}"\'<>/\\|@#$%^&*`~'

def delete_punctuation(string):
    '''
    Eh function string vichon punctuation hata ke navi string return karega.
    '''
    result = ''
    for char in string:
        if char not in PUNCTUATION:  # je character punctuation nai ae
            result += char           # taan ohnu result vich pa de
    return result


def get_word_counts(file_name):
    '''
    Eh function file padhega, punctuation hata ke har lafz gin'ke dictionary return karega.
    Keys = words, Values = count
    '''
    counts = {}  # dictionary jithon har word da count rakheya jaayega

    with open(file_name, 'r') as file:  # file open karo read mode vich
        for line in file:
            # punctuation hatao te lafz split karo
            words = delete_punctuation(line).split()

            for word in words:
                word = word.lower()  # sab words chhote kro (case insensitive)
                if word not in counts:
                    counts[word] = 1  # pehli vaar mila
                else:
                    counts[word] += 1  # already si, count vadhado

    return counts


def main():
    # Eh file da naam jithe words gin'ne ne
    print(get_word_counts('input.txt'))


# Program yahan se start honda ae
if __name__ == '__main__':
    main()
