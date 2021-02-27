def issuperpalindrome(n,n_square):
    if ispalindrome(n) and ispalindrome(n_square):
        return True
    return False

def ispalindrome(number):
    temp = number
    reverse = 0
    while number > 0:
        digit = number % 10
        reverse = reverse * 10 + digit
        number = number // 10
    if temp == reverse:
        return True
    return False


n = int(input("Enter the number:"))
n_square = n*n
print(issuperpalindrome(n,n_square))
