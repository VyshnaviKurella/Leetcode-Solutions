class Solution {
    public boolean isAnagram(String s, String t) { 
        if(s.length() != t.length())
        {
        return false;
        }
     HashMap<Character,Integer> mp1 = new HashMap();
     HashMap<Character,Integer> mp2 = new HashMap();
     for(int i=0;i<s.length();i++)
     {   
        char c= s.charAt(i);
        if(mp1.containsKey(c))
            mp1.put(c,mp1.get(c)+1);
        else
            mp1.put(c,1);
        
     }
     for(int i=0;i<t.length();i++)
     {  
        char c= t.charAt(i);
        if(mp2.containsKey(c))
            mp2.put(c,mp2.get(c)+1);
        else
            mp2.put(c,1);      
     }
     
    //  for(int i=0;i<s.length();i++)
    //  { 
    //     char c = s.charAt(i);
    //     if(!mp1.containsKey(c)|| !mp2.containsKey(c))       
    //       return false;
    //     System.out.println(mp1.get(c)!= mp2.get(c));
    //     System.out.println(mp1.get(c));
    //     System.out.println(mp2.get(c)); 
    //     if( mp1.get(c)!= mp2.get(c))
    //     {           
    //         return false;
    //     }

    if(!mp1.equals(mp2))
       return false;
     

return true;
    }
}