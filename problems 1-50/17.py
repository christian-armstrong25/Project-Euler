'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words,
how many letters would be used?

NOTE: Do not count spaces or hyphens.
'''

# sum of names 1-9
# sum of name 10-19
# "twenty" + "twenty" * sum of names 1-9
# ... "thirty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"
# + "one hundred"

one_to_nine = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
ten_to_nineteen = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens_digits = ["twenty", "thirty", "forty","fifty", "sixty", "seventy", "eighty", "ninety"]

sum_of_one_to_nine = sum([len(x) for x in one_to_nine])
sum_of_ten_to_nineteen = sum([len(x) for x in ten_to_nineteen])

sum_of_twenty_to_ninety_nine = 0
for tens_digit in tens_digits:
  sum_of_twenty_to_ninety_nine += 10 * len(tens_digit) + (sum_of_one_to_nine)
sum_of_one_to_ninety_nine = sum_of_one_to_nine + sum_of_ten_to_nineteen + sum_of_twenty_to_ninety_nine

sum_of_one_to_one_thousand = sum_of_one_to_ninety_nine
for hundreds_digit in one_to_nine:
  hundred = len(hundreds_digit) + len("hundred")
  sum_of_one_to_one_thousand += hundred + 99 * (hundred + len("and")) + sum_of_one_to_ninety_nine
sum_of_one_to_one_thousand += len("onethousand")
print(sum_of_one_to_one_thousand)
