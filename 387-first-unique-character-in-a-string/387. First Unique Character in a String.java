class Solution {
    public int firstUniqChar(String s) {
        int res=-1;
        for(int i=0;i<s.length();i++)
         {
             int fi= s.indexOf(s.charAt(i));
            
             int li = s.lastIndexOf(s.charAt(i));
             
             if(fi==li)
              {res = fi;
               i= s.length();
              }
         }
         return res;
    }
}