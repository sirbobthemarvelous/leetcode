class Solution {
    public int singleNumber(int[] nums) {
        //XOR bitwise is faster
        int result = 0;
        for(int num : nums){
            result ^= num;
        }
        return result;
        //hashsets work but it's slow
        /*
        Set<Integer> hashset = new HashSet<>();
        for (int key : nums) {
            if (hashset.contains(key)) {
                hashset.remove(key);
            }
            else{
                hashset.add(key);
            }
        }
        ArrayList<Integer> result = new ArrayList<>(hashset);

        return result.get(0);
        */
    }
}