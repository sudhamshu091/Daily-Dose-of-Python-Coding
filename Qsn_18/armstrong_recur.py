import time
Sum = 0
count = 0

def Count_Of_Digits(Number):
           global count
           if(Number > 0):
                      count = count + 1
                      Count_Of_Digits(Number // 10)
           return count

def Armstrong_Number(Number, Times):
           global Sum
           if(Number > 0):
                      Reminder = Number % 10
                      Sum = Sum + (Reminder ** count)
                      Armstrong_Number(Number //10, count)
           return Sum
start_time = time.time()
Number = int(input("Enter the Number to Check for Armstrong: "))

count = Count_Of_Digits(Number)
Sum = Armstrong_Number(Number, count)
if (Number == Sum):
    print("%d is Armstrong Number" %Number)
else:
    print("%d is Not a Armstrong Number" %Number)
end_time = time.time()
print("Time elapsed:", start_time - end_time)
#Output
#Enter the Number to Check for Armstrong: 370
#370 is Armstrong Number
#Time elapsed: -3.313142776489258
#Enter the Number to Check for Armstrong: 143
#143 is Not a Armstrong Number
#Time elapsed: -3.4391980171203613
