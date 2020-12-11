def multiplyList(List) :
    result = 1
    for i in List:
         result = result * i
    return result

def is_divisible(nums,k,w,i):
        if k == 1:
            return nums[0]
        elif k == 2:
                return i % nums[0] == 0
        elif k == 3:
            return (i % nums[k-2] == 0 and i % nums[k-1] == 0)
        else:
            return is_divisible(nums,k-1,w,i)

def lcm(list):
    nums = sorted(list)
    w = multiplyList(list)
    k = len(nums)
    for i in range(nums[-1], w + 1, nums[-1]):
        if is_divisible(nums,w,k,i):
            return i
