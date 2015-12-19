# Find the sum of all the multiples of 3 or 5 below 1000.

# set ans = 0
# loop through i=1 to 1000
# test if i mod 3 is 0 or if i mod 5 is 0.  If so, ans = ans + i

ans = 0
for i in range(1,1000):
   if(i%3==0 or i%5==0):
      ans = ans + i
   print(ans)