import random
class RandomizedSet:

    def __init__(self):
        self.seen = []

    def insert(self, val: int) -> bool:
        if val in self.seen:
            return False
        self.seen.append(val)
        return True
        
        

    def remove(self, val: int) -> bool:
        if val in self.seen:
            self.seen.remove(val)
            return True
        return False
        

    def getRandom(self) -> int:
        ans = random.choice(self.seen)
        return ans

        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()