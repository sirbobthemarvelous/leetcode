class Solution {
    const int mod = (1e9)+7; // As the question expects.
    
    int getMax(int length, vector<int> &cuts) {
        sort(cuts.begin(), cuts.end()); // Sort so that we will easily get the thickness
                                        // of each piece after cutting it.
        int n = cuts.size();
        int maxCut = max(length-cuts[n-1], // Thickness of the last piece.
                         cuts[0]);         // Thickness of the first piece.
        for (int i=1; i<n; i++) { // For each cut -
            maxCut = max(maxCut, cuts[i]-cuts[i-1]); // Thickness of each piece.
        }
        return maxCut; 
    }

public:
    int maxArea(int height, int width, vector<int>& h, vector<int>& w) {
        long maxHeight = getMax(height, h);
        long maxWidth = getMax(width, w);
        return (int)(maxHeight * maxWidth % mod);
    }
};