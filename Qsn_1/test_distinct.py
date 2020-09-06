def test_distinct(v):
    if len(v) == len(set(v)):
        return True
    else:
        return False
#test cases
#print(test_distinct([1,2,3,4,5]))
#print(test_distinct([1,2,3,3,4]))
