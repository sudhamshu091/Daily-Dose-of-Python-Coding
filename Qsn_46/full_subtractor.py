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
def NOT(a):
    if (a == 1):
        return int(False)
    else:
        return int(True)

a = bool(int(input("a: "), 2))
b = bool(int(input("b: "), 2))
c = bool(int(input("bin: "), 2))

d = XOR(a,b)
e = XOR(d,c)
f = AND(NOT(d), c)
g = AND(NOT(a), b)
h = OR(f, g)
print("Borrow:", h)
print("Diff:", e)
