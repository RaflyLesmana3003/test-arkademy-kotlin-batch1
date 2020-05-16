def cariPasangan(data):
    count = {}
    match = 0

    # loop to initalize all char in data have 1 point
    for i in data:
    # if data have duplicate then add 1 point again
      if i in count:
        count[i] += 1
      else:
        count[i] = 1

    for key in count:
    # if char point is largest than 1 
      if count[key] > 1: 
        # if char point is even number
        if count[key] % 2 == 0:
            # then divide point with 2 and loop output
            for i in range(int(count[key]/2)):
                print("[",key,",",key,"]")
                match += 1
        # if char point is odd number
        else:
            # then divide point with 2 and reduce with 1 too get even number
            for i in range(int((count[key]-1)/2)):
                print("[",key,",",key,"]")
                match += 1
    print(match," pasang")

cariPasangan([5,13,5,5,9,20,9,5,14])