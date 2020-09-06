def sum_of_cubes(n):
  total = 0
  for i in range(1,n+1):
    total = total + pow(i,3)
  return total
#print("Sum of cubes: ",sum_of_cubes(3))
#print("sum of cubes: ",sum_of_cubes(9))
