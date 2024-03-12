class Solution {
    public List<Integer> getRow(int rowIndex) {
        int[] prev = new int[rowIndex + 1];
        int[] curr = new int[rowIndex + 1];
        prev[0] = 1; curr[0] = 1;
        for(int i = 1, mid; i <= rowIndex ; i++){
            mid = i / 2 + 1;
            curr[i] = 1;
            for(int j = 1; j < mid; j++){
                curr[j] = prev[j] + prev[j - 1];
                curr[i - j] = curr[j];
            }
            int[] temp = curr;
            curr = prev;
            prev = temp;
        }
        List<Integer> Curr = new ArrayList<Integer>();
        for(int c : prev) Curr.add(c);
        return Curr;
    }

        /*
        if(rowIndex==0) return [1];
        if(rowIndex==1) return [1,1];
        List<Integer> prev = new ArrayList<Integer>();
        prev = {1,1};
        List<Integer> curr = new ArrayList<Integer>();
        for(int i = 1; i < rowIndex; i++){
            curr.add(1);
            for(int first = 0; first < prev.size()-1; first++){
                curr.add(prev.get(first)+prev.get(first+1));
            }
            curr.add(1);
            prev = curr;
        }
        return curr;
        */
}