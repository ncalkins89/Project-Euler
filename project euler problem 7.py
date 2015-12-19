# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10001st prime number?

def factor(n):
   i=2
   factors = []
   while n != 1:
      while(n%i == 0):  # we found a factor!
         factors.append(i)
         n = n / i
      i += 1
   return factors
prime_list = []
i=1
while len(prime_list) != 10001:
   factors = factor(i)
   if(factors == [i]):
      prime_list.append(i)
      print(len(prime_list), prime_list[len(prime_list)-1])
   i += 1