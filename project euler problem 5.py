# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""
while i%2 + i%3 + i%4 + i%5 + i%6 + i%7 + i%8 + i%9 + i%10 + i%11 + i%12 + i%13 + i%14 + i%15 + i%16 + i%17 + i%18 + i%19 + i%20 != 0:
   i += 1
print(i)
"""
i=11
while i%11 + i%12 + i%13 + i%14 + i%15 + i%16 + i%17 + i%18 + i%19 + i%20 != 0:
   i += 11
print(i)