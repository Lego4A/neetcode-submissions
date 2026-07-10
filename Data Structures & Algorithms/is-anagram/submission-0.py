class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashtableS, hashtableT = {}, {}

        for i in range(len(s)):
            if s[i] not in hashtableS:
                hashtableS[s[i]] = 0
            if t[i] not in hashtableT:
                hashtableT[t[i]] = 0
            
            hashtableS[s[i]] += 1
            hashtableT[t[i]] += 1
        
        return hashtableS == hashtableT