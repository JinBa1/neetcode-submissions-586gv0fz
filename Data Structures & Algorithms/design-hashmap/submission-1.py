class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.buckets = [[] for _ in range(self.size)]
    
    def hash_func(self, key: int) -> int:
        # A simple modulos hash
        return key % self.size

    def put(self, key: int, value: int) -> None:
        k_bucket = self.buckets[self.hash_func(key)]

        for i, (k, _) in enumerate(k_bucket):
            if k == key:
                k_bucket[i] = (key, value)
                return
        k_bucket.append((key, value))
        

    def get(self, key: int) -> int:
        k_bucket = self.buckets[self.hash_func(key)]

        for i, (k, v) in enumerate(k_bucket):
            if k == key:
                return v
        return -1
        

    def remove(self, key: int) -> None:
        k_bucket = self.buckets[self.hash_func(key)]

        for i, (k, v) in enumerate(k_bucket):
            if k == key:
                k_bucket.pop(i)

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)