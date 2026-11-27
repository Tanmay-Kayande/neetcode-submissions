class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        clean = "".join(char for char in s if char.isalnum())

        l, r = 0, len(clean) -1
        while l < r:
            if clean[l] != clean[r]:
                return False
            else:
                l += 1
                r -= 1
        return True