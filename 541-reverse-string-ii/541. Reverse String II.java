class Solution {
    public String reverseStr(String s, int k) {
        StringBuilder res = new StringBuilder();
        int count=0;
        System.out.println(s.length());
       if(s.length()>=k){
        for(int i=0;i+k<=s.length();i=i+k)
        {
           StringBuilder sub1 = new StringBuilder(s.substring(i,i+k));
           if(count%2==0)
            sub1 = sub1.reverse();
            count++;
            res= res.append(sub1);
        }
          int lv= s.length()%k;
         StringBuilder ls = new StringBuilder(s.substring(s.length()-lv,s.length())); 
         if(count%2==0) ls.reverse();
         res.append(ls);
       }
       else
       {
         res= res.append(s);
         res=res.reverse();
       }
       
        return(res.toString());
        
    }
}