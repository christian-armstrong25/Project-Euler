'''
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 * 99

Find the largest palindrome made from the product of two 3-digit numbers.
'''

# checking if palindrome is much faster than checking if product of 3-digit numbers
def is_palindrome(x: int) -> bool:
  x = str(x)
  for i in range(len(x)//2):
    if x[i] != x[-1 - i]:
      return False
  return True

# start with 999 and 999
# Either subtract from left or both, no need for right (commutative)
def largest_three_digit_palindrome():
  ans = 0
  # start at 0, subraction and increment
  for decrement in range(0, 100): # arbitrary
    # start with subtraction all on one left
    # transition to all on both by subtracting on right
    left = 999 - decrement
    for right in range(999, left-1, -1):
      if is_palindrome(left * right):
        ans = max(ans, left * right)
  return ans

print(largest_three_digit_palindrome())