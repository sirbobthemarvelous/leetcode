class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        //initialize a hash map
        Map<Integer, Integer> hashmap = new HashMap<>();

        for (int index = 0; index < nums.length; index++) {
            //check if it's already there
            if(!hashmap.containsKey(nums[index])){
                hashmap.put(nums[index], index);
            } // add the index value at the spot
            else {
                if(-k <= (hashmap.get(nums[index]) -index) ) return true;
                hashmap.put(nums[index], index);
            }
        }
        return false;
        
    }
}