#If the number is less than or equal to one, return False.
#If the number is divisible by any number, then the function will return False.
#After the loop, return True.
import time
def is_prime(n):
   if n <= 1:
      return False
   else:
      for i in range(2, n):
         if n % i == 0:
            return False
      else:
         return True
start_time = time.time()
primes = 0
for i in range(3000):
   if is_prime(i):
      primes += 1
print("Numebr of prime number in the range:",primes)
end_time = time.time()
print("Execution time:",end_time - start_time)

#Result
#Numebr of prime number in the range: 430
#Execution time: 0.09002470970153809
