class StockSpanner:

    def __init__(self):
        self.prices = []
        self.st = []
        

    def next(self, price: int) -> int:
        i = len(self.prices) - 1
        d = 1
        #print(f"prices: {self.prices}, looking for {price}")
        while i >= 0 and self.prices[i] <= price:
            i -= 1
            d += 1
        
        self.prices.append(price)

        return d

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)