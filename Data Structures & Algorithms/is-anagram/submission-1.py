class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        lettersS, lettersT = {}, {}

        for i in range(len(s)):
            if s[i] not in lettersS:
                lettersS[s[i]] = 0
            if t[i] not in lettersT:
                lettersT[t[i]] = 0
            lettersS[s[i]] += 1
            lettersT[t[i]] += 1
        
        return lettersS == lettersT