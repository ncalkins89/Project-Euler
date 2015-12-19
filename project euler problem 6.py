# sum of squares minus square of sum for first 100 natural numbers
sum_sq=0
sum=0
for i in range(1,101):
   sum_sq += i**2
for j in range(1,101):
   sum += j
sq_sum = sum**2
print(sum_sq)
print(sum)
print(sq_sum)
print(sq_sum - sum_sq)