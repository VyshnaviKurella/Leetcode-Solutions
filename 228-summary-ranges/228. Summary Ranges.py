class Solution:
 
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        if n == 0:
            return []
        if n==1:
            return[str(nums[0])]
        if n==2:
             if nums[1] != nums[0]+1:
                 return[str(nums[0]),str(nums[1])]
             return[str(nums[0]) +"->"+ str(nums[1])]

       
        #print(n)  
        def end(val):
          
            global init
            end=0
            if  val == 0:
              global i
              i=0
              init=nums[0]
            temp = init
            while  i < n-1 :
                if nums[i+1] != nums[i]+1:
                #print(val)
                    end = nums[i]
                    init =nums[i+1]
                    i= i+1
                    
                #print(temp,end,i)
                    return [temp,end]
                i=i+1
            if i==n-1:
                #print(temp,nums[i])
                i=i+1
                return [temp,nums[i-1]]
           
           
                
               
        for t in range(n):
            #global init 
            #global temp
            
            global ranlist
            last = end(t)
        
            #print(t)
            #print(last)
            if last != None:
                if last[0]== last[1]:
                    temp ="{}"
                    temp = temp.format(last[0])
                
                else:
                    temp = "{}->{}"
                    temp = temp.format(last[0],last[1])
               # print(temp)

                if t==0:
                    ranlist = list((temp,))
                else:
                    ranlist += list((temp,))
                
            if t== n-1:
                #ranlist.clear()
                init=0
                i=0
            
           
        return ranlist
    
        

 