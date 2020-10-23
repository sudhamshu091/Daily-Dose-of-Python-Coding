#sieve method
#reference:http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
import time
def SieveOfEratosthenes(n):
    prime = [True for i in range(n+1)]

    p = 2
    while(p * p <= n):
        if (prime[p] == True):
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    c = 0
    for p in range(2, n):
        if prime[p]:
            c += 1
    return c
t0 = time.time()
c = SieveOfEratosthenes(100000)
print("Total prime numbers in range:", c)

t1 = time.time()
print("Time required:", t1 - t0)
