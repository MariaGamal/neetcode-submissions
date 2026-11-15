class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = {}
        l, r = 0, 0
        res = 0
        while r < len(s):
            if s[r] in freq:
                stop = freq[s[r]]
                while l <= stop:
                    del freq[s[l]]
                    l +=1
            freq[s[r]] = r
            res = max(res, r - l + 1)
            r +=1
        return res