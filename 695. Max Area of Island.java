class Solution {
     int[][]grid;
     boolean[][]seen;

    public  int getArea(int r,int c){
       if(r < 0 || r >= grid.length || c<0 || c>=grid[0].length || seen[r][c] || grid[r][c] ==0)
         return 0;
       seen[r][c]=true;
       return(1+getArea(r+1,c)+getArea(r-1,c)+getArea(r,c-1)+getArea(r,c+1));

     }

     public  int maxAreaOfIsland(int[][]grid){
       this.grid=grid;
       int maxArea =0;
       seen = new boolean[grid.length][grid[0].length];
       for(int i=0;i<grid.length;i++){
         for(int j=0;j<grid[0].length;j++){
           maxArea=Math.max(maxArea,getArea(i,j));


         }
       }
       return maxArea;

     }


}