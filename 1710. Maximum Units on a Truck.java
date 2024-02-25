class Solution {
    public int maximumUnits(int[][] B, int T) {
        Arrays.sort(B, (a,b) -> b[1] - a[1]);
        int ans = 0;
        for (int[] b : B) {
            int count = Math.min(b[0], T);
            ans += count * b[1];
            T -= count;
			if (T == 0) return ans;
        }
        return ans;
    }
}
/*
class Solution {
    public int maximumUnits(int[][] boxTypes, int truckSize) {

        //a sorting algorithm to start with
        Arrays.sort(boxTypes, new Comparator<int[]>() {
            public int compare(int[] boxType1, int[] boxType2) {
                if (boxType1[1] != boxType2[1])
                    return boxType2[1] - boxType1[1];
                else
                    return boxType2[0] - boxType1[0];
            }
        });
        
        //keep adding up until the capacity is lower than the chunk amount
        int answer = 0;
        for(int index=0;index<boxTypes.length;index++){
            if(boxTypes[index][0] > truckSize){
                answer+= boxTypes[index][0]*boxTypes[index][1];
                truckSize-= boxTypes[index][0];
            }
            else{
                answer+= boxTypes[index][1]*truckSize;
                break;
            }
        }
        return answer;
    }
}*/