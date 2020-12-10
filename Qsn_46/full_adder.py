def AND(a,b):
    if(a == True and b == True):
        return int(True)
    else:
        return int(False)

def OR(a,b): ##defines the OR Gate
    if(a == False and b == False):
        return int(False)
    else:
        return int(True)

def XOR(a,b): #defines the XOR Gate
    if(a!= b):
        return int(True)
    else:
        return int(False)

a = bool(int(input("a: "), 2))
b = bool(int(input("b: "), 2))
c = bool(int(input("Cin: "), 2))

d = XOR(a,b)
e = XOR(d,c)
f = AND(d, c)
g = AND(a, b)
h = OR(f, g)
print("Cout:", h)
print("Sum:", e)
