class Solution {
    public int[] replaceElements(int[] arr) {
        if (arr.length==1){ //simple base case
            arr[arr.length-1] = -1;
            return arr;
        } 
        int largest = arr[arr.length-1];
        arr[arr.length-1] = -1;
        int temp;
        for(int x = arr.length-2; x >-1;x--){ //loop through backwards
            if(arr[x] > largest){
                temp = arr[x];                    
                arr[x] = largest;
                largest = temp;
            }
            else{
                arr[x] = largest;
            }
        }
    return arr;
    }
}