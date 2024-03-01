class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        num1_dis = set(nums1)
        num2_dis = set(nums2)
        res = [[],[]]

        for i in num1_dis:
            if i not in num2_dis:
                res[0].append(i)

        for i in num2_dis:
            if i not in num1_dis:
                res[1].append(i)

        return res