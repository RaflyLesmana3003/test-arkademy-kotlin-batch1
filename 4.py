# import python package for regex
import re

def findDuplicates(kata):
  # check if input is string
  if isinstance(kata, str):
    
    count = {}
    unduplicated = 0

    # if data have duplicate then add 1 point again
    for i in kata:
      if i in count:
        count[i] += 1
      else:
        count[i] = 1

    for key in count:
      # if char point is largest than 1 
      if count[key] > 1: 
        x = re.search("\s", key)
        # if char is space then ignore
        if (x):
          pass
        else:
          print (key,":",count[key])
      #  if char point is 1
      else:
        # add unduplicated char
        unduplicated += 1

    # if char do not have duplicated char
    if unduplicated == len(count):
      print("tidak ada karakter berulang")

  else:
    print("Harus memasukan parameter dan harus string!")

findDuplicates("hari apa saja saya bisa!")