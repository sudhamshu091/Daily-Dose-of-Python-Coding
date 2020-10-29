string = input("Enter word or number:")
print("It ia a palindrome" if string == string[::-1] else "It is not a palindrome")
