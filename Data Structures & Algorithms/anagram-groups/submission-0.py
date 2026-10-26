class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        
        anagrams = defaultdict(list)
        result = list()

        for word in strs:
            letterFreq = [0] * 26
            for letter in word:
                letterFreq[ord(letter) - ord('a') ] += 1
            
            tupledWord = tuple(letterFreq)
            anagrams[tupledWord].append(word)


        for thing in anagrams:
            result.append(anagrams[thing])
        
        return result
