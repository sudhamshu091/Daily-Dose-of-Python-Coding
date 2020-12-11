def lcm3(n1,n2,n3):
    nums = sorted([n1,n2,n3])
    w = nums[0]*nums[1]*nums[2]

    for i in range(nums[2], w+1, nums[2]):
        if i % nums[0] == 0 and i % nums[1] == 0:
            return i
