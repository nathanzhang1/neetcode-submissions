class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            self.store[key].append([value, timestamp])
        else:
            self.store[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store or self.store[key][0][1] > timestamp:
            return ""
        
        l, r = 0, len(self.store[key])-1
        res = l

        while l <= r:
            m = (l + r) // 2
            if self.store[key][m][1] <= timestamp:
                res = m
                l = m+1
            else:
                r = m-1
        
        return self.store[key][res][0]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)