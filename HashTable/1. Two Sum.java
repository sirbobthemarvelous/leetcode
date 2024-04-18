class Solution {
    public int[] twoSum(int[] nums, int target) {
        //initialize a hash map
        Map<Integer, Integer> hashmap = new HashMap<>();
        int length = nums.length;

        for (int index = 0; index < length; index++) {
            int complement = target - nums[index];
            //look for the complement actively
            if(hashmap.containsKey(complement)){
                return new int[]{hashmap.get(complement), index};
            }
            else{
                hashmap.put(nums[index], index);
            }
        }
        return new int[]{}; //if somehow there is no solution
    }
}