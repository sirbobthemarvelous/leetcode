import java.util.ArrayList;
class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        //initialize a hash map
        Map<Integer, Integer> hashmap = new HashMap<>();

        for (int index = 0; index < nums1.length; index++) {
            //fill up by frequency
            if(!hashmap.containsKey(nums1[index])){
                hashmap.put(nums1[index], 1);
            }
            else {
                hashmap.put(nums1[index], hashmap.get(nums1[index])+1);
            }
        }
        ArrayList<Integer> resultStuff = new ArrayList<Integer>();

        for (int index = 0; index < nums2.length; index++) {

            if(hashmap.containsKey(nums2[index])){
                resultStuff.add(nums2[index]);
                hashmap.put(nums2[index], hashmap.get(nums2[index])-1);
                if( hashmap.get(nums2[index]) == 0) {
                    hashmap.remove(nums2[index]);
                }
                
            }
        }
        
        
        int[] result = new int[resultStuff.size()];
        for (int i = 0; i < resultStuff.size(); i++) {
            result[i] = resultStuff.get(i);
        }
        return result;
        
        
    }
}