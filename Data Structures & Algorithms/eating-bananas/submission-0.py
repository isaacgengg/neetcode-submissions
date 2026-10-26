class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def eat(k) -> int:
            hours = 0

            for pile in piles:
                hours += math.ceil(pile / k)

            return hours


        l = 1
        r = max(piles)

        while l < r:
            mid = (l + r) // 2
            if eat(mid) <= h:
                r = mid
            elif eat(mid) > h:
                l = mid + 1

        return l 


