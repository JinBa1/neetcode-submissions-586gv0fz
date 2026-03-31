class MyHashSet:
    size = 100
    buckets = []

    def __init__(self):
        self.buckets = [[] for _ in range(self.size)]    

    def hash_function(self, value):
        # Simple hash function: sum of character codes modulo the number of buckets
        return value % self.size    

    def add(self, key: int) -> None:
        # Add a value
        index = self.hash_function(key)
        bucket = self.buckets[index]
        if key not in bucket:
            bucket.append(key)

    def remove(self, key: int) -> None:
        # Remove a value
        index = self.hash_function(key)
        bucket = self.buckets[index]
        if key in bucket:
            bucket.remove(key)

    def contains(self, key: int) -> bool:
        # Check if a value exists in the set
        index = self.hash_function(key)
        bucket = self.buckets[index]
        return key in bucket


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)