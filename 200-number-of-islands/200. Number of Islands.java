class NodeIndex{
    int rowNum; 
    int colNum;
    NodeIndex(int i, int j){
        rowNum=i;
        colNum=j;
    }
}

class Solution {
    public void BFS(char[][] grid, boolean [][]visitedArray, int i, int j){
     ArrayDeque<NodeIndex> q = new ArrayDeque<>();
        q.add(new NodeIndex(i,j));
        visitedArray[i][j] = true;
        while(!q.isEmpty()){
           NodeIndex p = q.poll();
           int row = p.rowNum, col = p.colNum;
           int adjRow = 0, adjCol = 0;
           
           for(int vicRow=-1; vicRow<=1; vicRow++){
               for(int vicCol=-1; vicCol<=1; vicCol++){
                   adjRow=row+vicRow; adjCol=col+vicCol;
                  
                   if((Math.abs(vicRow-vicCol)==1)&&
                   (adjRow>=0 && adjRow<grid.length) && 
                   (adjCol>=0 && adjCol<grid[i].length) && 
                   !visitedArray[adjRow][adjCol] &&
                    grid[adjRow][adjCol]=='1')
                   {
                       q.add(new NodeIndex(adjRow,adjCol));
                       visitedArray[adjRow][adjCol]=true;
                   }
                   adjRow=0; adjCol=0;
               }
           }
        }
    }

    public int numIslands(char[][] grid) {
        int n = grid.length;
        int m = grid[0].length;
        boolean visit[][] = new boolean[n][m];
        int count=0;

        for(int i=0; i<n; i++){
            for(int j=0; j<m; j++){
                if(grid[i][j]=='1' && visit[i][j]==false){
                    BFS(grid,visit,i,j);
                    count++;
                }
            }
        }
        return count;
    }

}
