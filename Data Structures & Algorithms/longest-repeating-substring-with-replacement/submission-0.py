class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        maxLength = 0
        letterFreq = [0] * 26

        l = 0

        for r in range(len(s)):
            letterFreq[ord(s[r]) - ord('A')] += 1
            mostFreqLetter = max(letterFreq)

            if  r - l + 1 - mostFreqLetter > k :
                letterFreq[ord(s[l]) - ord('A')] -= 1
                l += 1

            maxLength = max(maxLength, r - l + 1) 

        return maxLength   


