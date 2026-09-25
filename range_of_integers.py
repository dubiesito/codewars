def generate_range(start, stop, step):
    templist= []
    i = start
    while i <= stop:
        templist.append(i)
        i += step 
    return templist