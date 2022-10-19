from collections import Counter
from functools import cmp_to_key
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words = Counter(words)
        return sorted(words.keys(), 
                        key=cmp_to_key(
                                lambda a,b: (-1 if words[a] > words[b] else 1) 
                                            if words[a] != words[b] 
                                                else (-1 if a < b else 1)))[:k]
