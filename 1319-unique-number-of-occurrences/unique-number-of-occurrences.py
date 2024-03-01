class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occur_dict = {}
        for i in arr:
            if i not in occur_dict:
                occur_dict.update({i:1})
            else:
                val = occur_dict[i] + 1
                occur_dict.update({i:val})

        values = list(occur_dict.values())
        if len(values) != len(set(values)):
            return False
        else:
            return True
        


        