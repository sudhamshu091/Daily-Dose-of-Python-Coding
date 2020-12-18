a = "sudhamshu"
b = list(a)
count = 0
for i in b:
    if count % 2 == 0:
        b[count] = b[count].upper()
    count +=1
print("".join(b))
