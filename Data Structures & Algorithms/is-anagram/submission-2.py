class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dictS, dictT = {}, {}

        for i in range(len(t)):
            if s[i] not in dictS:
                dictS[s[i]] = 0
            if t[i] not in dictT:
                dictT[t[i]] = 0
            dictS[s[i]] += 1
            dictT[t[i]] += 1
        
        return dictS == dictT