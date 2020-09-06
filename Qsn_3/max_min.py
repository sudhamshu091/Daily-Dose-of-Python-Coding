def max_min(list):
    max=list[0]       #initialisation
    min=list[0]
    for n in list:    #for comparing every number with another number in list
        if n > max:   #here max is second max
            max = n   #here max is highest of all
        elif n < min: #here min is second min
            min = n   #here min is lowest of all
    return max,min
#test cases
#print(max_min([1,2,3,4,8,6,7,5]))
#print(max_min([123,567,899,98,67.8,-98]))
