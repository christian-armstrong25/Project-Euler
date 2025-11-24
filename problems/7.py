'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, 13,
we can see that the 6th prime is 13.

What is the 10,001st prime number
'''
import math

N = 10_001
primes = [2]

x = 3
while len(primes) < N:
  for p in primes:
    if p > math.floor(math.sqrt(x)):
      primes.append(x)
      break
    if x % p == 0:
      break
  x += 2

print(primes[-1])