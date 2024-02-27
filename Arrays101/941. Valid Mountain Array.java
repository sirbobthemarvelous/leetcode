class Solution {
    public boolean validMountainArray(int[] arr) {
        if(arr.length < 3) return false;
        int l = 0;
        int r = arr.length - 1;
        while(l + 1 < arr.length - 1 && arr[l] < arr[l + 1]) l++;
        while(r - 1 > 0 && arr[r] < arr[r - 1]) r--;
        return l == r;
    }
}
/*
class Solution {
    public boolean validMountainArray(int[] arr) {
        if(arr.length < 3 || arr[1] < arr[0]) return false;
        boolean ascending = true;
        for(int x=1;x< arr.length;x++){
            if(arr[x] == arr[x-1] || 
            !ascending && arr[x] > arr[x-1]) return false;
            if(ascending && arr[x] < arr[x-1]) ascending = false;

        } 
        return !ascending;
    }
} */