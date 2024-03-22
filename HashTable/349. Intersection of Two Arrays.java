
class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        HashSet<Integer> result = new HashSet<>();
        HashSet<Integer> hset = new HashSet<>();

        for(int num: nums2){
            hset.add(num);
        }
        for(int num: nums1){
            if(hset.contains(num)){
                result.add(num);
            }
        }

        int resultForm[] = new int[result.size()];
        // iterating over the hashset 
        int index=0;
        for(int num:result){ 
          resultForm[index++] = num; 
        } 
        
        return resultForm;
    }
}