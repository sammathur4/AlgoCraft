class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = [0] * len(spells)
        potions.sort()

        for i in range(len(spells)):
            # find the smallest value to reach in spells
            needed = success//spells[i] + bool(success % spells[i])

            l, r = 0, len(potions) # r should start with len(potions) to give a full range from 0 to len(potions) to l
            while l < r:
                mid = l + (r - l) // 2
                if potions[mid] < needed:
                    l = mid + 1
                else:
                    r = mid
                res[i] = len(potions) - l

        return res