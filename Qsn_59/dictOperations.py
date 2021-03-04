import operator
class Solution:

    def ispresent(self,d,k):
        if k in d:
            d.pop(k)
            print("Given key was there, Now deleted")
            return dict(sorted(d.items(), key = operator.itemgetter(0)))
        else:
            print("Given key wasn't there")
            return dict(sorted(d.items(), key = operator.itemgetter(0)))

    def square_dict(self,d):
        for x in d:
            d[x] = x*x
        return d

s = Solution().ispresent({1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60},4)
print(s)
print(Solution().square_dict(s))
