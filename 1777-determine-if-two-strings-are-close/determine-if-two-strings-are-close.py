class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!=len(word2):
            return False

        freq1 = [0]* 26
        freq2 = [0]* 26

        for idx in range(len(word1)):
            char1 = ord(word1[idx]) - ord("a")
            char2 = ord(word2[idx]) - ord("a")

            freq1[char1]+=1
            freq2[char2]+=1

        for idx in range(len(freq1)):
            if freq1[idx]>0 and freq2[idx]==0:
                return False
            if freq2[idx]>0 and freq1[idx]==0:
                return False
            
        freq1.sort()
        freq2.sort()

        return freq1==freq2

                
