def factor(n):
   i=2
   factors = []
   while n != 1:
      while(n%i == 0):  # we found a factor!
         factors.append(i)
         n = n / i
      i += 1
   return factors
ans = factor(600851475143)
print(ans)

"""
# mod 2 --> if 0, add 2 to list and divide n by 2
# mod 3 --> if 0, add 3 to list and divide n by 3
# continue until n divided by i is 1

12
12mod2 = 0
add 2 to the list and divide by 2 -->
6mod2 = 0 
add 2 to the list and divide by 2 -->
3mod2 != 0 --> move onto 3
3mod3 = 0 --> 
add 3 to the list and divide by 3
n is 1, so stop.
"""