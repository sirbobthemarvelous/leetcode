class Solution {
  public boolean checkIfExist(int[] arr) {
        HashMap<Integer,Integer> map = new HashMap<>();
        for (int i = 0; i < arr.length; i++) {
            map.put(arr[i],i);
        }
        for (int i = 0; i < arr.length; i++) {
//    As 3/2 = 1 so, if 3 is there and 1 is there , it will return true. To avoid, number should be even
//            To check if 0 is present and it returns the same index , we need to add != i as well.
            if(arr[i] %2 == 0 && map.get(arr[i]/2) != null && map.get(arr[i]/2)!= i){
                return true;
            }
        }
        return false;
    }
}
/*
class Solution {
    public boolean checkIfExist(int[] arr) {
        Arrays.sort(arr);
        int zeroCount = 0;
        for (int x : arr) {
            if (x != 0) {
                if (binarySearch(x*2, arr)) {
                    return true;
                }
            }
            else {
                ++zeroCount;
            }
        }
        return zeroCount >= 2;
    }
    
    public boolean binarySearch(int x, int[] nums) {
        int start = 0;
        int end = nums.length - 1;
        while (start <= end) {
            int mid = (int)((start + end)/2);
            if (nums[mid] < x) {
                start = 1 + mid;
            }
            else if (nums[mid] > x) {
                end = mid - 1;
            }
            else {
                return true;
            }
        }
        return false;
    }
}
class Solution {
    public boolean checkIfExist(int[] arr) {
        Arrays.sort(arr);
        for (int i = 0; i < arr.length; i++) {
            int target = 2 * arr[i];
            int lo = 0, hi = arr.length - 1;
            while (lo <= hi) {
                int mid = lo + (hi - lo) / 2;
                if (arr[mid] == target && mid != i) 
                    return true;
                if (arr[mid] < target) 
                    lo = mid + 1;
                else 
                    hi = mid - 1;
            }
        }

        return false;
    }
}
*/
// TC: O(n * logn), SC: O(1)
/*
import java.util.*; 
class Solution {
    public boolean checkIfExist(int[] arr) {
        //if (Collections.frequency(arr,0)  > 1) return true;
        Boolean zeros = false;
        Set<Integer> hash_Set = new HashSet<Integer>();
        for(int x=0; x< arr.length; x++){
            if(arr[x]==0){
                if(zeros) return true;
                zeros = true;
            }
            hash_Set.add(arr[x]);
        }
        if(zeros) hash_Set.remove(0);

        for(int i=0; i< arr.length; i++){
            if(hash_Set.contains(arr[i]*2)) return true;
        }
        return false;
    }
}
*/