num=int(input("enter a number:"))
sum=0
temp=num
while temp>0:
	digit=temp%10
	sum+=digit**3
	temp//=10
	if num==sum:
		print("given number is armstrong number")
	else:
		print("given number is not an armstrong number") 