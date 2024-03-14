class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.hashmap = [[] for _ in range(self.size)]
        #1000 buckets by 1000 items in there

    def _hash(self, key):
        return key % self.size #get the hashItem number

    def put(self, key, value):
        hash_key = self._hash(key)
        for i in range(len(self.hashmap[hash_key])):
            #loop through the length of the bucket
            if self.hashmap[hash_key][i][0] == key:
            #until you find the key
                self.hashmap[hash_key][i] = (key, value)
                return
        self.hashmap[hash_key].append((key, value))

    def get(self, key):
        hash_key = self._hash(key)
        for k, v in self.hashmap[hash_key]:
            #loop through the bucket until you find the key
            if k == key:
                return v
        return -1

    def remove(self, key):
        hash_key = self._hash(key)
        for i in range(len(self.hashmap[hash_key])):
            #loop through the bucket until you find the key
            if self.hashmap[hash_key][i][0] == key:
                self.hashmap[hash_key].pop(i)
                return