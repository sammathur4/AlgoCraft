class SmallestInfiniteSet:

    def __init__(self):
        self.min_val = 1
        self.is_val_in_heap = {}
        self.heap = []
        

    def popSmallest(self) -> int:
        if not self.heap:
            smallest = self.min_val
            self.min_val+=1

        else:
            smallest = heappop(self.heap)
            del self.is_val_in_heap[smallest]

        return smallest
        

    def addBack(self, num: int) -> None:
        if num>=self.min_val or num in self.is_val_in_heap:
            return
        
        elif num == self.min_val-1:
            self.min_val -=1
        else:
            heappush(self.heap, num)
            self.is_val_in_heap[num]=True
            
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)