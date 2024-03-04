class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        /*
        As we walk through all elements in the array, we can use the current element as an index and flag its value (in place). All numbers are > 0, so we can use a negative number.
In the end, the indexes of all positive numbers in the array are the missing values.
        */
        //good efficiency, doing it in-place
        for (int i : nums) {
            int index = Math.abs(i);
            if (nums[index - 1] > 0) {
                nums[index - 1] *= -1;
            }
        }
        List<Integer> res = new ArrayList<>();
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] > 0) {
                res.add(i + 1);
            }
        }
        return res;
        /*
        
        
        //using sets! this is slow
        Set<Integer> set = new HashSet<>();
        for (int val : nums) {
            set.add(val);
        }
        ArrayList<Integer> list = new ArrayList<>();
        for (int i = 1; i <= nums.length; i++) {
            if (!set.contains(i)) {
                list.add(i);
            }
        }
        return list;
        
        int[] filled;
        for(int i=1; i<nums.length+1;i++){
            filled[i-1] = i;
        }
        // Creating an object of Set class  
        Set<Integer> a = new HashSet<Integer>(filled); 
        // Adding all elements to List  
        //a.addAll(Arrays.asList(filled)); 
        
        // Again declaring object of Set class  
        Set<Integer> b = new HashSet<Integer>(); 
          
        b.addAll(Arrays.asList(nums)); 
        return a.removeAll(b); 
        */
    }
}