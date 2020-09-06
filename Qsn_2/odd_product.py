def odd_product(number):
    for i in range(len(number)):
        for j in range(len(number)):
            if i!=j:
                product = number[i] * number[j]
                if (product % 2) & 1:
                    return True
print(odd_product([1,6,4,7,8]))
print(odd_product([2,4,6,8]))
print(odd_product([1,2,3]))
