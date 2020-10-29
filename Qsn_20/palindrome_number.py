n = int(input("Enter the number you want to check for palindrome:"))
temp = n
reverse = 0
while (n > 0):
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10
if (temp == reverse):
    print("It is a palindrome")
else:
    print("It is not a palindrome")
