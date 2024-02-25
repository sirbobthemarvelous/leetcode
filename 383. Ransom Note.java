
class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {

        // Initialize an array of count with the size that fits the ascii table
        int[] counter = new int[128];
        // Traverse a loop through the magazine and fill up the array with numbers
        for (final char ch : magazine.toCharArray())
            ++counter[ch];
        // loop through the letters in ransomNote...
        for (final char ch : ransomNote.toCharArray())
            if (--counter[ch] < 0)
                return false;
        return true;      
    }
}