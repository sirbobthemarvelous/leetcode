class MyHashMap {
    private static final int SIZE = 1000;
    private List<int[]>[] map;
    //list of int arrays instead of 2D array

    public MyHashMap() {
        map = new List[SIZE];
        //its a map so it's a list of 1000 buckets
        for (int i = 0; i < SIZE; i++) {
            map[i] = new ArrayList<>();
            //fill the list with arraylists
        }
    }

    public void put(int key, int value) {
        int index = key % SIZE;
        List<int[]> bucket = map[index];
        //each arraylist is just a key value pair
        for (int[] pair : bucket) {
            if (pair[0] == key) {
                pair[1] = value; // Update value if key exists
                return;
            }
        }
        bucket.add(new int[]{key, value});
    }

    public int get(int key) {
        int index = key % SIZE;
        List<int[]> bucket = map[index];
        for (int[] pair : bucket) {
            if (pair[0] == key) {
                return pair[1]; // Return the value if key exists
            }
        }
        return -1; // Key not found
    }

    public void remove(int key) {
        int index = key % SIZE;
        List<int[]> bucket = map[index];
        Iterator<int[]> iterator = bucket.iterator();
        //create an iterator, just keep checking the next thing in the bucket
        while (iterator.hasNext()) {
            int[] pair = iterator.next();
            if (pair[0] == key) {
                iterator.remove();
                return;
            }
        }
    }
}