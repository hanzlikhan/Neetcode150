from typing import List

class Solution:
    # by keep count in the hashmap and sort to find 
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        # Count frequencies
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # Convert dictionary to list of (num, frequency) pairs
        freq_list = list(freq.items())

        # Sort the list based on frequency in descending order
        freq_sorted = sorted(freq_list, key=lambda x: x[1], reverse=True)

        # Pick top k elements
        result = []
        for i in range(k):
            result.append(freq_sorted[i][0])

        return result
    

#  by using heap to to find largest element ds

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        # Convert to list of tuples (num, freq)
        freq_list = list(freq.items())
        
        # Sort by frequency in descending order
        freq_list.sort(key=lambda x: x[1], reverse=True)
        
        # Extract top k elements
        return [freq_list[i][0] for i in range(k)]

