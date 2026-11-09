class Solution:

    def encode(self, strs: List[str]) -> str:
        
        encoded = ""
        for i in strs:
            encoded += f"{len(i)}#{i}"
        return encoded

    def decode(self, s: str) -> List[str]:
        i = 0 
        res = []
        
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            word_len = int(s[i:j])
            res.append(s[j+1: j+1+word_len])
            i = j+1+word_len
        return res