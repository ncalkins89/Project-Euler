# By considering the terms in the Fibonacci sequence whose values do not 
# exceed four million, find the sum of the even-valued terms.

import math
def F(n):
   return round(((1 + math.sqrt(5))**n - (1 - math.sqrt(5))**n) / ((2**n)*math.sqrt(5)))
i=1
ans=0
while F(i) < 4000000:
   if(F(i) % 2 == 0):
      ans = ans + F(i)
   i = i + 1
print(ans)