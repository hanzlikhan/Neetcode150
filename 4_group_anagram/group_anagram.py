from typing import List
from collections import defaultdict
# group anagram leetcode question 
def groupAnagrams(strs: List[str]) -> List[List[str]]:
    anagram_map = defaultdict(list)  # default value is an empty list

    for word in strs:
        # Sort word to find its "signature"
        sorted_word = ''.join(sorted(word))
        # Group the word using the sorted form
        anagram_map[sorted_word].append(word)

    # Return only the grouped values
    return list(anagram_map.values())

# Example
print(groupAnagrams(["act", "pots", "tops", "cat", "stop", "hat"]))
