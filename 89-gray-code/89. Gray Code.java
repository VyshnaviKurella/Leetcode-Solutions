class Solution {
    public List<Integer> grayCode(int n) {
       List<Integer> mp = new ArrayList<Integer>();
       int num =(int) Math.pow(2,n);
       for(int i=0;i<num;i++)
        mp.add(i);
      for(int i=0;i<num-1;i++)
      {  //System.out.println(i);
          for(int j=i+1;j<num;j++)
          { 
            int val = mp.get(i)^mp.get(j);
                //System.out.println(val);
              val = val & (val-1);
              System.out.println(val);          
            if(val==0)
            {  
                 int temp = mp.get(i+1);
                 mp.set(i+1,mp.get(j));
                 mp.set(j,temp); 
                 j = num;
                
             } 
          }
      }
       return mp;
    }
}