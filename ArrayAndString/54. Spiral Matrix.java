class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        //base cases 
        int height = matrix.length, width = matrix[0].length;
        if(height == 1) Arrays.asList(matrix[0]);
        List<Integer> result = new ArrayList<>();
        //List<Integer> result = Arrays.asList(new Integer[height*width]);
        if(width == 1){
            for(int ele = 0; ele < matrix.length; ele++){
                //result.set(ele, matrix[ele][0]);
                result.add(matrix[ele][0]);
            }
            return result;
        }
        // 4 moving walls, two of which is height and width
        int leftWall = 0, upWall = 0;
        int finalSize = height*width, i = 0;
        while(result.size()< finalSize){
            for(i= leftWall; i< width; ++i){
                //result.set(resultIndex, matrix[upWall][i]);
                result.add(matrix[upWall][i]);
            }
            upWall++; //move the ceiling once you've cleared it
            for(i = upWall; i<height;++i){
                //result.set(resultIndex, matrix[i][width-1]);
                result.add(matrix[i][width-1]);
            }
            width--; //move the right wall once you've cleared it
            if(upWall<height){ //check that we haven't collapsed the walls
                for(i = width-1; i>=leftWall;--i){
                    //result.set(resultIndex, matrix[height-1][i]);
                    result.add(matrix[height-1][i]);
                }
                height--;
            }
            if(leftWall<width){ //check that we haven't collapsed the walls
                for(i = height-1; i>=upWall;--i){
                    //result.set(resultIndex, matrix[i][leftWall]);
                    result.add(matrix[i][leftWall]);
                }
                leftWall++;
            }
        }
        return result;
    }
}