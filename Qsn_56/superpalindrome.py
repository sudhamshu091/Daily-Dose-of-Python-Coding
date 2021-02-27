def issuperpalindrome(n,n_square):
    if ispalindrome(n) and ispalindrome(n_square):
        return True
    return False
def ispalindrome(string):
    if string == string[::-1]:
        return True
    return False

n = int(input("Enter the number:"))
n_square = str(n*n)
n = str(n)
print(issuperpalindrome(n,n_square))
