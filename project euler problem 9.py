# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

# c = sqrt(a2 +b2)
# a+b+c = 1000

import math
import time

def pythag_triplet_sum(n):
   for a in range (1, n-1):
      for b in range (1, n-a-1):
         c = n-a-b
         if a**2 + b**2 == c**2:
            return(a, b, c, a*b*c)

"""
while a + b + math.sqrt(a**2 + b**2) != 30:
   for a in range(1, 29):
      print("attempt =", attempt)
      for b in range(attempt, 30-attempt):
         if a + b + math.sqrt(a**2 + b**2) > 30:
            break
         b += 1
         print("a =",a, "b =",b, "c=",math.sqrt(a**2 + b**2), "a+b+c =", a + b + math.sqrt(a**2 + b**2),attempt)
      attempt += 1
print (a, b, math.sqrt(a**2 + b**2), a*b*math.sqrt(a**2 + b**2)) # answer

need a2 + b2 = c2
and a + b + c = 1000

c = sqrt(a2+b2)

a + b + sqrt(a2 + b2) = 1000

start at a=2, b=2
test if the condition is true (=1000)
if not, increment b and test again
continue until the result is greater than 1000
when it is, increment a, reset b to 2, and try again
"""