class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:

        res = [0] * len(t)
        st = []

        for i in range(len(t)-1, -1, -1 ):
            curr_t = t[i]

            while st and curr_t>=t[st[-1]]:
                st.pop()
            if st:
                res[i] = st[-1]-i
            
            st.append(i)
        return res

        