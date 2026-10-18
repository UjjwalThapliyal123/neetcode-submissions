from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # DICT TO MAP CHAR COUNT
        anagrams = defaultdict(list)

        for s in strs:
            # creating a frequency array of size 26 for "a" through "z"
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
        # using the tuple of counts as a tuple is hashable in python
            anagrams[tuple(count)].append(s)
        return list(anagrams.values())



