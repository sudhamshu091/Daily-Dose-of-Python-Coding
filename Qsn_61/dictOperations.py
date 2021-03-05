class Solution:

    def listtodict(self,list1,list2):
        return dict(zip(list1,list2))

    def sort_dict(self,dict):
        for key in sorted(dict):
            print("%s: %s" %(key, dict[key]))

    def maxmin(self,dict):
        maxval = max(dict.keys(), key = lambda k : dict[k])
        minval = min(dict.keys(), key = lambda k : dict[k])
        return maxval,minval

s = Solution().listtodict(['red', 'green', 'blue'],['#FF0000','#008000', '#0000FF'])
print(s)
print(Solution().sort_dict(s))
print(Solution().maxmin(s))
