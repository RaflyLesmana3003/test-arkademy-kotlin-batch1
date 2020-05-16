# NOTE func for triangle
def triangle(angka):
  # check if input is int, instead string 
  # and check if input is largest than 0 
  if(isinstance(angka, int) != True or angka < 0):
    return "parameter harus angka dan positif!"

  # rows
  for i in range(0, angka): 
    
      # columns 
      for j in range(0, i+1): 
        
          # print data 
          print("# ",end="") 
      
      # new row
      print("\r") 


triangle(7)

#false
#triangle(-2)

#false
# triangle("p")