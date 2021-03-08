class Solution:
    def combgen(self, nums, subcomb, res, k):
        if len(subcomb) == k :
            res.append(subcomb)
            return
        for i in range(len(nums)) :
            self.combgen(nums[i+1:], subcomb+[nums[i]], res, k)

    def combine(self, n: int, k: int):
        res = []
        nums = [i for i in range(1, n+1)]
        self.combgen(nums, [], res, k)
        return res

print(Solution().combine(4,2))
