# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

# generate a product of 2 three-digit numbers
# test if it's a palindrome.  If so, add to list
# find largest value in list

def is_palindrome(product):
   return product == product[::-1]
palindromes=[]
for i in range(999,100,-1):
   for j in range(999,100,-1):
      mystring = str(i*j)
      if(is_palindrome(mystring)) == True:
         palindromes.append([i*j])
print(max(palindromes))