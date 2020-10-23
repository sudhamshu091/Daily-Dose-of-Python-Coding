import time
import math
def is_prime(n):
   if n <= 1:
      return False
   elif n == 2:
      return True
   elif n > 2 and n % 2 == 0:
      return False
   else:
      for i in range(3, int(math.sqrt(n)) + 1, 2):
         if n % i == 0:
            return False
      return True
start_time = time.time()
primes = 0
for i in range(3000):
   if is_prime(i):
      primes += 1
print("Total primes in the range:",primes)
end_time = time.time()
print("Execution time:",end_time - start_time)
#Result
#Total primes in the range: 430
#Execution time: 0.0479888916015625
