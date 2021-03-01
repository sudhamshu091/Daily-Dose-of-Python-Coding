import operator
class Solution:
    def dictOperations(self,d1,d2,d3,new_values):
        d1.update(new_values)
        d4 = {}
        for d in (d1,d2,d3):
            d4.update(d)
        descending_sorted = dict(sorted(d4.items(), key = operator.itemgetter(0), reverse = True))
        ascending_sorted = dict(sorted(d4.items(), key = operator.itemgetter(0)))
        return ascending_sorted,descending_sorted

      

d1 = {1:30,2:20}
d2 = {3:10,4:50}
d3 = {5:40,6:60}
new_values = {7:70}
print(Solution().dictOperations(d1,d2,d3,new_values))

