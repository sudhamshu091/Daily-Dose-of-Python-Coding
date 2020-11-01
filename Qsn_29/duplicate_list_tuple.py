List = [87, 52, 44, 53, 54, 87, 52, 53]
print("List", List)
List = list(set(List))
tuple = tuple(List)
print("tuple ", tuple)

print("Minimum number is: ", min(tuple))
print("Maximum number is: ", max(tuple))
