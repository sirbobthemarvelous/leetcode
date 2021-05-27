class Solution {
    static boolean checkDuplicateChars(char[] first, char[] second){
        for(int x=0; x< first.length; x++){
            for(int y=0; y<second.length; y++){
                if(first[x]==second[y]){
                    return true;
                }
            }
        }
        return false;
    }
    public int maxProduct(String[] words) {
        int unique = 0;
        for(int tulip=0;tulip<words.length-1; tulip++){
            for(int lake=tulip+1; lake<words.length; lake++){
                if(words[tulip].length()*words[lake].length() > unique){
                    char[] atticus = words[tulip].toCharArray();
                    char[] jesse = words[lake].toCharArray();
                    if(!checkDuplicateChars(atticus,jesse)){
                        unique = words[tulip].length()*words[lake].length();
                    }
                }
            }
        }
            
        return unique;
    }
}