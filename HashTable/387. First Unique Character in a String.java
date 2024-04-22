class Solution {
    public int firstUniqChar(String s) {
        //initialize a hash map
        Map<Character, Integer> hashmap = new HashMap<>();
        //char[] charArray = s.toCharArray();

        for (int index = 0; index < s.length(); index++) {
            //fill up and call duplicates -1
            if(!hashmap.containsKey(s.charAt(index))){
                hashmap.put(s.charAt(index), index);
            }
            else{
                hashmap.put(s.charAt(index), 100001);
            }
        }
        int smallVal = 100001;
        /*
        //remove duplicates
        for (Map.Entry<Character, Integer> entry : hashmap.entrySet()){
            if(entry.getValue() == -1){
                hashmap.remove(entry);
            }
        } */
        
        if(hashmap.size() == 0) return -1;

        //find the smallest
        for (Map.Entry<Character, Integer> entry : hashmap.entrySet()){
            if(entry.getValue() < smallVal){
                smallVal = entry.getValue();
            }
        }
        if(smallVal == 100001) return -1;
        return smallVal;
        
    
        
    }
}