def valid_anagram(self, s, t):
    # if len(s) != len(t):
    #     return  False
    # return sorted(s) == sorted(t)


    count_s = {}
    count_t = {}

# count a frequency with the element from first string
    for ch in s:
        count_s[ch] = count_s.get(ch,0) + 1
# count a frequency wiht the element from the second string 
    for ch in t:
        count_t[ch] = count_t.get(ch,0) + 1
    
    return count_s == count_t
