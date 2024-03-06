class Solution {
    public int[] findDiagonalOrder(int[][] mat) {
        int height = mat.length, width = mat[0].length;
        if(height == 0) return new int[] {};
        if(height == 1){
            return mat[0];
        }
        if(width == 1){
            int result[] = new int[height];
            for(int i = 0; i< height; i++){
                result[i] = mat[i][0];
            }
            return result;
        } //various base-cases

        int index = 0; //up and down
        int index2 = 0; //left and right
        boolean upperRight = true;
        int result[] = new int[height*width];
        int resultIndex = 0;
        while(resultIndex < result.length){
            if(upperRight){ //going upRight or downLeft?
                while(index >= 0 && index2 < width){
                    result[resultIndex] = mat[index][index2];
                    index--;
                    index2++;
                    resultIndex++;
                }
                index++;
                if(index2 >= width){
                    index2= width-1;
                    index++;
                }
            }
            else{
                while(index < height && index2 >= 0 ){
                    result[resultIndex] = mat[index][index2];
                    index++;
                    index2--;
                    resultIndex++;
                }
                index2++;
                if(index >= height){
                    index = height - 1;
                    index2++;
                }
            }
            upperRight = !upperRight;
        }
        return result;
    }
}