'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
'''

# Dividing as we go, all prime factors are going to be less than the sqrt(N) or N is prime
# proof:
# if equal to sqrt(N), then co-factor will be itself
# if greatest prime factor > sqrt(N), then co-factor must be less than sqrt(N),
# and thus we already removed it, and now N <= sqrt(N)
# so the greatest prime factor can't be greater than sqrt(N)


import math

largest_prime = 1
N = 600851475143

upper_bound = math.floor(math.sqrt(N))
if upper_bound % 2 == 0:
  upper_bound += 1
# primes must be odd, so can skip every other number
for x in range(upper_bound, 3, -2):  # count down to stop early
    if N % x == 0:  # factor of N
      # and prime
      is_prime = True
      for y in range(3, math.floor(math.sqrt(x))+1, 2):
        if x % y == 0:
          is_prime = False
          break

      if is_prime:
        largest_prime = x
        break

if largest_prime == 1:
  largest_prime = N
print(largest_prime)
