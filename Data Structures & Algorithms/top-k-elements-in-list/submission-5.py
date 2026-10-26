class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # numFreq = defaultdict(int)
        # result = [];

        # for num in nums:
        #     numFreq[num] += 1
        
        # for i in range(k):
        #     mostFreq = (max(numFreq, key = numFreq.get))
        #     result.append(mostFreq)
        #     numFreq[mostFreq] = 0

        # return result
        numFreq = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            numFreq[num] += 1
        for num, count in numFreq.items():
            freq[count].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        

