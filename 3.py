def HollowTriangle(number) : 
    
    #  loop row
    for i in range(1,number+1) : 
          
        # loop space for centering inverted pyramid
        for j in range(1,i) : 
            print ("  ",end=" ") 
              
        # Print hollow inverted pyramid 
        for j in range(1,(number * 2 - (2 * i - 1))  
                                       +1) : 
            if (i == 1 or j == 1 or 
               j == (number * 2 - (2 * i - 1))) : 
                print (" o ", end="")  
            else : 
                print(" x ", end="")  
                  
        # print next line 
        print (""), 

HollowTriangle(8) 