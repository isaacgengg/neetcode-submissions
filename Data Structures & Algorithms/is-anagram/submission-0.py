class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sCount = defaultdict(int)
        tCount = defaultdict(int)

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            sCount[s[i]] += 1 
            tCount[t[i]] += 1
        
        return sCount == tCount
