'''
Let d(n) be defined as the sum of the divisors of n.
If d(a) = b and d(b) = a where a != b, then a and b are an amicable pair
and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1,2,4,5,10,11,20,22,44,55,110;
therefore d(220) = 284. The proper divisors of 284 are 1,2,4,71, and 142;
so d(284) = 220.

Evaluate the sum of all the amicable numbers below 10,000.
'''
import math

N = 10_000

def d(n: int) -> int:
  d_n = 1 # 1 but not self are proper divisors
  # other divisors are factors less than root that divide and their cofactors
  for divisor in range(2, math.floor(math.sqrt(n))+1):
    if n % divisor == 0:
      d_n += divisor + n//divisor
  return d_n

amicable_numbers = []
results = {} # d(n) -> n

for n in range(1, N):
  d_n = d(n)
  # if there exists d(a) == b and a == d(b)
  if n in results and results[n] == d_n:
    amicable_numbers.append(n)
    amicable_numbers.append(d_n)
  results[d_n] = n

print(sum(amicable_numbers))
