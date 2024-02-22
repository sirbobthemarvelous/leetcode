class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        //let's try working backwards in java
        int back = m+n-1, back1 = m-1, back2 = n-1;
        while(back2 >=0){ //cover the else statement
            if(back1 >=0 && nums1[back1] > nums2[back2]){
                nums1[back] = nums1[back1];
                back1--;
                back--;
            }
            else{
                nums1[back] = nums2[back2];
                back2--;
                back--;
            }

        }
        
    }
}