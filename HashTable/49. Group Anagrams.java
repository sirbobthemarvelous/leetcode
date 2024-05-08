class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        //initialize a hash map
        Map<String, List<String>> hashmap = new HashMap<>();
        //char[] charArray = s.toCharArray();

        String result;
        for( String ele: strs){
            if(ele.length() > 1){
                char[] charArray = ele.toCharArray();
                Arrays.sort(charArray);
                result = new String(charArray);
            }
            else{
                result = ele;
            }
            if(!hashmap.containsKey(result)){
                ArrayList<String> list = new ArrayList<String>();
                list.add(ele);
                hashmap.put(result, list);
            }
            else{
                List<String> list = hashmap.get(result);
                list.add(ele);
                hashmap.put(result, list);
            }
        }
        //converting to types with lists and arraylists is pretty finiky
        List<List<String>> allLists = new ArrayList<List<String>>();
        for( Map.Entry<String, List<String>> entry : hashmap.entrySet()){
            allLists.add(entry.getValue());
        }

        return allLists;
    }
}