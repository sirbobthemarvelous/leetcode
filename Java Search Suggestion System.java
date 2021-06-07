import java.util.Arrays;
import java.util.ArrayList;

class Solution {
    public List<List<String>> suggestedProducts(String[] products, String searchWord) {
        Arrays.sort(products);
        List<List<String>> result = new ArrayList<List<String>>();
            //instantiate individual array lengths later
        for(int substringIndex = 1; substringIndex < searchWord.length()+1; substringIndex++){
            List<String> temp = new ArrayList();
            temp.clear();
            int numInserted =0;
            boolean early = false;
            String newPrefix = searchWord.substring(0,substringIndex);
            
            for(int index =0; index<products.length;index++){
                if(products[index].startsWith(newPrefix)){
                    temp.add(products[index]);
                    numInserted++;
                }
                if(numInserted==3){
                    result.add(temp);
                    early = true;
                    break;
                }
            }
            if (early == false){
                result.add(temp);
            }
            
        }
        return result;
    }
}