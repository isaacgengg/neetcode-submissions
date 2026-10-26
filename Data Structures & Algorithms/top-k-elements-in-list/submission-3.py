class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numFreq = defaultdict(int)
        result = [];

        for num in nums:
            numFreq[num] += 1
        
        for i in range(k):
            mostFreq = (max(numFreq, key = numFreq.get))
            result.append(mostFreq)
            numFreq[mostFreq] = 0

        return result
            