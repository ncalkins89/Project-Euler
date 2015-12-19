# exec(open("C:\\Users\\calkinsn\\Desktop\\Scripts\\Python\\project euler problem 20.py").read())
import math
def add_digits(n):
   string_num = str(n)
   ans = 0
   for digit in string_num:
      ans += int(digit)
   return ans
add_digits(math.factorial(100))