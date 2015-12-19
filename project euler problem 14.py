import time
start_time = time.time()
def collatz(n):
   if n%2 == 0:
      return n/2
   if n%2 == 1:
      return 3*n+1

def collatz_chain(n):
   chain = []
   while n != 1:
      chain.append(n)
      n = collatz(n)
   chain.append(n)
   return chain

"""
chains = []
for i in range(1,100000):
   cur_chain = collatz_chain(i)
   cur_chain_length = len(cur_chain)
   chains.append((cur_chain_length, cur_chain))
max_length = max([x[0] for x in chains]) # find the maximum first value (length) of each tuple
longest_chain = [x for x in chains if x[0] == max_length]
ans = longest_chain[0][1][0]
print(ans)
"""

chains = []
for i in range(1,1000001):
   cur_chain = collatz_chain(i)
   cur_chain_length = len(cur_chain)
   chains.append((i, cur_chain_length))
max_length = max([x[1] for x in chains]) # find the maximum first value (length) of each tuple
longest_chain = [x for x in chains if x[1] == max_length]
end_time = time.time()
elapsed_time = end_time - start_time
print("elapsed time = ", elapsed_time, " seconds")
print(longest_chain)

# max_length = max

# BRUTE FORCE DOESNT WORK. run time an issue.  May need to find a way to cache results.  If the chain hits a value in a previously-calculated
# chain, then return the current length + the prev chain length, store and and the starting value

"""
exec(open("C:\\Users\\calkinsn\\Desktop\\Scripts\\Python\\project euler problem 14.py").read())

def collatz(n):
   while True:
      if n%2 == 0:
         n = n/2
         yield n/2
      if n%2 == 1:
         n = 3*n+1
         yield 3*n+1

   while cur != 1:
      if cur%2 == 0:
         cur = cur/2
      else cur = 3*cur + 1
      chain.append(cur)
   chain.append(cur)
"""

# make generator that yields the next number in the chain?