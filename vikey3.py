num2 = int(input())
temp1 = num2
rev = 0
while temp1 != 0:
	rev = (rev * 10) + (temp1 % 10)
	temp1 = temp1 // 10
if num2 == rev:
	print("yes")
else:
	print("no")
