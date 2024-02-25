class Solution {
    public void duplicateZeros(int[] arr) {
        //the two pointer solution is better than the home-made insert function
        int length = arr.length, count = 0;

        for (int num : arr) { //count the number of zeros in the array
            if (num == 0) {
                count++;
            }
        }
        int i = length - 1;
        int j = length + count - 1;

        //modify array from the back
        while (i >= 0 && j >= 0) {

            if (arr[i] != 0) {
                if (j < length) { //keep adding until you've exhausted the spots increased by the zeros
                    arr[j] = arr[i];
                }

            } else {
                if (j < length) {
                    arr[j] = arr[i];
                }
                j--;
                if (j < length) {
                    arr[j] = arr[i];
                }
            }
            i--;
            j--;
        }
        /*
        int x = 0;
        while(x < arr.length-1){
            if(arr[x]==0){ 
                //this cannot be the best way to do this
                for(int y = arr.length-1;y>x+1;y--){
                    arr[y] = arr[y-1];
                }
                arr[x+1] = 0;
                x+=2;
            }
            else{
                x++;
            }
        }
        */
        
    }
}