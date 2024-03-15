class helper:
    n = 38
    nums = [0]*n

    def tribo(self, k):
        if k == 0: return 0
        if self.nums[k]!=0:
            return self.nums[k]

        self.nums[k] = self.tribo(k-1) + self.tribo(k-2) + self.tribo(k-3)
        return self.nums[k]

    def __init__(self):
        self.nums[1] = 1
        self.nums[2] = 1
        self.tribo(self.n-1)

class Solution:
    t= helper()
        
    def tribonacci(self, n: int) -> int:
        return Solution.t.nums[n]

        

        