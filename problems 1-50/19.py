'''
You are given the following information, but you may prefer to do some research for yourself.
- 1 Jan 1900 was a Monday.
- Thirty days has September,
- April, June and November.
- All the rest have thirty-one,
- Saving February alone,
- Which has twenty-eight, rain or shine.
- And on leap years, twenty-nine.
- A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

# Let day_of_week be a digit mod 7
# we figure out how much to add between first of the months and keep a count of
# sundays (0) [0: "Sunday", ..., 6: "Saturday"]

day_of_week = 1 + (365 % 7)  # 1 Jan 1900 was a Monday and 1900 had 365 days (not leap year becuase indivisible by 400)
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
sundays_on_firsts = 0

for year in range(1901, 2001):
  leap_year = False
  # A leap year occurs on any year evenly divisible by 4
  if year % 4 == 0:
    # but not on a century unless it is divisible by 400.
    if year % 100 != 0 or year % 400 == 0:
      leap_year = True

  for days in days_in_month:
    # And on leap years, twenty-nine.
    if days == 28 and leap_year:
      day_of_week += 1

    day_of_week = (day_of_week + days) % 7
    if day_of_week == 0:
      sundays_on_firsts += 1

print(sundays_on_firsts)
