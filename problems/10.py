'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17

Find the sum of all the primes below two million.
'''

import math

N = 2_000_000
primes = [2]

for x in range(3, N, 2): # only odd primes after 2
  for p in primes:
    if p > math.floor(math.sqrt(x)): # no factors other than itself will be greater than it's root
      primes.append(x)
      break
    if x % p == 0: # factor other than 1 or itself
      break

print(sum(primes))
