'''
The following iterative sequence is defined for the set of positive integers:

n -> n/2 (if n is even)
n -> 3n + 1 (if n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz Problem),
it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

N = 1_000_000
ans = (1, 1) # (starting number, chain_length)
for start in range(2, N):
  chain_length = 1 # 1 at the end
  x = start
  while x != 1:
    chain_length += 1
    if x % 2 == 0: # even
      x = x//2
    else: # odd
      x = 3*x + 1

  if chain_length > ans[1]:
    ans = (start, chain_length)
print(ans[0])
