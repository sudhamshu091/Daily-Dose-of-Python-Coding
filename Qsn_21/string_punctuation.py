from string import punctuation
string = "/{Python @ is actually an > interesting //language@ "
replace = '#'
for char in punctuation:
    string = string.replace(char, replace)

print("String after replacement is: ", string)
