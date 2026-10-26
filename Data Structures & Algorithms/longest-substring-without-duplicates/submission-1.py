class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        maxLength = 0
        seenLetters = set()  

        l = 0

        for r in range(len(s)):
            while s[r] in seenLetters:
                seenLetters.remove(s[l])

                l += 1
            
            seenLetters.add(s[r])
            maxLength = max(maxLength, r - l + 1)
        
        return maxLength
    
