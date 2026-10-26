class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        index = []
        index.append(0)
        results = [0] * len(temperatures)

        for i in range(1, len(temperatures)):
            while index and temperatures[i] > temperatures[index[-1]]:
                results[index[-1]] = i - index[-1]
                index.pop()
            
            index.append(i)
        
        return results

        # 1 2

        # 1 

