class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        n_char: list[int] = [0] * 26

        for i in range(len(s)):
            n_char[ord(s[i]) - ord('a')] += 1
            n_char[ord(t[i]) - ord('a')] -= 1
            
        for n in n_char:
            if n != 0:
                return False

        return True
        