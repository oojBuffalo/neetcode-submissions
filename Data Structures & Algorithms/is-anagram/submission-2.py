class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        chars: dict[str,int] = {}

        for c in s:
            if c in chars:
                chars[c] += 1
            else:
                chars[c] = 1

        for c in t:
            if c not in chars:
                return False
            else:
                chars[c] -= 1
            

        return sum(abs(c) for c in chars.values()) == 0

        