class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int index = 0;
		int index2 = 0;
		int index3 = 0;
        int size = nums1.length+nums2.length;
		int [] combo = new int[size];
		//two for loops 
		while(index < nums1.length && index2 < nums2.length) {
			//compare which is lower
			if(nums1[index] < nums2[index2]) {
				combo[index3] = nums1[index];
				index++;
				index3++;
			}
			else {
				combo[index3] = nums2[index2];
				index2++;
				index3++;
			}
			//in the event that you reach the end of one array
			while(index < nums1.length && index2 == nums2.length) {
				combo[index3] = nums1[index];
				index++;
				index3++;
			}
			while(index == nums1.length && index2 < nums2.length) {
				combo[index3] = nums2[index2];
				index2++;
				index3++;
			}
		}
        if((size%2) ==0){
            return ((combo[size/2]+combo[(size/2)-1])/2);
        }
        else{
            return combo[size/2];
        }
    }
}