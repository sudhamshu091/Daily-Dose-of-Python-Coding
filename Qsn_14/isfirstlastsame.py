def isfirstlastsame(list):
    first = list[0]
    last = list[-1]
    if (first == last):
        return True
    return False
print(isfirstlastsame([10,20,30,20,10]))
print(isfirstlastsame([10,20,30,40,50]))
