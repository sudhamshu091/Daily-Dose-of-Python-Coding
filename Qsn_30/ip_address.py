import re
ip = input("Enter IP address:") 
string = re.sub('\.[0]*', '.', ip)
print(string)
