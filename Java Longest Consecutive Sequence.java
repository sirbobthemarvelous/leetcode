import java.util.ArrayList;
class Solution {
    public static int[] removeDuplicates(int[] arr){
        ArrayList nums2 = new ArrayList();
        nums2.add(0,arr[0]);
        int nums2Index =0;
        for(int i = 1; i<arr.length; i++){
            if(arr[i-1]!=arr[i]){
                nums2Index++;
                nums2.add(nums2Index,arr[i]);
            }
        }
        int[] nums3 = new int[nums2Index+1];
        for(int j =0; j<nums3.length;j++){
            nums3[j] = (int) nums2.get(j);
        }
        return nums3;
    }
    public int longestConsecutive(int[] nums) {
        if(nums.length == 0){
            return 0;
        }
        int longest = 1;
        int chunk = 1;
        Arrays.sort(nums);
        int[] cleaned = removeDuplicates(nums);
        for(int i=1;i<cleaned.length;i++){
            if(cleaned[i-1]==cleaned[i]-1){
                chunk++;
            }
            else{
                if(chunk > longest){
                    longest = chunk;
                }
                chunk = 1;
            }
        }
        if(chunk > longest){
                    longest = chunk;
                }
        
        return longest;
    }
}