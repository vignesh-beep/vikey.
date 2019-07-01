lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))
 
for num2 in range(lower,upper + 1):
   
   sum1 = 0
 
   
   temp = num2
   while temp > 0:
       digit = temp % 10
       sum1 += digit ** 3
       temp //= 10
 
   if num2 == sum1:
       print(num2)
