class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        for i in s:
            freq[i] = freq.get(i, 0) + 1
        for i in t:
            freq[i] = freq.get(i, 0) - 1
        return all(value == 0 for value in freq.values())
        