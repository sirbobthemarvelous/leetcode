import java.util.ArrayList;

class Solution {
    public String[] findRestaurant(String[] list1, String[] list2) {
        //initialize a hash map
        Map<String, Integer> hashmap = new HashMap<>();

        for (int index = 0; index < list1.length; index++) {
            //fill up without duplicates
            if(!hashmap.containsKey(list1[index])){
                hashmap.put(list1[index], index);
            }
        }
        ArrayList<String> smallest = new ArrayList<String>();
        int smallVal = 2000;
        for (int index = 0; index < list2.length; index++) {

            if(hashmap.containsKey(list2[index])){
                if(hashmap.get(list2[index])+index < smallVal){
                    smallVal = hashmap.get(list2[index])+index;
                    smallest.clear();
                    smallest.add(list2[index]);

                }
                else if(hashmap.get(list2[index])+index == smallVal) {
                    smallest.add(list2[index]);
                }
            }
        }
        String[] arrayResult = new String[smallest.size()];
        for (int i = 0; i < smallest.size(); i++) {
            arrayResult[i] = smallest.get(i);
        }
        return arrayResult; 
    }
}