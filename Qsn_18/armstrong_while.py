import time
start_time = time.time()
Number = int(input("Enter the Number to Check for Armstrong: "))
Sum = 0
count = 0

Temp = Number
while Temp > 0:
           count = count + 1
           Temp = Temp // 10

Temp = Number
while Temp > 0:
           Reminder = Temp % 10
           Sum = Sum + (Reminder ** count)
           Temp //= 10
if Number == Sum:
           print("%d is Armstrong Number" %Number)
else:
           print("%d is Not a Armstrong Number" %Number)
end_time = time.time()
print("Time elapsed:",start_time - end_time)
#Output
#Enter the Number to Check for Armstrong: 143
#143 is Not a Armstrong Number
#Time elapsed: -3.456416606903076
#Enter the Number to Check for Armstrong: 370
#370 is Armstrong Number
#Time elapsed: -3.9342691898345947
