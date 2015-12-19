# exec(open("C:\\Users\\calkinsn\\Desktop\\Scripts\\Python\\project euler problem 17.py").read())
import math
num_dict = {
   0: 'zero'
   ,1: 'one'
   ,2: 'two'
   ,3: 'three'
   ,4: 'four'
   ,5: 'five'
   ,6: 'six'
   ,7: 'seven'
   ,8: 'eight'
   ,9: 'nine'
   ,10: 'ten'
   ,11: 'eleven'
   ,12: 'twelve'
   ,13: 'thirteen'
   ,14: 'fourteen'
   ,15: 'fifteen'
   ,16: 'sixteen'
   ,17: 'seventeen'
   ,18: 'eighteen'
   ,19: 'nineteen'
   ,20: 'twenty'
   ,30: 'thirty'
   ,40: 'forty'
   ,50: 'fifty'
   ,60: 'sixty'
   ,70: 'seventy'
   ,80: 'eighty'
   ,90: 'ninety'
}
place_dict = {
   0: ''
   ,1: 'thousand'
   ,2: 'million'
   ,3: 'billion'
   ,4: 'trillion'
}
def two_digit_num_to_text(n):
   string_num = str(n)
   length = len(string_num)
   digit_list = []
   ans = ""
   for letter in string_num:
      digit_list.append(letter)
   if length == 1:
      ans = num_dict[int(digit_list[0])]
   if length == 2 and n <= 19:
      ans = num_dict[int(digit_list[0] + digit_list[1])]
   if length == 2 and n > 19 and digit_list[1] == "0":
      ans = num_dict[int(digit_list[0] + digit_list[1])]
   if length == 2 and n > 19 and digit_list[1] != "0":
      ans = num_dict[int(digit_list[0] + "0")] + "-" + num_dict[int(digit_list[1])]
   return ans
def three_digit_num_to_text(n):
   string_num = str(n)
   length = len(string_num)
   digit_list = []
   ans = ""
   for letter in string_num:
      digit_list.append(letter)
   if length <= 2:
      ans = two_digit_num_to_text(n)
   if length == 3:
      ans = num_dict[int(digit_list[0])] + " hundred "
      if digit_list[1] != '0' or digit_list[2] != '0':
         ans += two_digit_num_to_text(int(digit_list[1] + digit_list[2]))
   return(ans)
def split_integer(n):
   triple_digit_list = []
   string_num = str(n)
   length = len(string_num)
   remainder = length % 3
   if length <= 3:
      triple_digit_list.append(string_num)
   else: 
      triple_digit_list.append(string_num[0:remainder]) # first add part in front of first comma
      for i in range (0, (length-remainder)//3):        # then add all remaining sets of 3 digits
         triple_digit_list.append(string_num[remainder + i*3 : remainder + (i+1)*3])
   for digit_set in triple_digit_list:                  # remove empty string that gets added if there is no remainder
      if digit_set == '':
         triple_digit_list.remove(digit_set)
   return triple_digit_list
"""
def n_digit_num_to_text(n):
   ans = ""
   triple_digit_list = split_integer(n)
   num_chunks = len(triple_digit_list)
   for (i, chunk) in enumerate(triple_digit_list):
      if int(chunk) != 0:
         ans += three_digit_num_to_text(int(chunk)) + " " + place_dict[num_chunks - i - 1] + " "
   return(ans)
"""
def n_digit_num_to_text(n):
   ans = ""
   ands = 0
   length = len(str(n))
   letters = 0
   triple_digit_list = split_integer(n)
   num_chunks = len(triple_digit_list)
   for (i, chunk) in enumerate(triple_digit_list):
      if int(chunk) != 0:
         ans += three_digit_num_to_text(int(chunk)) + " " + place_dict[num_chunks - i - 1] + " "
      if int(chunk) > 100:
         ands += 1
   if ands == 0 and n > 100:
      ands = 1
   for letter in ans:
      if letter != "-" and letter != " ":
         letters += 1
   letters += ands*3
   return(letters)
cumul_letters = 0
for i in range(1000,1001):
   cumul_letters += n_digit_num_to_text(i)
print(cumul_letters)
"""
cumul_letters = 0
for i in range(1,1001):
   text = n_digit_num_to_text(i)
   length = len(str(i))
   letters = 0
   for letter in text:
      if letter != "-" and letter != " ":
         letters += 1
   letters += ands*3
   cumul_letters += letters
print(cumul_letters)
"""