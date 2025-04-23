def encode(self, strs):
    res = ''
    for s in strs:
        res = str(len(s)) + '#' + s
    return res

def decode(self, strs):
    res = []
    i = 0
    while i < len(str):
        j = i
        
        while str[j] != '#':
            j+=1
        length = int(str[i:j])
        j+=1

        word = [str[j:j] + length]

        res.apped(word)
        i = j+length
    return res



