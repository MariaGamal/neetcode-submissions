class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded
    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            j = i
            while j < len(s) and s[j] != "#":
                j += 1
            l = int(s[i:j])
            res.append(s[j+1:j+1+l])
            i+= 1 + j - i + l
        return res
        
