import math
# generator that returns the next triangular number
def tri():
   i = 0
   t = 1
   while True:
      t += i
      yield t + i
      i += 1
# returns all factors (including nonprimes) of n
def factor(n):
   factors = []
   for i in range(1, math.ceil((n+1)/2)):
      if(n%i == 0):
         factors.append(i)
   factors.append(n)
   return(factors)

tri_gen = tri()
factorlist = []
for t in tri_gen:
   factorlist = factor(t)
   print(t, len(factorlist))
   if len(factorlist) >= 500:
      break
# exec(open("C:\\Users\\calkinsn\\Desktop\\Scripts\\Python\\project euler problem 12.py").read())