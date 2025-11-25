'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example 3^2 + 4^2 = 9 + 16 = 25 = 5^2

There exists exactly one Pythagorean triplet for which a + b + c = 1000
Find the product abc.
'''

# a + b + c = 1000
# a^2 + b^2 = c^2
# a < b < c
# a * b * c = ?

for c in range(334, 997): # must be greater than 1/3 of 1000 for three lesser numbers to sum to 1000
  for b in range((1000-c)//2, c): # b < c, must be greater than half the remainder to sum to 1000
    a = 1000 - c - b # a + b + c = 1000
    if a < 0: # natural numbers only
      break
    if a**2 + b**2 == c**2: # pythagorian triplet
      print(f"{a} < {b} < {c}")
      print(f"{a} + {b} + {c} = {a + b + c}")
      print(f"{a}^2 + {b}^2 = {a**2} + {b**2} = {a**2 + b**2} = {c}^2")
      print(f"{a} * {b} * {c} = {a * b * c}")
