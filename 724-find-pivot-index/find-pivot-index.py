class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum, right_sum = 0, sum(nums)

        for idx, ele in enumerate(nums):
            right_sum-=ele
            if left_sum == right_sum:
                return idx
            
            left_sum+=ele
        return -1