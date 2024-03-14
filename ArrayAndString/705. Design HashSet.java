class MyHashSet {
    
    boolean buckets[][]; //2d Array of booleans
    int bucket = 10000;
    int bucketItem = 10000;
    
    public MyHashSet() {
        buckets = new boolean[bucket][];
        //every hashset has 10,000 buckets
    }
    public int getBucket(int key){
        return key / bucket;
        // get the bucket which is the significant digits
    }
    public int getBucketItem(int key){
        return key % bucketItem;
        //cut the key number down to specific item number
    }
    public void add(int key) {
        int bucketKey = getBucket(key);
        int bucketItemkey = getBucketItem(key);
        
        //add a bucket if one isn't there already
        if(buckets[bucketKey] == null)
            buckets[bucketKey] = new boolean[bucketItem];
        buckets[bucketKey][bucketItemkey] = true;
    }
    public void remove(int key) {
        
        int bucketKey = getBucket(key);
        int bucketItemkey = getBucketItem(key);

        //if it exists, set it to false
        if(buckets[bucketKey] != null)
             buckets[bucketKey][bucketItemkey] = false;
    }
    public boolean contains(int key) {
        int bucketKey = getBucket(key);
        int bucketItemkey = getBucketItem(key);
        
        //if you find the bucket, return the value
         if(buckets[bucketKey] != null)
             return  buckets[bucketKey][bucketItemkey];
        return false;
    }
}