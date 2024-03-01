class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        k,s=0,0
        for i in gain:
            k+=i
            s=max(s,k)
        return s
