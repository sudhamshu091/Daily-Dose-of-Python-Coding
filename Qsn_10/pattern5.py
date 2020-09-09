n=int(input("Enter a positive number:"))
def pattern5(n):
        for i in range(n):
                for j in range(i+1):
                        print(i,end=" ")
                        i=i+1
                print()
pattern5(n)
