class StockSpanner:

    def __init__(self):
        self.monotonic_stack = []
        

    def next(self, price: int) -> int:
        st = self.monotonic_stack

        cur_price_qoute, cur_price_span = price, 1

        while st and st[-1][0]<=cur_price_qoute:
            prev_price_quote, prev_price_span = st.pop()

            cur_price_span+=prev_price_span
        st.append(
            (cur_price_qoute, cur_price_span)
        )

        return cur_price_span
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)