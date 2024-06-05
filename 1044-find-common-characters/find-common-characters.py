class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        min_freq = Counter(words[0])

        for w in words:
            min_freq &= Counter(w)
        return list(min_freq.elements())
        