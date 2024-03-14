class MyHashSet:

    #faster but more memory
    def __init__(self):
        self.l={} #create a dictionary

    def add(self, key: int) -> None:
        self.l[key]=1
        # set key to True

    def remove(self, key: int) -> None:
        if key in self.l:
            del self.l[key]
            #remove key if exists

    def contains(self, key: int) -> bool:
        return key in self.l
        #return the true/false value in the dict