class Solution {
    public List<List<Integer>> generate(int numRows) {
     List<List<Integer>> result = new ArrayList<List<Integer>>();
         for(int row=1;row<=numRows;row++)
        {   
            int value=1;
            List<Integer> rowValues = new ArrayList<Integer>();
            for( int position=1;position<=row;position++)
             { 
                rowValues.add(value);
                value= value*(row-position)/position;    
             }
             result.add(rowValues);
        }
     return(result);
    }
}