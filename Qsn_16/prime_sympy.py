import sympy
import time
start_time = time.time()
end = int(input( "End limit :"))
prime = list(sympy.primerange(0,end+1))
print (prime)
end_time = time.time()
print(start_time - end_time)
