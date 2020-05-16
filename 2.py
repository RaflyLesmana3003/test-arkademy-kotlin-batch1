# import python package for regex
import re

# func check input
def cek_kata(kata):
    # convert string to array/list
    kata = kata.split(' ')

    # counter var for check if array value is sentence without number
    counter = 0;
    for sentence in kata:
        # use regex for check input
        x = re.search("([0-9])+", sentence)
        if (x):
            pass
        else:
            # if array value not include number then add counter value
            counter += 1
            
    # output counter and a whole string lenght
    print(counter,"/",len(kata))
            

cek_kata("2 pasang sandal hilang");

cek_kata("ini adalah sebuah kata");