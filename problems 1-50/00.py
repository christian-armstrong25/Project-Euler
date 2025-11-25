'''
A number is a perfect square, or a square number, if it is the square of a positive integer.
For example, 25 is a square number because 5^2 = 5 * 5 = 25; it is also an odd square.

The first 5 square numbers are: 1, 4, 9, 16, 25,
and the sum of the odd squares is 1 + 9 + 25 = 35.

Among the first 802 thousand square numbers, what is the sum of all the odd squares?
'''

# Odd squares come only from squaring odd numbers:
# A number is odd if it can be written as 2m + 1, and even if written as 2m
# 2n * 2n = 4n^2 = 2m where m = 2n^2
# (2n + 1) * (2n + 1) = 4n^2 + 4n + 1 = 2m + 1 where m = 2n^2 + 2n
# So we just need to sum the squares of all the odd numbers between 1 and 802k

ans = 0
N = 802_000

for x in range(1, N, 2):
  ans += x**2
print(ans)


def __main__():
  print("Hello World")