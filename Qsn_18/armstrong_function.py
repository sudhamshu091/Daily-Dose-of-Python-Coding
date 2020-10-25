import time
def Armstrong_Number(Number):
           Sum = 0
           count = 0

           Temp = Number
           while Temp > 0:
                      count = count + 1
                      Temp = Temp // 10

           Temp = Number
           for n in range(1, Temp + 1):
                      Reminder = Temp % 10
                      Sum = Sum + (Reminder ** count)
                      Temp //= 10
           return Sum
start_time = time.time()
Number = int(input("Enter the Number to Check for Armstrong: "))

if (Number == Armstrong_Number(Number)):
    print("%d is Armstrong Number" %Number)
else:
    print("%d is Not a Armstrong Number" %Number)
end_time = time.time()
print("Time elapsed:",start_time - end_time)
#Output
#Enter the Number to Check for Armstrong: 370
#370 is Armstrong Number
#Time elapsed: -3.4470980167388916
#Enter the Number to Check for Armstrong: 143
#143 is Not a Armstrong Number
#Time elapsed: -4.066716909408569
