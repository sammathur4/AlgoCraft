class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        sorted_prod = sorted(products)
        res = []

        for i in range(1, len(searchWord) +1):
            prefix = searchWord[:i]

            idx = bisect_left(sorted_prod, prefix)
            sug = []

            for j in range(idx, min(idx+3, len(sorted_prod))):
                if sorted_prod[j].startswith(prefix):
                    sug.append(sorted_prod[j])
            res.append(sug)
        return res

        