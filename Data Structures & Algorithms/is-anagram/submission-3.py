class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seen = {}
        for ch in s:
            if ch in seen:
                seen[ch] += 1
            else:
                seen[ch] = 1
        
        for ch in t:
            if ch not in seen:
                return False
            else:
                seen[ch] -= 1
        for v in seen.values():
            if v != 0:
                return False
        return True