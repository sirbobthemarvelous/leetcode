class Solution {
    public List<List<Integer>> generate(int numRows) {
    List<List<Integer>> arr = new ArrayList<>();
    arr.add(List.of(1));
    for (int i = 1; i < numRows; i++) {
        List<Integer> li = new ArrayList<>();
        int prev = 1;
        for (int j = 0; j <= i; j++) {
            li.add(prev);
            prev = prev * (i - j) / (j + 1);
        }
        arr.add(li);
    }
    return arr;
}
    /*
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> result = new ArrayList<>();
        result.add(new ArrayList<Integer>());
        result.get(0).add(1);
        if(numRows == 1) {
            return result;
        }
        result.add(new ArrayList<Integer>());
        result.get(1).add(1);
        result.get(1).add(1);
        if(numRows == 2) {
            return result;
        }
        for(int times = 3; times<= numRows; times++){
            result.add(new ArrayList<Integer>());
            result.get(times-1).add(1);
            for(int move = 0; move < result.get(times-1).size()-1; move++){
                int val = result.get(times-2).get(move)+result.get(times-2).get(move+1);
                result.get(times-1).add(val);
            }
            result.get(times-1).add(1);
        }

        return result;
    } */
}