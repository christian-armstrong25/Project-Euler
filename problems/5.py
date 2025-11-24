'''
2520  is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

# At least 2520 since it is the smallest divisible by 1 to 10
# 2520 works because
print(5 * 7 * 8 * 9)
# start with 10!
# remove redundant factors:
# right to left, if prime factors found in numbers to left, remove

print(5 * 7 * 9 * 11 * 13 * 16 * 17 * 19)